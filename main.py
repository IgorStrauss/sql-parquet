import pandas as pd
from fastapi import FastAPI

# Inicializando o app FastAPI
app = FastAPI()


# Função para carregar os dados de um arquivo parquet
def load_parquet(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_parquet(file_path, engine="pyarrow")
    except Exception as e:
        return {"error": str(e)}


# Definindo a rota para retornar todos os dados da tabela pessoa
@app.get("/pessoa/")
async def get_pessoa():
    df = load_parquet("data/pessoa.parquet")
    if isinstance(df, pd.DataFrame):
        return df.to_dict(orient="records")
    return {"error": "Erro ao carregar dados"}


# Definindo a rota para retornar dados de uma pessoa específica, pelo CPF
@app.get("/pessoa/{cpf}")
async def get_pessoa_by_cpf(cpf: str):
    df = load_parquet("data/pessoa.parquet")
    pessoa = df[df["CPF"] == cpf]
    if not pessoa.empty:
        return pessoa.to_dict(orient="records")
    return {"error": "Pessoa não encontrada"}


# Definindo a rota para retornar todos os dados da tabela veiculos
@app.get("/veiculos/")
async def get_veiculos():
    df = load_parquet("data/veiculos.parquet")
    if isinstance(df, pd.DataFrame):
        return df.to_dict(orient="records")
    return {"error": "Erro ao carregar dados"}


# Definindo a rota para retornar os veículos de uma pessoa pelo CPF
@app.get("/veiculos/{chassi}")
async def get_veiculos_by_chassi(chassi: str):
    # Carregar os dados do arquivo Parquet
    df = load_parquet("data/veiculos.parquet")

    veiculos = df[df["Chassi"].str.strip() == chassi.strip()]

    # Verificar se encontramos os veículos
    if not veiculos.empty:
        return veiculos.to_dict(orient="records")
    return {"error": "Veículos não encontrados"}
