import os

def readInts(filename):

    cwd = os.path.dirname(os.path.abspath(__file__))
    path = "{0}\{1}".format(cwd,filename)

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    intList = []

    for line in lines:
        intList.append(int(line))

    return intList