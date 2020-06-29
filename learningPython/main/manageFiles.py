import os

def readFileContent(filename):
    try:
        f = open(filename,"r")
        content = f.read()
    finally:
        f.close()
    return content
    
def appendFileContent(filename, content):
    try:
        f = open(filename,"a")
        f.write("\n" + content)
    finally:
        f.close()
    return

def writeFile(filename, content):
    try:
        f = open(filename,"w+")
        f.write(content)
    finally:
        f.close()
    return

def createFile(filename):
    try:
        f = open(filename,"w+")
    finally:
        f.close()
    return 

def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print "The file", filename, "does not exist"