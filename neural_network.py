import pandas as pd
import joblib
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import filedialog as fd
# Read the CSV file
filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

skip = 486900

# Read the CSV data into a DataFrame
df = pd.read_csv(filename)
df_train = pd.read_csv(filename, skiprows=skip, usecols=[2])
df_type = pd.read_csv(filename, skiprows=skip, usecols=[3])

y = []
z = []

with open(filename, 'r') as f:
        my_data = csv.reader(f)
            
        for row in my_data:
            if row[3] != 'type' and float(row[3]) == 0:
                line = my_data.line_num
                y.append(float(row[2]))
            elif row[3] != 'type' and float(row[3]) == 1:
                z.append(float(row[2]))

x = [y, z]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, [0, 1], test_size=0.2, random_state=1)

clf = MLPClassifier(random_state=1, max_iter=1000, verbose=True, shuffle=False, learning_rate='adaptive', solver='adam').fit(X_train, y_train)

results = clf.predict(X_test)
print(results)