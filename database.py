import mysql.connector
import os

# Dados de conexão - ajuste conforme seu MySQL local, ou defina
# as variáveis de ambiente DB_HOST, DB_USER, DB_PASSWORD, DB_NAME.
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", 3306)),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "1234"),
    "database": os.environ.get("DB_NAME", "petcare"),
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def _get_connection_sem_banco():
    config = DB_CONFIG.copy()
    config.pop("database")
    return mysql.connector.connect(**config)


def init_db():
    # cria o banco de dados "petcare" caso ainda não exista
    conn = _get_connection_sem_banco()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor.close()
    conn.close()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            telefone VARCHAR(30) NOT NULL,
            email VARCHAR(150),
            endereco VARCHAR(255)
        ) ENGINE=InnoDB
    """)
    conn.commit()
    cursor.close()
    conn.close()
