from flask import Flask

app = Flask(__name__)

@app.route('/healthz', methods=["GET"])
def healthz():
	return 'OK'

if __name__ == '__main__':
	app.run(debug=True, port=9631)
