import random

import factory

# Conexão com o banco de dados
from config_db import conectar_ao_banco
from factory import Faker


# Factory para a tabela Veiculos
class VeiculosFactory(factory.Factory):
    class Meta:
        model = dict

    Chassi = Faker("bothify", text="??????????")
    Marca = Faker("company")
    Modelo = Faker("word")
    Cor = Faker("color_name")
    Ano = Faker("year")
    Ano_Modelo = Faker("year")


# Factory para a tabela Pessoa
class PessoaFactory(factory.Factory):
    class Meta:
        model = dict  # Usamos dict para representar o modelo de dados

    CPF = Faker("bothify", text="?????")
    Nome = Faker("first_name")
    Sobrenome = Faker("last_name")


# Factory para a tabela EnderecoPessoa
class EnderecoPessoaFactory(factory.Factory):
    class Meta:
        model = dict

    Id_Pessoa = factory.LazyAttribute(lambda x: random.randint(1, 100))
    Logradouro = Faker("street_name")
    Complemento = Faker("secondary_address")
    Numero = Faker("building_number")
    Is_Active = Faker("boolean")


# Factory para a tabela TelefonePessoa
class TelefonePessoaFactory(factory.Factory):
    class Meta:
        model = dict

    Id_Pessoa = factory.LazyAttribute(lambda x: random.randint(1, 100))
    DDD = Faker("random_number", digits=2)
    Numero = factory.LazyAttribute(
        lambda x: str(random.randint(100000000, 999999999))
    )
    Is_Active = Faker("boolean")


# Factory para a tabela ProprietarioVeiculo
class ProprietarioVeiculoFactory(factory.Factory):
    class Meta:
        model = dict

    Id_Pessoa = factory.LazyAttribute(
        lambda x: random.randint(1, 100)
    )  # Relacionado a Pessoa
    Id_Veiculo = factory.LazyAttribute(
        lambda x: random.randint(1, 100)
    )  # Relacionado a Veiculo
    Is_Active = Faker("boolean")


# Função para inserir dados no banco de dados
def inserir_dados(conn, tabela, factory_class, quantidade=100):
    cursor = conn.cursor()

    for _ in range(quantidade):
        # Criar a instância do modelo com dados falsos
        dados = factory_class()
        campos = ", ".join(dados.keys())
        valores = ", ".join([f"'{v}'" for v in dados.values()])

        # Montar o comando SQL para inserção
        sql = f"INSERT INTO [Parquet].[{tabela}] ({campos}) VALUES ({valores})"
        cursor.execute(sql)

    conn.commit()
    print(f"{quantidade} registros inseridos na tabela {tabela}.")


# Função para rodar a inserção de dados
def rodar_insercao():
    conn = conectar_ao_banco()

    if conn:
        # Inserir dados nas tabelas usando as factories
        inserir_dados(conn, "Veiculos", VeiculosFactory)
        inserir_dados(conn, "Pessoa", PessoaFactory)
        inserir_dados(conn, "EnderecoPessoa", EnderecoPessoaFactory)
        inserir_dados(conn, "TelefonePessoa", TelefonePessoaFactory)
        inserir_dados(conn, "ProprietarioVeiculo", ProprietarioVeiculoFactory)

        conn.close()


if __name__ == "__main__":
    rodar_insercao()
