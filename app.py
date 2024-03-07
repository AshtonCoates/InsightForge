from flask import Flask, render_template, request
import os
from processor import QueryProcessor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # access form data
        codes = request.form['codes']
        datafile = request.files['datafile']
        processor = QueryProcessor(codes, datafile)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)