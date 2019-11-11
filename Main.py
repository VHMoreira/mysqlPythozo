from flask import render_template, request, Flask, redirect
from Jogo import Jogo
import Database
import os

app = Flask(__name__)
upload_folder = 'static/upload'
jogos = []

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    return render_template('Cadastro.html')

@app.route('/cadastrar',methods=['POST'])
def cadastrar():
    img = request.files['img']
    name = request.form['name']
    nota = request.form['nota']
    src = os.path.join(upload_folder,img.filename)
    infoText = request.form['infoText']

    img.save(os.path.join(upload_folder,img.filename))


    jogo = Jogo(name,int(nota),src,infoText)
    jogos.append(jogo)
    return redirect('/home')

@app.route('/home',methods=['GET'])
def index():
    return render_template('Home.html',lista=jogos)

app.run(port=8080,debug=True)