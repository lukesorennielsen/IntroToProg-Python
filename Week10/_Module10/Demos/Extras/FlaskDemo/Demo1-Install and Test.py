# Install Flask then import its code like this
from flask import Flask

# Next we create a Flask object to work with.
app = Flask(__name__)

# The website will use http routes to process content.
# This example maps the "root" of the website (/) to the function index()
@app.route('/')
def index():
    data_str = 'test data'
    return data_str

# Finally we launch the website using the run() method
if __name__ == '__main__':
    app.run(debug=True)