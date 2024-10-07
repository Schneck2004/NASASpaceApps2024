import pandas as pd
import csv
from tkinter import filedialog as fd


c = True

line = 0

while c:
    filename = fd.askopenfilename(title='Select a csv file', initialdir='C:/Users/guilh/Downloads/')
    filename.replace("", '')
    print(filename)

    time1 = float(input("Type the initial relative time of the quake: "))
    time2 = float(input("Type the final relative time of the quake: "))
    
    csv_input = pd.read_csv(filename)
    
    with open(filename, 'r') as f:
        my_data = csv.reader(f)
            
        for row in my_data:
            if row[1] != 'time_rel(sec)' and float(row[1]) >= time1 and float(row[1]) <= time2:
                line = my_data.line_num
                csv_input.loc[line, 'type'] = '1'
                
                
    
    csv_input.to_csv(filename, index=False)
    
    a = input("Continue? (Y/n): ").lower()
    if a != "y":
        c = False
