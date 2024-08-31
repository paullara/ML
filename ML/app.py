from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

#load the model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    age = float(request.form['age'])

    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)

    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)
