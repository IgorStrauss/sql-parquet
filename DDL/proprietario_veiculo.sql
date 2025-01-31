-- Criando a tabela ProprietarioVeiculo
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'ProprietarioVeiculo' AND schema_id = SCHEMA_ID('Parquet'))
BEGIN
    -- Criando a tabela ProprietarioVeiculo
    CREATE TABLE [Parquet].[ProprietarioVeiculo] (
    Id_Proprietario INT IDENTITY(1,1) PRIMARY KEY,
    Id_Pessoa INT NOT NULL,
    Id_Veiculo INT NOT NULL,
    Is_Active BIT DEFAULT(0)
);
END
ELSE
BEGIN
    PRINT 'A tabela ProprietarioVeiculo já existe.'
END