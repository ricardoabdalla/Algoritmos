import os

def readUfData(filename):

    cwd = os.path.dirname(os.path.abspath(__file__))
    path = "{0}\{1}".format(cwd,filename)

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def loadUfData(uf, data):
    n = int(data[0])
    print(n)
