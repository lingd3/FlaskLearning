from flask import Flask
app = Flask(__name__)

@app.route('/sum/<int:a>/<int:b>/')
def doSum(a,b):
	sum_ = a+b
	return str(sum_)

if __name__ == '__main__':
	app.run(debug=True)