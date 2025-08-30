from flask import Flask

app = Flask(__name__)


@app.route('/')
def hellow():
    return '<h1 style="color: red">Привіт, світе! Я працюю з Flask та Docker!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
