from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World!'

@app.route('/name')
def hello():
	return "Lin Guodan"

@app.route('/')
def index():
	return 'Index Page'

@app.route('/user/<username>')
def show(username):
	return 'User %s' % username

if __name__ == '__main__':
	app.run(debug=True)