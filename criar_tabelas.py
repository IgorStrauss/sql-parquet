import logging
import os
import time

from config.database.config_db import conectar_ao_banco
from config.utils.logs import logger


class ExecutarScriptsSQL:
    def __init__(self, arquivos_sql):
        """
        Inicializa a classe com a lista de arquivos SQL a serem executados.
        :param arquivos_sql: Lista de caminhos dos arquivos SQL.
        """
        self.arquivos_sql = arquivos_sql
        self.conn = None

        logger()

    def conectar_ao_banco(self):
        """
        Estabelece a conexão com o banco de dados.
        """
        self.conn = conectar_ao_banco()
        if self.conn:
            logging.info("Conexão bem-sucedida ao banco de dados.")
        else:
            logging.error("Falha ao conectar ao banco de dados.")

    def verificar_tabela_existente(self, nome_tabela):
        """
        Verifica se uma tabela existe no banco de dados.
        :param nome_tabela: Nome da tabela a ser verificada.
        :return: True se a tabela existir, False caso contrário.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{nome_tabela}'"
        )
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado > 0

    def executar_script_sql(self, caminho_script):
        """
        Executa um script SQL no banco de dados.
        :param caminho_script: Caminho para o arquivo SQL.
        """
        try:
            with open(caminho_script, "r", encoding="utf-8") as file:
                sql_script = file.read()

            nome_tabela = caminho_script.split("\\")[-1].replace(".sql", "")

            if self.verificar_tabela_existente(nome_tabela):
                logging.info(
                    f"A tabela '{nome_tabela}' já existe. Script {caminho_script} não será executado."
                )
            else:
                cursor = self.conn.cursor()
                cursor.execute(sql_script)
                logging.info(
                    f"Tabela '{nome_tabela}' criada com sucesso usando o script: {caminho_script}"
                )
                self.conn.commit()
                cursor.close()

        except Exception as e:
            logging.error(f"Erro ao executar o script SQL: {e}")
            logging.exception("Detalhes do erro:")

    def executar_scripts(self):
        """
        Itera sobre a lista de arquivos SQL e executa cada um.
        """
        if self.conn:
            for caminho_script in self.arquivos_sql:
                logging.info(
                    f"Iniciando a execução do script: {caminho_script}"
                )
                self.executar_script_sql(caminho_script)
                time.sleep(1)
            self.fechar_conexao()
        else:
            logging.error(
                "Não foi possível executar os scripts. Conexão com o banco não estabelecida."
            )

    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conn:
            self.conn.close()
            logging.info("Conexão fechada.")
        else:
            logging.warning(
                "Não foi possível fechar a conexão, pois não estava aberta."
            )


# Lista de arquivos SQL a serem executados em sequencia - atende SO Windows, Linux e MacOS
arquivos_sql = [
    os.path.join("DDL", "schema.sql"),
    os.path.join("DDL", "veiculo.sql"),
    os.path.join("DDL", "pessoa.sql"),
    os.path.join("DDL", "endereco_pessoa.sql"),
    os.path.join("DDL", "telefone_pessoa.sql"),
    os.path.join("DDL", "proprietario_veiculo.sql"),
]

# Instancia e executa os scripts
if __name__ == "__main__":
    # Cria a instância da classe
    executor = ExecutarScriptsSQL(arquivos_sql)

    # Conectar ao banco
    executor.conectar_ao_banco()

    # Executar todos os scripts SQL
    executor.executar_scripts()
