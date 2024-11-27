# Install Flask then import its code like this
from flask import Flask
from flask import render_template

# Next we create a Flask object to work with.
app = Flask(__name__)

# The website will use http routes to process content.
# This example maps the "root" of the website (/) to the function index()
@app.route('/')
def index():
    return render_template('page-using-template.html')

# Finally we launch the website using the run() method
if __name__ == '__main__':
    app.run(debug=True)