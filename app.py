from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'IOS Backup Services'

if __name__ == '__main__':
    app.run()
