import pandas as pd
import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import filedialog as fd
# Read the CSV file
filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

# Read the CSV data into a DataFrame
df = pd.read_csv(filename)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop(['type', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)', 'time_rel(sec)'], axis=1), df['type'], train_size=0.9999999999, random_state=45)

clf = MLPClassifier(random_state=45, max_iter=1000, verbose=True, shuffle=True, learning_rate='adaptive', solver='sgd', learning_rate_init=5.0).fit(X_train, y_train)

data = []

for j in df['velocity(m/s)']:
    data.append(j)

for k in range(data):
    results = clf.predict([data[k], data[k]])