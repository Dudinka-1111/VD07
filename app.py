from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сохранить изменения')

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь вы можете обработать изменения профиля, например, сохранить их в базе данных.
        flash('Ваш профиль был обновлен!', 'success')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)