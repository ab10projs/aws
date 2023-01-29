from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField ("what breed .. This is label")
    Submit = SubmitField('button for submit-- This is label')

@app.route('/',methods=['GET','POST'])
def index():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data =''
    return render_template('index.html',form=form,breed=breed)


if __name__ =='__main__':
    app.run(debug=True)