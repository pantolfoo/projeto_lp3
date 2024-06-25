# Flask: aplicações WEB, comunhão de bibliotecas
# Não precisa editar o código para editar o conteúdo da página

# importa a classe Flask do modulo flask
from flask import Flask, render_template, request
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

lista_produtos = [
        {"nome": "Mais esperto que o diabo", "genero": "autoajuda"},
        {"nome": "É assim que acaba", "genero": "Romance"},
        {"nome": "Código limpo", "genero": "Informática linguagens"},
]


@app.route("/")
def home():
    home_retorno = "<h1> Home page </h1>"
    return render_template("home.html") 

# /contato 
@app.route("/contatos")
def contatos():
    return render_template("contatos.html") 

# /produtos 
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Mais esperto que o diabo", "genero": "autoajuda"},
        {"nome": "É assim que acaba", "genero": "Romance"},
        {"nome": "Código limpo", "genero": "Informática linguagens"},
    ]

    return render_template("produtos.html", produtos=lista_produtos) 


# /cpf (devolver um cpf aleatório)
@app.route("/cpf")
def gerar_cpf():
    cpf = CPF ()
    cpf_retorno = cpf.generate((True))
    return render_template("cpf.html", cpf = cpf_retorno)


# /cnpj (devolver um cnpj aleatório)
@app.route("/cnpj")
def gerar_cnpj():
    cnpj = CNPJ ()
    cnpj_retorno = cnpj.generate((True))
    return render_template("cnpj.html", cnpj = cnpj_retorno)



# /servicos (devolver um titulo com "Nossos serviços")
@app.route("/servicos")
def servicos():
    servicos_retorno = "<h1> Nossos serviços </h1>"
    return servicos_retorno

@app.route("/politicas")
def politicas_privacidade():
    return render_template("politicas.html")

@app.route("/termos")
def termos_de_uso():
    return render_template("termos.html")

@app.route("/utilizar")
def como_utilizar():
    return render_template("utilizar.html")

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos/cadastro", methods=['POST'])
def salvar_produtos():
    nome = request.form  ['nome']#dicionario imnutavel
    descricao = request.form  ['descricao']
    produto = { "nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos) 
