import mysql.connector
import os


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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            especie VARCHAR(80) NOT NULL,
            raca VARCHAR(80),
            idade INT,
            cliente_id INT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        ) ENGINE=InnoDB
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            telefone VARCHAR(30) NOT NULL,
            especialidade VARCHAR(150)
        ) ENGINE=InnoDB
    """)

    conn.commit()
    cursor.close()
    conn.close()
