import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
	"Tittle":"Dbms",
	"author":"pavi",
	"year":2008
},

{
	"Tittle":"Sql",
	"author":"suresh",
	"year":2012
},

{

	"Tittle":"Mongodb",
	"author":"chenchu",
	"year":2014
	
},

{
	"Tittle":"Mysql",
	"author":"chenchuramu",
	"year":2015
},

{
	"Tittle":"Oracle",
	"author":"divya",
	"year":2016
},

{
	"Tittle":"Dbms",
	"author":"kaviya",
	"year":2010
}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>flask api Reading Archive</h1><p>This site is a prototype API for flask reading of books.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()


--- To run browser ---
--- http://127.0.0.1:5000/api/v1/resources/books/all ----