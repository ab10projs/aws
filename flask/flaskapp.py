from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> The First Page </h1>'

@app.route('/info/')
def info():
    return '<h1> This is info page </h1>'

@app.route('/info/<name>')
def info_name(name):
    if name[-1] == 'l':
        name = name[:-1]+'Y'
    if name[-1] == 'm':
        name = name[:-1] + 'YYY'
    return  '<h1>This is info for {}</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug= True)
    #app.run()  # for no debug
