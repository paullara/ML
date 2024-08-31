from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('diabetes_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('diabetes.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form
    input_features = [float(x) for x in request.form.values()]
    prediction = model.predict([input_features])
    
    if prediction[0] == 1:
        output = 'Positive'
        health_tips = "It's important to consult with a healthcare provider for a detailed management plan. Regular monitoring of your blood sugar level, maintaining a healthy diet, and regular physical activity are crucial"
    else:
        output = 'Negative'
        health_tips = "Great News! Continue to maintain a healthy lifestyle by eating balanced meals, exercising regularly, and maintain your health regularly to prevent diabetes"
    return render_template('diabetes.html', prediction_text=f'Diabetes Prediction: {output}', health_tips=health_tips)

if __name__ == '__main__':
    app.run(debug=True)
