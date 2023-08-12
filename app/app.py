from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Создание cookie с данными пользователя
        response = make_response(redirect(url_for('greeting')))
        response.set_cookie('userData', f'{{"name": "{name}", "email": "{email}"}}')
        return response

    return redirect(url_for('index'))

@app.route('/greeting')
def greeting():
    user_cookie = request.cookies.get('userData')
    if user_cookie:
        print(user_cookie)
        user_data = eval(user_cookie)
        return render_template('welcome.html', user_data=user_data)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('userData')
    return response

if __name__ == '__main__':
    app.run(debug=True)
