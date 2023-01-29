from flask import Flask , render_template, request
app = Flask(__name__)

varstr = "Anupam"
varlst = [10, 12, 13, 1, 4, 1, 2, 44]
vardict = {'K1': 'val1', 'K2': 'val2'}

@app.route('/')
def index():
    return render_template('homepage.html', vst=varstr, vlst= varlst, vdict= vardict )

@app.route('/business/')
def business():
    return render_template('business.html', vst=varstr, vlst= varlst, vdict= vardict )

@app.route('/info/')
def info():
    return '<h1> This is info page </h1>'

@app.route('/signup/')
def signup_fn():
    return render_template('signup.html')

@app.route('/thankyou/')
def thankyou_fn():
    first =request.args.get('first')
    last = request.args.get('last')
    return  render_template('thankyou.html', first=first, last=last)


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
