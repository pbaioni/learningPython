import fnmatch
import os

def searchFiles(rootPath, pattern):
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
