from flask import Flask, request
from markupsafe import Markup, escape
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print(escape('<script>alert(document.cookie);</script>'))
    return Markup('<strong>Hello</strong>')


@app.route('/hello', methods=['GET'])
def say_hello():
    template = Markup("<h1>Hello <i>%s</i></h1>")
    if 'name' in request.args:
        return template % request.args['name']
    else:
        return template % '"World!!"'


if __name__ == '__main__':
    app.run()
