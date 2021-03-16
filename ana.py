import csv    
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

arr_data = np.loadtxt('alpha1.csv', delimiter=",", dtype="float")
lens = len(arr_data)
data=arr_data.tolist()
print(lens)

i=0
j=0

with open('smooth_an.csv','w') as fout:
    for i in tqdm(range(lens)):
        for j in range(3071):
            if j == 0 | j == 3071:
                fout.write(str(data[i][j]))
            else :
                data[i][j] = (data[i][j-1]+2*data[i][j]+data[i][j+1])/4
                fout.write(str(data[i][j]))
                fout.write(',')
        fout.write('\n')

def t_max(data,k):
    t_max=0
    for j in range(3071):
        if data[k][j]>t_max:
            t_max=data[i][j]
    return t_max

def t_min(data,k):
    t_min=10000
    for j in range(3071):
        if data[k][j]<t_min:
            t_min=data[i][j]
    return t_min

with open('smooth_norm_an.csv','w') as fout1:
    for i in tqdm(range(lens)):
        tmax = t_max(data,i)
        tmin = t_min(data,i)
        for j in range(3071):
            data[i][j] = (data[i][j] - tmin)/(tmax - tmin)
            fout1.write(str(data[i][j]))
            fout1.write(',')
        fout1.write('\n')        

def raise_edge(data,k):
    idk = 0.15*(t_max(data,k)-t_min(data,k))
    sim =1.
    match = 0.
    for j in range(3071):
        if abs(data[k][j] - idk) < sim:
            sim = abs(data[k][j] - idk)
            match = j
    return match

with open('final_an.csv','w') as fout2:
    for i in tqdm(range(lens)):
        k = raise_edge(data,i)
        for j in range(k-20,k+105):
            fout2.write(str(data[i][j]))
            fout2.write(',')
        fout2.write('\n')             

