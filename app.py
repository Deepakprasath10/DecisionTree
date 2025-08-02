from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


model = pickle.load(open('decision_tree_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        qualification = request.form['qualification']
        language = request.form['language']
        hours = int(request.form['hours'])
        interest = request.form['interest']

        qualification_map = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
        language_map = {'Python': 2, 'Java': 1, 'C++': 0, 'JavaScript': 3}
        interest_map = {'AI': 0, 'Web': 2, 'Data': 1}

        input_data = [
            age,
            qualification_map[qualification],
            language_map[language],
            hours,
            interest_map[interest]
        ]

        prediction = model.predict([input_data])[0]

        course_map = {
            0: "Big Data Analytics",
            1: "Data Analysis",
            2: "Deep Learning",
            3: "Frontend Web Dev",
            4: "Full Stack Development",
            5: "Machine Learning"
        }

        predicted_course = course_map.get(prediction, "Unknown Course")

        return render_template('index.html', prediction_text=f"Recommended Course: {predicted_course}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
