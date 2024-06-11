# Flask: aplicações WEB, comunhão de bibliotecas
# Não precisa editar o código para editar o conteúdo da página

# importa a classe Flask do modulo flask
from flask import Flask
# flask: modulo
# Flask: classe

# instancia um objeto flask que representa a aplicação
app = Flask('minha aplicação')

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home: - / 

# app = Flask
@app.route("/")
def home():
    return "<h1> Home page </h1>"

# página contato: - /contato 
@app.route("/contato")
def contatos():
    return "<h1> Contatos </h1>"

# página produtos: - /produtos
@app.route("/")
def produtos():
    return "<h1> Produtos </h1>"

