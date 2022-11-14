import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import attrition

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "data"

@app.route('/')
def render():
   return render_template('index.html')

@app.route('/upload',  methods = ['POST'])
def upload_file():
    if request.method == 'POST': 
        f = request.files['file']
        print(secure_filename("./data/" + f.filename))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        output_filepath = filepath.split(".csv")[0] + "_prediction.csv"
        f.save(filepath)
        attrition.predict_attrition(filepath, output_filepath)
        data = pd.read_csv(output_filepath)
        return render_template('table.html', tables=[data.to_html()], titles=[''])

@app.route('/eda')
def display():
   return render_template('eda.html')

if __name__ == '__main__':
   app.run(debug = True)