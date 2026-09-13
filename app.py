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

@app.route("/clientes/<int:cliente_id>/editar", methods=["GET"])
def editar_cliente_form(cliente_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()

    if cliente is None:
        return redirect(url_for("listar_clientes"))

    return render_template("editar_cliente.html", cliente=cliente)


@app.route("/clientes/<int:cliente_id>/editar", methods=["POST"])
def editar_cliente(cliente_id):
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form.get("email")
    endereco = request.form.get("endereco")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE clientes
           SET nome = %s, telefone = %s, email = %s, endereco = %s
           WHERE id = %s""",
        (nome, telefone, email, endereco, cliente_id),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("listar_clientes"))


@app.route("/clientes/<int:cliente_id>/excluir", methods=["POST"])
def excluir_cliente(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("listar_clientes"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
