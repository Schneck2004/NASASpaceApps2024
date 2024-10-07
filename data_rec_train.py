import pandas as pd
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import filedialog as fd
import data_process as dp

# Read the CSV file
filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

# Read the CSV data into a DataFrame
df = pd.read_csv(filename)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop(['type', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)', 'time_rel(sec)'], axis=1), df['type'], test_size=0.2, random_state=42)

# Train a Support Vector Machine (SVM) model
svm_model = SVC(verbose=True, max_iter=1000, probability=True)
svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

joblib.dump(svm_model, 'trained.z', 3)