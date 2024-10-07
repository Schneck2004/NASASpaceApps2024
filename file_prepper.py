import pandas as pd
from tkinter import filedialog as fd

filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
filename.replace("", '')
print(filename)

csv_input = pd.read_csv(filename)
csv_input['type'] = '0'
csv_input.to_csv(filename, index=False)