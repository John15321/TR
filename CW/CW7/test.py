import subprocess
import os
matlab_path = "C:\\Program Files\\MATLAB\\R2018a\\bin\\matlab.exe"

matlab_function = "\"nyquist_plot_with_k("+str(repr([1]))+","+str(
    repr([1, 2, 3]))+"," + "\'"+"a"+"\');exit;\""

process = subprocess.Popen([matlab_path, " -nodesktop", " -r ", matlab_function ])
exitCode = process.wait()
print("Waiting for Matlab to finish:")
while not os.path.exists("end_of_mat.csv"):
    pass
print("FINISH")
