from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin_page():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == "admin" and request.form['password'] == "123456":
        return redirect("/")
    else:
        return render_template('signin.html')


@app.route('/list')
def _list():
    return render_template('list.html')


@app.route('/setting')
def setting():
    return render_template('setting.html')

if __name__ == '__main__':
    app.run()
