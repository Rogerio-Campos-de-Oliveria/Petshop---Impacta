from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, init_db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    termo = request.args.get("q", "").strip()

    cconn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if termo:
        like = f"%{termo}%"
        cursor.execute(
            """SELECT * FROM clientes
               WHERE nome LIKE %s OR telefone LIKE %s OR email LIKE %s
               ORDER BY id DESC""",
            (like, like, like),
        )
    else:
        cursor.execute("SELECT * FROM clientes ORDER BY id DESC")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("clientes.html", clientes=clientes, termo=termo)


@app.route("/clientes/novo", methods=["POST"])
def cadastrar_cliente():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form.get("email")
    endereco = request.form.get("endereco")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (%s, %s, %s, %s)",
        (nome, telefone, email, endereco),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("listar_clientes"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
