from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/error')
def error():
    return 'username or password is wrong!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'shiyanlou' and request.form['password'] == 'shiyanlou':
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return "Hello shiyanlou"
        else:
            return redirect(url_for('error'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

app.secret_key = 'wing1995 is a very good girl'

if __name__ == '__main__':
    app.run(debug=True)