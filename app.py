from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError, NoResultFound
from settings import url, db
from models import User

app = Flask(__name__)
cors = CORS(app)
app.secret_key = b'ede658e5f53b85f2c4dbac1588c6328efab1d8a28160c6a9c15645a71577cb14'
app.config['SQLALCHEMY_DATABASE_URI'] = url
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template('hello.html', name=session['username'])
    return render_template('hello.html')


@app.route("/login/",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', msg="GET")
    elif request.method == "POST":
        print(request.form)
        if request.form.get("username") and request.form.get("password"):
            username = request.form.get("username")
            password = request.form.get("password")
            try:
                user = db.session.execute(db.select(User).filter_by(username=username, password=password)).scalar_one()
                if user is not None:
                    session['username'] = user.username
                    return render_template('hello.html', name=user.name, success='Usuário logado!')
                else:
                    return render_template('cadastro/cadastro.html', error='Usuário não existe! Faça o cadastro!')
            except NoResultFound:
                print('No result found')
                return render_template('cadastro/cadastro.html', fields=['nome', 'username', 'e-mail', 'senha'], error='Usuário não existe!')
            except Exception as e:
                print(e)
                return render_template('cadastro/cadastro.html', fields=['nome', 'username', 'e-mail', 'senha'], error='Usuário não existe!')
        return render_template('login.html', error='Os campos não podem ser vazios!')

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    fields = ['nome', 'username', 'email', 'password', ]
    if request.method == "GET":
        return render_template('cadastro/cadastro.html', fields=fields)
    elif request.method == "POST":
        name = request.form.get("nome")
        password = request.form.get("password")
        email = request.form.get("email")
        username = request.form.get("username")
        if name and password and email and username:
            try:
                user = User(name=name,password=password, email=email, username=username)
                db.session.add(user)
                db.session.commit()
                return render_template('login.html', success='Usuário cadastrado com sucesso!')
            except IntegrityError as ie:
                print(ie)
                return render_template('cadastro/cadastro.html', fields=fields, error='Usuário já cadastrado!')
            except Exception as e:
                print(e)
                return render_template('cadastro/cadastro.html', fields=fields, error='Usuário não foi cadastrado!' )
        return render_template('cadastro/cadastro.html', fields=fields, error='Os campos não podem ser vazios!')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return render_template('hello.html', success='Usuário deslogado!')