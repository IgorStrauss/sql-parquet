import pyodbc


def conectar_ao_banco():
    try:
        server = "server"
        database = "Dev"
        username = "username"
        password = "password"

        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        conn = pyodbc.connect(conn_str)

        cursor = conn.cursor()

        cursor.execute("SELECT 1;")
        resultado = cursor.fetchone()

        if resultado:
            print("Conexão bem-sucedida ao banco de dados!")
        else:
            print("Falha na conexão ao banco de dados.")

        return conn

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
