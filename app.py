from flask import Flask, render_template, request
import os.path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Access form data
        codes = request.form['codes']
        datafile = request.files['datafile']

        # Process the form data as needed (e.g., save the file, perform operations)
        # For example, saving the file:
        datafile.save('uploads/' + datafile.filename)
        codes.save('uploads/' + 'codes.txt')

        # You can now use the 'codes' and 'datafile' variables as needed in your backend logic.

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)