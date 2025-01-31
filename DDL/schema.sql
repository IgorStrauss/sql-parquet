-- Criando schema Parquet
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'Parquet')
BEGIN
    EXEC('CREATE SCHEMA [Parquet];');
END
ELSE
BEGIN
    PRINT 'O Schema Parquet já existe.';
END

