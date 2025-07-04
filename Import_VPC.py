### Import VPC BDT data set

import os
import numpy as np
import pandas as pd

working_dir = "Bimodal_detection_task_VPC"
sampling_rate = 30000

def import_data(path):
    Neurons = []
    Psychos = []

    os.chdir(os.path.join(working_dir, path))
    files = os.listdir('.')
    files.sort()
    
    for filename in files:
        if len(filename) > 3 and filename[7] == 'e':
            Neurons.append(np.genfromtxt(filename, delimiter=','))

        elif filename.startswith('p'):
            Psychos.append(pd.read_csv(filename, delimiter=","))
            

    # Psychometric indices (python)
    pi = np.genfromtxt("All_Psico.csv", delimiter=',', dtype=np.int16) - 1 
    
    return Neurons, Psychos, pi


## VPCr 32


N32r = 264 #number of neurons
P32r = 17 #number of psychometrics files
Neurons32r, Psychos32r, pi32r = import_data("All_Neurons_RR32_right")


# Allign and catch exceptions 

Psychos32r[0] = Psychos32r[0][:145]
err32r = []
for n in range(N32r):
    try:
        if pi32r[n] == 0:
            Neurons32r[n] = Neurons32r[n][:145, :]
        
        Neurons32r[n] = Neurons32r[n] / sampling_rate - np.expand_dims(Psychos32r[pi32r[n]]["o3"], 1)
    except:
        err32r.append(n)
        Neurons32r[n] = np.zeros((Psychos32r[pi32r[n]].shape[0],1))


## VPCl 32


N32l = 310
P32l = 20
Neurons32l, Psychos32l, pi32l = import_data("All_Neurons_RR32_left")

# Catch exceptions 

err32l = []
for n in range(N32l):
    if not Neurons32l[n].shape[0] == Psychos32l[pi32l[n]].shape[0]:
        err32l.append(n)
        Neurons32l[n] = np.zeros((Psychos32l[pi32l[n]].shape[0],1))
     
       
## VPCr 33

N33r = 345
P33r = 23
Neurons33r, Psychos33r, pi33r = import_data("All_Neurons_RR33_right")
# Fix exceptions 

err33r = []
for n in range(N33r):
    if n == 21 or n == 23:
        Neurons33r[n] = Neurons33r[n][:123, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[:123, :])
        pi33r[n] = P33r + 1    
    elif n == 99 or n == 100 or n == 101 or n == 102 or n == 109 or n == 110: 
        Neurons33r[n] = Neurons33r[n][60:150, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[60:150, :])
        pi33r[n] = P33r + 2
    elif n == 176: 
        Neurons33r[n] = Neurons33r[n][40:, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[40:, :])
        pi33r[n] = P33r + 3
    elif n == 121:
        Neurons33r[n] = Neurons33r[n][:75, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[:75, :])
        pi33r[n] = P33r + 4
    elif n == 149 or n == 150 or n == 151: 
        Neurons33r[n] = Neurons33r[n][:50, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[:50, :])
        pi33r[n] = P33r + 5
    elif n == 175: 
        Neurons33r[n] = Neurons33r[n][40:, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[40:, :])
        pi33r[n] = P33r + 6
    elif n == 229 or n == 230: 
        Neurons33r[n] = Neurons33r[n][70:, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[70:, :])
        pi33r[n] = P33r + 7
    elif n == 294: 
        Neurons33r[n] = Neurons33r[n][:130, :]
        Psychos33r.append(Psychos33r[pi33r[n]].iloc[:130, :])
        pi33r[n] = P33r + 8
    else:
        if not Neurons33r[n].shape[0] == Psychos33r[pi33r[n]].shape[0]:
            err33r.append(n)
            Neurons33r[n] = np.zeros((Psychos33r[pi33r[n]].shape[0],1))



