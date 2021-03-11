from flask import Flask,render_template, url_for, flash, redirect,request, session
from flask_sqlalchemy import SQLAlchemy
from forms import Registerationform,Loginform
import pymysql
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cwr4tr 78f7gf7ff8gf86gf8fvf'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:Heya#123@localhost/Bucketlist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "try"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True,nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self,name,email,username,password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password


@app.route('/register')
def register():
    form  = Registerationform()
    return render_template('register.html',title='register', form=form)


@app.route('/login')
def login():
    form  = Loginform()
    return render_template('login.html',title='login', form=form)


@app.route('/')
def home():
    return render_template('home.html',title='home')


@app.route('/enterdata',methods=['GET','POST'])
def enterdb():
    form1 = Registerationform()
    if form1.validate_on_submit() and request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        record = User(name,email,username,password)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))


@app.route('/verification', methods=['GET','POST'])
def checkdb():
    form1 = Loginform()
    if form1.validate_on_submit() and request.method == 'POST':
        user = request.form['username']
        session['username'] = request.form['username']
        passwd = request.form['password']
        a = User.query.filter_by(username = user,password=passwd ).first()
        if a is not None:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))
























if __name__ == '__main__':
    app.run(debug=True)

