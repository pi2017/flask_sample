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


@app.route('/<users>/')
def hello_all(users):
    return render_template('hello_all.html', users=users)


@app.route('/<pic>/')
def get_pic(pic):
    return render_template('get_pic.html', user_image=uav.jpg)


if __name__ == '__main__':
    app.run()
