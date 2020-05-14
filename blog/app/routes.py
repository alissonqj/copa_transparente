from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vinicius'}
    posts = [
        {
            'author': {'username': 'Vinicius'},
            'body': 'Ótimo dia em Florianópolis'
        },
        {
            'author': {'username': 'Jaiminho'},
            'body': 'Dia chuvoso em Tamgamandápio'
        }
    ]
    return render_template('index.html', title='Página Inicial', user=user, posts=posts)
