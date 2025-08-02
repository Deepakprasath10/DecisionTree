import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle


df = pd.read_csv('student_course_data.csv')

X = df.drop('Recommended_Course', axis=1)
y = df['Recommended_Course']

le = LabelEncoder()
for col in X.columns:
    X[col] = le.fit_transform(X[col])

y = le.fit_transform(y)

model = DecisionTreeClassifier()
model.fit(X, y)

with open('decision_tree_model.pkl', 'wb') as f:
    pickle.dump(model, f)
