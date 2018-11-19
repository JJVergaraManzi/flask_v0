#Login to user dashboard

#import libraries
from flask import render_template, Flask, redirect, , url_for
from flask_bootstrap import flask_bootstrap #import libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

#init the app
app = Flask(__name__)
app.config['SECRET KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE']
Bootstrap(app)

#Form class
class loginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(), Length(min=4, max= 15)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max(20))])
    remember = BooleanField('Recuerda me')

#define routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) #include methods client - server
def login():
    form = loginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))
        return '<h1> Usuario o contraseña inválido </h1>'
    return render_template('login.html', form = form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


#port assignament
if __name__=='__main__':
    app.run(debug = True, port = 5000)
