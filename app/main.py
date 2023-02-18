from flask import Flask, render_template, redirect, request

class Checklist:
    def __init__(self, nome):
        self.nome = nome

lista = []

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/tarefas')
def tarefas():
    return render_template("tarefas.html", list=lista)


@app.route('/criar', methods=['POST', ])
def criar():
    tarefa = request.form['info']
    tarefa2 = Checklist(tarefa)
    lista.append(tarefa2)
    return render_template("tarefas.html", list=lista)

# Deletar um item da lista, basta colocar -> deletar/indice_do_item
@app.route('/deletar/<int:indice>')
def deletar(indice):
    del lista[indice]
    return render_template("tarefas.html", list=lista)


@app.route('/<string:nome>')
def erro(nome):
    variavel = f'A página [{nome}] não existe'
    return render_template('error.html', variavel=variavel)


if __name__ == '__main__':
    app.run(debug=True)