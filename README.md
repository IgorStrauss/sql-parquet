## Teste SQL, Parquet, API, Power BI

Teste para validar compressão dos dados com uso de arquivo [parquet](https://parquet.apache.org/)

Cenário de teste:

Banco de Dados SQL Server
 - Tabela *Veiculos*
 - Tabela *Pessoa*
 - Tabela *EnderecoPessoa*
 - Tabela *TelefonePessoa*
 - Tabela *ProprietarioVeiculo*


Tabela Veiculo:
 - Id_Veiculo  INT
 - Chassi      CHAR(10)
 - Marca       VARCHAR(45)
 - Modelo      VARCHAR(45)
 - Cor         VARCHAR(45)
 - Ano         INT
 - Ano_Modelo  INT

Tabela Pessoa:
 - Id_Pessoa  INT
 - CPF        CHAR(5)
 - Nome       VARCHAR(45)
 - Sobrenome  VARCHAR(45)

Tabela EnderecoPessoa:
 - Id_EnderecoPessoa INT
 - Id_Pessoa         INT
 - Logradouro        VARCHAR(100)
 - Complemento       VARCHAR(100)
 - Numero            VARCHAR(10)
 - Is_Active         BIT DEFAULT(0)

Tabela TelefonePessoa:
 - Id_TelefonePessoa INT
 - Id_Pessoa         INT
 - DDD               CHAR(2)
 - Numero            VARCHAR(9)
 - Is_Active         BIT DEFAULT(0)

Tabela ProprietarioVeiculo:
 - Id_Proprietario INT
 - Id_Pessoa       INT
 - Id_Veiculo      INT
 - Is_Active       BIT DEFAULT(0)


### Iniciar projeto

## Projeto consiste em: Criar toda estrutura no Banco de Dados para validar item a item, ou, utilizar os arquivos .parquet que jã estão incluidos no diretorio data

## Os arquivos .parquet que estão disponiveis, podem ser utilizados diretamente no arquivo Power BI, ou, consumido nas consultas geradas pela API que está também no projeto

**Adicionar credenciais para banco de dados que será utilizado para teste no arquivo**
**```config.database.config_db.py```**

Ao iniciar projeto, será criado automaticamente o **schema** ```Parquet```

 - Criar ambiente virtual
 - Ativar ambiente virtual
 - Instalar bibliotecas com comando ```pip install -r requirements.txt``` ou ```task requirements```

### Criando Schema e Tabelas no Banco de Dados SQL Server

```task table```

### Populando as tabelas com 100 registros Fake

```task insert-table```

### Iniciando API para conculta dos dados via .Parquet

```task run```

### Arquivo .PBIP incluido no projeto para validação