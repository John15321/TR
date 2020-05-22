import os

num = [1]
den = [1, 2, 3, 4]
plot_name = "JEBAC_POLICJE.png"


if os.name == "nt":
    print("Detected OS: Windows")
    command = "matlab -nodesktop -r \"testowa("+str(repr(num))+","+str(repr(den))+","+ "\'"+plot_name+"\');exit;\""
    os.system(command)
    print("Command/s to be run: \n"+command)
elif os.name == "posix":
    print("Detected OS: Linux")
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit
