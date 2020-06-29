import os
import logging
import time
import globalVariables

#the main logging settings have been done in the __init__script, as it should be
logger = logging.getLogger('logToFile')

#creating log folder if it doesn't exist
if not os.path.isdir(globalVariables.logFolder):
    os.mkdir(globalVariables.logFolder)

#adding an handler that enables the logger to log into a file
#this handler is local, it doesn't have an impact on loggers in other scripts
fileHandler = logging.FileHandler("./log/activity.log")
fileHandler.setFormatter(logging.Formatter(globalVariables.logFormatter))
logger.addHandler(fileHandler)

#using the logger. This logger will log in the console as specified in the __init__ script AND in the ./log/activity.log file
logger.info('Waiting 3 seconds')
time.sleep(3)
logger.info('Done')