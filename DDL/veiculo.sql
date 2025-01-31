-- Criando a tabela Veiculos
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Veiculos' AND schema_id = SCHEMA_ID('Parquet'))
BEGIN
    -- Criando a tabela Veiculos
    CREATE TABLE [Parquet].[Veiculos] (
    Id_Veiculo INT IDENTITY(1,1) PRIMARY KEY,
    Chassi CHAR(10) NOT NULL,
    Marca VARCHAR(45) NOT NULL,
    Modelo VARCHAR(45) NOT NULL,
    Cor VARCHAR(45) NOT NULL,
    Ano INT NOT NULL,
    Ano_Modelo INT NOT NULL
);
END
ELSE
BEGIN
    PRINT 'A tabela Veiculos já existe.'
END