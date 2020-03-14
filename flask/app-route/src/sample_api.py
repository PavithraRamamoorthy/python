from flask import Flask

app = Flask(__name__)


@app.route('/api/v1')
def view_message():
	return {"message": "This is flask !"}

@app.route('/api/v1/version')
def api_version():
    return {"version": "1.0.0"}