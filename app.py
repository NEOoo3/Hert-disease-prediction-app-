from flask import Flask, render_template, request

app = Flask(__name__)

history = []  # To store prediction history

@app.route('/')
def home():
    return render_template('index.html', history=history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        thalach = int(request.form['thalach'])

        # Dummy logic for prediction (replace with your model logic)
        if age > 50 and cp > 1 and thalach < 120:
            prediction = "High risk of heart disease."
        else:
            prediction = "Low risk of heart disease."

        # Add the prediction to history
        history.append(prediction)

        return render_template('index.html', prediction_text=prediction, history=history)
    except ValueError:
        return render_template('index.html', prediction_text="Invalid input. Please try again.", history=history)

if __name__ == "__main__":
    app.run(debug=True)
