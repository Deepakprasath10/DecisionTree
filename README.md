# Student Course Prediction Web App

A Flask-based machine learning web application that predicts the most suitable academic course for a student based on their academic background and preferences. The prediction is made using a trained **Decision Tree Classifier**.

---

##  Overview

Many students face challenges when choosing the right course for higher education. This app helps recommend the most appropriate course based on key features like academic scores, interests, and stream.

---

##  Features

-  Predicts the ideal course for a student
-  Trained using a Decision Tree Classifier
-  Simple CSV-based dataset input
-  Easy-to-use web form for user input
-  Clean, responsive frontend using HTML & CSS
-  Real-time predictions powered by Flask

---

##  Tech Stack

- Python 3.10+
- Flask
- scikit-learn
- Pandas
- HTML/CSS

---

##  Project Structure
```
student-course-predictor/
│
├── static/
│ └── style.css # Custom frontend styling
│
├── templates/
│ ├── index.html # Input form UI
│ └── result.html # Prediction result
│
├── dataset.csv # Student data for training
├── model_train.py # Model training and export
├── decision_tree_model.pkl # Saved model
├── app.py # Flask application
└── README.md # Project documentation
```
---

##  Installation

 1. Clone the Repository

```
git clone https://github.com/yourusername/student-course-predictor.git
cd student-course-predictor
```

2. Install Requirements
```
pip install -r requirements.txt

```
3. Train the Model
Train your Decision Tree model using the dataset:
```
python model_train.py
```
This will generate the file decision_tree_model.pkl.

4. Run the App
Start the Flask server:
```
python app.py
```
Visit the application in your browser:
http://127.0.0.1:5000/


## Use Cases
College counseling systems

Career guidance platforms

EdTech recommendation systems

Automated admission portals

## Screenshots
![alt text](<Screenshot 2025-08-02 104800.png>)
![alt text](<Screenshot 2025-08-02 104821.png>)
![alt text](<Screenshot 2025-08-02 104830.png>)