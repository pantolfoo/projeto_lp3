# Flask: aplicações WEB, comunhão de bibliotecas
# Não precisa editar o código para editar o conteúdo da página

# importa a classe Flask do modulo flask
from flask import Flask
# flask: modulo
# Flask: classe

from validate_docbr import CPF, CNPJ


# instancia um objeto flask que representa a aplicação
app = Flask('minha aplicação')

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# app = Flask

# /
@app.route("/")
def home():
    home_retorno = "<h1> Home page </h1>"
    return home_retorno

# /contato 
@app.route("/contato")
def contatos():
    contatos_retorno = "<h1> Contatos </h1>"
    return contatos_retorno

# /produtos 
@app.route("/produtos")
def produtos():
    produtos_retorno = "<h1> Produtos </h1>"
    return produtos_retorno


# /cpf (devolver um cpf aleatório)
@app.route("/cpf")
def gerar_cpf():
    cpf = CPF ()
    cpf_retorno = "<h1>CPF Gerado:</h1>"
    cpf_retorno += cpf.generate((True))
    return cpf_retorno


# /cnpj (devolver um cnpj aleatório)
@app.route("/cnpj")
def gerar_cnpj():
    cnpj = CNPJ ()
    cnpj_retorno = "<h1>CNPJ Gerado:</h1>"
    cnpj_retorno += cnpj.generate((True))
    return cnpj_retorno


# /servicos (devolver um titulo com "Nossos serviços")
@app.route("/servicos")
def servicos():
    servicos_retorno = "<h1> Nossos serviços </h1>"
    return servicos_retorno

app.run()

