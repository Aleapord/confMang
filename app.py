from flask import Flask, render_template,request
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@49.235.167.8/Conference'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
db = SQLAlchemy(app)

class LoginForm(Form):
    name = StringField('name',validators=DataRequired('不能为空'))
    password = PasswordField('password',validators=DataRequired('密码不能为空'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    inf = db.Column(db.String(1024))


class Conf(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), primary_key=True, nullable=False)
    detail = db.Column(db.String(1024), nullable=True)
    compere_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    compere = db.relationship('User',backref='conf')

    def __repr__(self):
        return '<Conf:(%s,%s)>' % (self.name, self.detail)


user1 = User(name='曾庶强', inf='dadadasfsfgfsf')
confq = Conf(name="fsfefwf", detail='fewqgfgregrgtggwrgewrgewg', compere_id=21)
confv = Conf(name='dsaddsafefregertg', detail='gegtrghrthrthrh', compere_id=8987)


def Cover2Json(conf: Conf = '', user: User = ''):
    if conf is not None:
        return {
            'id': conf.id,
            'name': conf.name,
            'detail': conf.detail,
            'compere_id': conf.compere_id
        }
    else:
        return {
            'id': user.id,
            'name': user.name,
            'inf': user.inf
        }


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    conf_list = [confq, confv]
    return render_template('index.html', conf_list=conf_list)


@app.route('/ss')
def getAll():
    return json.dumps(user1.Cover2Json())

@app.route('/login')
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template()



if __name__ == '__main__':
    app.run(debug=True)
