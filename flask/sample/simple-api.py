from flask import Flask

app = Flask(__name__)


@app.route('/api/v1')
def index_page():
	return {"message": "Welcome !"}

@app.route('/api/v1/version')
def api_employee_json():
    return {"version": "1.0.0"}
