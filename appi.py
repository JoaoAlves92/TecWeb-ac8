from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cursos.html")
def cursos():
    return render_template("cursos.html")


@app.route("/disciplina.html")
def disciplina():
    return render_template("disciplina.html")


@app.route("/noticias.html")
def noticias():
    return render_template("noticias.html")


app.run()
