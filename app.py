""""
Simple server
version 1.0
Author:
Bootstrap -- for site design

"""

from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>/')
def hello_to(name):
    return render_template('index.html', name=name)


users = ['Root', 'Boot', 'Foot']


@app.route('/all/')
def hello_all():
    return render_template('hello_all.html', users=users)


@app.route('/pic/')
def get_pic():
    return render_template('get_pic.html')


if __name__ == '__main__':
    app.run()
