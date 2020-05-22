import os

num = [1]
den = [1, 2, 3, 4]
plot_name = "linuxtest.png"


if os.name == "nt":  # if is Windows
    print("Detected OS: Windows")
    command = "matlab -nodesktop -r \"testowa("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+plot_name+"\');exit;\""

elif os.name == "posix":  # if is Linux
    print("Detected OS: Linux")
    command = "/usr/local/MATLAB/R2018a/bin/matlab -softwareopengl -nodesktop -r \"testowa("+str(
        repr(num))+","+str(repr(den))+"," + "\'"+plot_name+"\');exit;\""
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit

print("Command/s to be run: \n"+command)
os.system(command)
