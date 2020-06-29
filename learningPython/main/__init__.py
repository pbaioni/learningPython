import os
import logging
from askInput import *
from manageFiles import readFileContent, writeFile, appendFileContent, deleteFile
import  searchFiles
import globalVariables
import CustomException

#creating log folder if it doesn't exist
if not os.path.isdir(globalVariables.logFolder):
    os.mkdir(globalVariables.logFolder)
#setting root logerg configuration
logging.basicConfig(level=logging.INFO,format=globalVariables.logFormatter)

#testing functions defined in personal scripts
#change the False condition to activate a specific section

if False :
    #testing file functions
    content = readFileContent('inputs/data.txt')
    writeFile('outputs/created.txt', content)
    appendFileContent('outputs/created.txt', 'New line appended')
    deleteFile('fileToDelete.txt')

if False :
    #reading string lines
    for line in content.splitlines():
        print 'line:', line

if False :
    #testing user interaction functions
    floatNumber = askForFloat('enter a decimal:')
    print 'I received ', floatNumber
    
    intNumber = askForInt('enter an integer:')
    print 'I received ', intNumber
    
    stringInput = askForString('enter your name:')
    print 'I received ', stringInput

if False:
    #testing loops and execfile call
    execfile('loops.py')
    
if False:
    #testing lists
    execfile('lists.py')
    
if False:
    #testing arguments and os.system call
    #IMPORTANT: do NOT import the script if you use os.system to execute it
    os.system('python manageArguments.py 7 5')
    
if False:
    #testing passing variables between scripts
    variableToPass = 10
    #testing script execution using 'import'
    import passVariables
    
if False:
    #testing colors
    import manageColors
    
if False:
    #testing dates
    import manageDates
    
if False:
    #testing file search by pattern
    searchFiles.searchFiles('/Users/paolobaioni/Documents/Music/Italiana/883/', '*.mp3')
    
if False:
    #testing email sending
    import sendEmail
    
if False:
    #testing periodic action
    import periodicTask
    
if False:
    #testing logging
    import logToFile
    import logToConsole
    
if False:
    #testing exceptions
    
    #this can raise local exception
    import manageExceptions
    
    #this raises an exception to be caught here
    try:
        manageExceptions.raiseCustomException()
    except CustomException as ce:
        print('Custom Exception caught in calling script:')
        print(ce)
        
if False:
    #testing concurrent threads
    import manageThreads
        