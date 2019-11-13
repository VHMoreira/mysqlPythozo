from flask import render_template, request, Flask, redirect
from Jogo import Jogo
from datetime import datetime
#import Database
import os

app = Flask(__name__)
upload_folder = 'static/upload'
jogos = []
val = {'access':False}

@app.route('/admin/cadastro', methods=['POST','GET'])
def cadastro():
    if val['access'] == True:
        return render_template('Cadastro.html')
    else:
        return redirect('/home')

@app.route('/admin')
def login():
    return render_template('Login.html')

@app.route('/admin/validation',methods=['POST'])
def validation():
    userLogin = request.form['login']
    password = str(request.form['password'])
    print(userLogin, password)
    if userLogin == 'admin' and password == '12345678':
        val['access'] = True
        return redirect('/admin/cadastro')
    else:
        return redirect('/home')


@app.route('/admin/cadastrar',methods=['POST'])
def cadastrar():
    img = request.files['img']
    name = request.form['name']
    nota = request.form['nota']
    src = os.path.join(upload_folder,img.filename)
    infoText = request.form['infoText']
    index = datetime.now()

    img.save(os.path.join(upload_folder,img.filename))


    jogo = Jogo(index,name,int(nota),src,infoText)
    jogos.append(jogo)
    return redirect('/home')

@app.route('/home',methods=['GET'])
def index():
    return render_template('Home.html',lista=jogos)

app.run(port=8080,debug=True)