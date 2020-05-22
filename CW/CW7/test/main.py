import os
import numpy as np
import pandas as pd 
import matplotlib as plt

num = [1]
den = [1, 2, 3, 4]
plot_name = "WYKRES.png"

f= open("stabs.txt","w+")
f.close()

# dlmwrite('./stabs.txt',[1 2 3 4],'delimiter',',')
if os.name == "nt":  # if is Windows
    print("Detected OS: Windows")
    command_start = "matlab -nodesktop -r \"nyquist_plot_with_k("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"a.png"+"\');nyquist_plot_with_k("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"b.png"+"\');nyquist_plot("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"c.png"+"\');nyquist_plot("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"d.png"+"\');exit;\""

elif os.name == "posix":  # if is Linux
    print("Detected OS: Linux")
    command_start = "/usr/local/MATLAB/R2018a/bin/matlab -softwareopengl -nodesktop -r \"nyquist_plot_with_k("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"a.png"+"\');nyquist_plot_with_k("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"b.png"+"\');nyquist_plot("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"c.png"+"\');nyquist_plot("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+"d.png"+"\');exit;\""
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit

print("Command/s to be run: \n"+command_start)
os.system(command_start)


df = pd.read_csv("stabs.txt", header=None)
stabilities = df[0].to_list()
