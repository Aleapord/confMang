from flask import Flask, render_template, request,redirect
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@49.235.167.8/Conference'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SECRET_KEY"] = "12345678"
app.jinja_env.auto_reload = True
db = SQLAlchemy(app)


class LoginForm(Form):
    name = StringField('name')
    password = PasswordField('password')
    submit = SubmitField('登录')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(128),nullable=False)
    inf = db.Column(db.String(1024))


class Conf(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), primary_key=True, nullable=False)
    detail = db.Column(db.String(1024), nullable=True)
    compere_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    compere = db.relationship('User', backref='conf')

    def __repr__(self):
        return '<Conf:(%s,%s)>' % (self.name, self.detail)


user1 = User(name='曾庶强', inf='dadadasfsfgfsf',password='123456')
user2 = User(name='叶琴',inf='啊书法大赛分隔符',password='123456')
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()
        if user:
            return redirect('http://www.baidu.com')
        else:
            flash('用户名不存在')

    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
