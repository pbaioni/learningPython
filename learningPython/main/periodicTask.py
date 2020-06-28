import time, threading

period = 2

def printCurrentTime():
    print(time.ctime())
    threading.Timer(period, printCurrentTime).start()

printCurrentTime()
