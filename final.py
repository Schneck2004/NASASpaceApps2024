'''

Project Made by: Caio Rivas, Guilherme Schneck, João Nasciment for the 2024 NASA Space Apps Chalenge
Created in 05/10/2024, last modified at 06/10/2024
'''
import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

file='./data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1970-03-25HR00_evid00003'
#Open the files 
csv_file=file+'.csv'
data_cat = pd.read_csv(csv_file)

try:
    csv_times = np.array(data_cat['time_rel(sec)'].tolist())
    Moon='yes'
except:
    csv_times = np.array(data_cat['rel_time(sec)'].tolist())
    Moon='no'
if Moon == 'yes':
    csv_times = np.array(data_cat['time_rel(sec)'].tolist())
    csv_data = np.array(data_cat['velocity(m/s)'].tolist())
    parts =[[] for _ in range(1,6)]
    parts_2 =[[] for _ in range(1,6)]
    csv_rows = data_cat.shape[0]
    part_div=csv_rows // 5
    lists = 0
    for i in range(csv_rows):
        times = csv_times[i]
        speed = csv_data[i]
        if i == part_div or i == part_div *2 or i == part_div * 3 or i == part_div * 4 :
            lists += 1
        parts[lists].append(times)
        parts_2[lists].append(speed)
else :
    csv_data = np.array(data_cat['velocity(c/s)'].tolist())
    parts =[[] for _ in range(1,6)]
    parts_2 =[[] for _ in range(1,6)]
    csv_rows = data_cat.shape[0]
    part_div=csv_rows // 5
    lists = 0
    for i in range(csv_rows):
        times = csv_times[i]
        speed = csv_data[i]
        if i == part_div or i == part_div *2 or i == part_div * 3 or i == part_div * 4 :
            lists += 1
        parts[lists].append(times)
        parts_2[lists].append(speed)
fig,one = plt.subplots(1,1,figsize=(15,3))
one.plot(parts[0], parts_2[0])
one.set_title('One')
plt.savefig('./AI_local_database/one.png')

fig,two = plt.subplots(1,1,figsize=(15,3))
two.plot(parts[1], parts_2[1])
two.set_title('Two')
plt.savefig('./AI_local_database/two.png')

fig,three = plt.subplots(1,1,figsize=(15,3))
three.plot(parts[2], parts_2[2])
three.set_title('Three')
plt.savefig('./AI_local_database/three.png')

fig,four = plt.subplots(1,1,figsize=(15,3))
four.plot(parts[3], parts_2[3])
four.set_title('Four')
plt.savefig('./AI_local_database/four.png')

fig,five = plt.subplots(1,1,figsize=(15,3))
five.plot(parts[4], parts_2[4])
five.set_title('Five')
plt.savefig('./AI_local_database/five.png')