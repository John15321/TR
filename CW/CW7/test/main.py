import os

num = [1]
den = [1, 2, 3, 4]
plot_name = "linuxtest.png"


if os.name == "nt":
    print("Detected OS: Windows")
    command = "matlab -nodesktop -r \"testowa("+str(repr(num))+","+str(
        repr(den))+"," + "\'"+plot_name+"\');exit;\""
    print("Command/s to be run: \n"+command)
    os.system(command)
elif os.name == "posix":
    print("Detected OS: Linux")
    #  -nodesktop -r "testowa([1],[1, 2, 3, 4],'JEBAC_POLICJE.png');exit;"
    command = "/usr/local/MATLAB/R2018a/bin/matlab -softwareopengl -nodesktop -r \"testowa("+str(
        repr(num))+","+str(repr(den))+"," + "\'"+plot_name+"\');exit;\""
    print("Command/s to be run: \n"+command)
    os.system(command)
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit
