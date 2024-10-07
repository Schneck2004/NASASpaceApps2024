import pandas as pd
from tkinter import filedialog as fd
from sklearn.preprocessing import OrdinalEncoder
import csv

# Read the CSV file
filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

# Read the CSV data into a DataFrame
df = pd.read_csv(filename)

x = []
y = []

with open(filename, 'r') as f:
    data = csv.reader(f)
    
    for row in data:
        if row[1] != 'time_rel(sec)':
            y.append(float(row[2]))
            y.append(int(row[3]))
            x.append(y)
            y = []
        
enc = OrdinalEncoder()

enc.fit(x)

print(enc.categories_[0])