import os

def getScriptDirPath():
    return os.path.dirname(os.path.realpath(__file__))

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
