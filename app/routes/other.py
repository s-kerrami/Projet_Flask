from flask import render_template
from app import app

@app.route('/')
def index():
    test = "Ma valeur test"
    return render_template('index.html', test = test)

@app.route('/demo/jinja')
def demoJinja():
    return render_template('demo-jinja.html')