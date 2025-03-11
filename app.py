from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Пример данных пользователя
user_data = {
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "password": "password123"  # Никогда не храните пароли в открытом виде
}

@app.route('/', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Получение данных из формы
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        new_password = request.form.get('password')

        # Обновление данных пользователя
        user_data['name'] = new_name
        user_data['email'] = new_email
        user_data['password'] = new_password  # Не забудьте про хеширование в реальном приложении

        return redirect(url_for('profile'))

    return render_template('edit_profile.html', user=user_data)

@app.route('/profile')
def profile():
    return render_template('profile.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)