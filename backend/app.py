from flask import Flask

def app():
    app = Flask(__name__)
    pass

if __name__ == '__main__':
    app = app()
    app.run(host='0.0.0.0', port=5000)