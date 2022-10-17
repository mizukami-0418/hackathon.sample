from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = b'icecream2022'

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if request.form['user'] == '' or request.form['password'] == '':
            flash('ユーザー・パスワードを入力してください')
            flash('お願いします。')
        else:
            flash('ログインしました')
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()