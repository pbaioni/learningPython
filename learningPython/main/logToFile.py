import logging
import time

#the main logging settings have been done in the __init__script, as it should be
logger = logging.getLogger('logToFile')

#could'nt find a way to recover the formatter already specified in __init__, so we repeat it here
logFormatter = logging.Formatter('%(asctime)s (%(threadName)-10s) %(filename)s [%(levelname)s] %(message)s')

#adding an handler that enables the logger to log into a file
#this handler is local, it doesn't have an impact on loggers in other scripts
fileHandler = logging.FileHandler("./log/activity.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

#using the logger. This logger will log in the console as specified in the __init__ script AND in the ./log/activity.log file
logger.info('Waiting 3 seconds')
time.sleep(3)
logger.info('Done')