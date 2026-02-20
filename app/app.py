import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

import os

# Load Model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/model.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Extract features from form
        features = [
            float(request.form['relationships']),
            float(request.form['funding_rounds']),
            float(request.form['funding_total_usd']),
            float(request.form['milestones']),
            float(request.form['avg_participants']),
            float(request.form['age_first_funding_year']),
            float(request.form['age_last_funding_year']),
            float(request.form['age_first_milestone_year']),
            float(request.form['age_last_milestone_year'])
        ]
        
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        output = 'Acquired (Success)' if prediction[0] == 1 else 'Closed (Failure)'
        
        return render_template('result.html', prediction_text=f'Startup Outcome Prediction: {output}')
        
    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
