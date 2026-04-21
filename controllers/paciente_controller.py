from flask import Blueprint, render_template, request, redirect, session
from models.paciente import Paciente
from extensions import db

paciente_bp = Blueprint("paciente", __name__)


# =========================
# 📌 LISTAR + CADASTRAR
# =========================
@paciente_bp.route("/pacientes", methods=["GET", "POST"])
def pacientes():

    if not session.get("logado"):
        return redirect("/login")

    if request.method == "POST":

        novo = Paciente(
            nome=request.form["nome"],
            idade=request.form["idade"],
            telefone=request.form["telefone"],
            email=request.form["email"]
        )

        db.session.add(novo)
        db.session.commit()

        return redirect("/pacientes")

    pacientes = Paciente.query.all()

    return render_template("pacientes.html", pacientes=pacientes)


# =========================
# 🗑 EXCLUIR PACIENTE (CORRIGIDO)
# =========================
@paciente_bp.route("/excluir/<int:id>")
def excluir(id):

    if not session.get("logado"):
        return redirect("/login")

    paciente = Paciente.query.get(id)

    if paciente:
        db.session.delete(paciente)
        db.session.commit()

    return redirect("/pacientes")
