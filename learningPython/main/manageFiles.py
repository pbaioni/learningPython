import os

def readFileContent(filename):
    f = open(filename,"r")
    content = f.read()
    f.close()
    return content
    
def appendFileContent(filename, content):
    f = open(filename,"a")
    f.write("\n" + content)
    f.close()
    return

def writeFile(filename, content):
    f = open(filename,"w+")
    f.write(content)
    f.close()
    return

def createFile(filename):
    f = open(filename,"w+")
    f.close()
    return 

def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print "The file", filename, "does not exist"