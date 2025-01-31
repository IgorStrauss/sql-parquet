-- Criando a tabela EnderecoPessoa
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'EnderecoPessoa' AND schema_id = SCHEMA_ID('Parquet'))
BEGIN
    -- Criando a tabela EnderecoPessoa
    CREATE TABLE [Parquet].[EnderecoPessoa] (
        Id_EnderecoPessoa INT IDENTITY(1,1) PRIMARY KEY,
        Id_Pessoa INT NOT NULL,
        Logradouro VARCHAR(100) NOT NULL,
        Complemento VARCHAR(100),
        Numero VARCHAR(10) NOT NULL,
        Is_Active BIT DEFAULT(0)
    );
END
ELSE
BEGIN
    PRINT 'A tabela EnderecoPessoa já existe.'
END
