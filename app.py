from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    nome_DEV = "Felipe Patricio Silva"
    RA_DEV = "2202618"
    return (f'Meu nome é: {nome_DEV} e meu Ra é : {RA_DEV}')   