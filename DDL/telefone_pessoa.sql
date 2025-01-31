-- Criando a tabela TelefonePessoa
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'TelefonePessoa' AND schema_id = SCHEMA_ID('Parquet'))
BEGIN
    -- Criando a tabela TelefonePessoa
    CREATE TABLE [Parquet].[TelefonePessoa] (
    Id_TelefonePessoa INT IDENTITY(1,1) PRIMARY KEY,
    Id_Pessoa INT NOT NULL,
    DDD CHAR(2) NOT NULL,
    Numero VARCHAR(9) NOT NULL,
    Is_Active BIT DEFAULT(0)
);
END
ELSE
BEGIN
    PRINT 'A tabela TelefonePessoa já existe.'
END