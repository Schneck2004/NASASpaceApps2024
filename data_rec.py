import pandas as pd
import csv
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import filedialog as fd

# Read the CSV file
filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

filepath = fd.askdirectory(title='Select the output folder', initialdir='C:/Users/guilh/Downloads/')
filepath.replace("", '')

# Read the CSV data into a DataFrame
df = pd.read_csv(filename)

# Split the dataset into training and testing sets
X_test = df.drop(['time_abs(%Y-%m-%dT%H:%M:%S.%f)', 'time_rel(sec)'], axis=1)

svm_model: SVC = joblib.load('trained.z')

# Predict the class for the testing set
y_pred = svm_model.predict(X_test)

# Export data to a new file
new_file = f'{filepath}/{(filename.split("/")[len(filename.split("/"))-1]).replace(".csv", "")}_quake_data.csv'

df.to_csv(new_file, index=False)

quake_data = pd.read_csv(new_file)

quake_data.to_csv(new_file, index=False)

with open(new_file, 'w+') as f:
    my_data = csv.reader(f)
    writer = csv.writer(f, delimiter='\n')
        
    for row in my_data:
        if row[1] != 'time_rel(sec)':
            line = my_data.line_num
            if y_pred[line-1] == 0:
                writer.writerow(row)
        else:
            writer.writerow(row)

quake_data.to_csv(new_file, index=False)