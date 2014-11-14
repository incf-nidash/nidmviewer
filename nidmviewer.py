__author__ = 'satra'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('index.html', 'rt') as fp:
        return ''.join(fp.readlines())

if __name__ == '__main__':
    app.run()