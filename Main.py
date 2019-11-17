from flask import render_template, request, Flask, redirect
from Jogo import Jogo
from datetime import datetime
from Database import Database
import os


bd = Database()
# bd.criarTabela()

app = Flask(__name__)
upload_folder = 'static/upload'
val = {'access':False}

@app.route('/',methods=['GET'])
def index():
    jogos = bd.readTabela()
    return render_template('Home.html',lista=jogos)

@app.route('/admin/cadastro', methods=['POST','GET'])
def cadastro():
    if val['access'] == True:
        return render_template('Cadastro.html')
    else:
        return redirect('/')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/logout')
def logout():
    val['access'] = False
    return redirect('/')

@app.route('/admin',methods=['GET'])
def admin():
    if val['access'] == True:
        jogos = bd.readTabela()
        return render_template('Admin.html',lista=jogos)
    else:
        return redirect('/')

@app.route('/login/validation',methods=['POST'])
def validation():
    userLogin = request.form['login']
    password = str(request.form['password'])
    
    if userLogin == 'admin' and password == '12345678':
        val['access'] = True
        return redirect('/admin')
    else:
        return redirect('/')


@app.route('/admin/cadastrar',methods=['POST']) #passar para bd, esta funcionando
def cadastrar():
    table = []
    img = request.files['img']
    name = request.form['name']
    nota = request.form['nota']
    src = os.path.join(upload_folder,img.filename)
    infoText = request.form['infoText']
    now = datetime.now() # verificar se id nao repete
    print(now)
    index = now.second

    img.save(os.path.join(upload_folder,img.filename))

    table.append(name)
    table.append(nota)
    table.append(index)
    table.append(src)
    table.append(infoText)

    bd.insertInto(table) #insere no BD
    return redirect('/admin')


@app.route('/admin/delete',methods=['POST']) #passar para bd, nao esta funcionando
def delete():
    index = request.form['id']
    bd.remove(index)
    
    return redirect('/admin')

@app.route('/admin/update',methods=['POST']) #atualizar bd
def update():
    index = request.form['id']
    name = request.form['name']
    nota = request.form['nota']
    infoText = request.form['infoText']
    table =[name,nota,infoText]
    bd.update(table,index)
    
    return redirect('/admin')

app.run(port=8080,debug=True)