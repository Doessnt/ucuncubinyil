from flask import Flask

app = Flask(__name__)



@app.route('/merhaba/<name>')
def indexpage(name):
    return 'Django >> %s '% name

@app.route('/areyougay')
def bruh():
    return 'YOU ARE GAY'

if __name__ == '__main__':
    app.run()