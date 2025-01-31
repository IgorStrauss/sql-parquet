-- Criando a tabela Pessoa
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Pessoa' AND schema_id = SCHEMA_ID('Parquet'))
BEGIN
    -- Criando a tabela Pessoa
    CREATE TABLE [Parquet].[Pessoa] (
    Id_Pessoa INT IDENTITY(1,1) PRIMARY KEY,
    CPF CHAR(5) NOT NULL,
    Nome VARCHAR(45) NOT NULL,
    Sobrenome VARCHAR(45) NOT NULL
);
END
ELSE
BEGIN
    PRINT 'A tabela Pessoa já existe.'
END