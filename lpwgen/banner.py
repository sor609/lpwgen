# variable length banner
import sys
from __builtin__ import len
from flask import Flask, flash, render_template, redirect, url_for

# flask form stuff
app = Flask(__name__)
app.config.from_object('config')

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyInput(FlaskForm):
	banner = StringField('banner', validators=[DataRequired()])
 
@app.route('/', methods=('GET', 'POST'))
def submit():
	form = MyInput()
	if form.validate_on_submit():
		numch = len(form.banner.data) + 4
		flash('-' * numch)
		flash('| %s |' % form.banner.data)
		flash('-' * numch)
		return redirect(url_for('submit'))
	return render_template('form.html', title='Banner text', form=form)

if __name__ == '__main__':
    app.run()
