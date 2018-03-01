from flask import Flask, url_for, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
	print(url_for('static', filename='/'))
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")
	
if __name__ == "__main__":
	list_files("..")
	app.run(debug=True)