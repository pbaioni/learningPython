import os
from askInput import *
import globalVariables
import logging
from manageFiles import readFileContent, writeFile, appendFileContent, deleteFile
import  searchFiles
import CustomException
from manageDatabase import *

#setting root logger configuration
logging.basicConfig(level=logging.INFO,format=globalVariables.logFormatter)

#******************************
#testing functions defined in personal scripts
#change the False condition to activate a specific section
#******************************

#testing loops and execfile call
if False:
    execfile('loops.py')

#testing lists
if False:
    execfile('lists.py')
    
#testing colors
if False:
    import manageColors

#testing dates
if False:
    import manageDates

#testing passing variables between scripts and shared global variables
if False:
    variableToPass = 10
    #script execution using 'import'
    import passVariables
    
#testing arguments and os.system call 
if False:
    #IMPORTANT: do NOT import the script if you use os.system to execute it 
    os.system('python manageArguments.py 7 5')

#testing user interaction functions
if False :
    floatNumber = askForFloat('enter a decimal:')
    print 'I received ', floatNumber
    
    intNumber = askForInt('enter an integer:')
    print 'I received ', intNumber
    
    stringInput = askForString('enter your name:')
    print 'I received ', stringInput
    
#testing logging 
if False:
    import logToFile
    import logToConsole
    
#testing exceptions
if False:   
    #this can raise local exception
    import manageExceptions
    
    #this raises an exception to be caught here
    try:
        manageExceptions.raiseCustomException()
    except CustomException as ce:
        print('Custom Exception caught in calling script:')
        print(ce)
    
#testing file functions
if False :
    content = readFileContent('inputs/data.txt')
    writeFile('outputs/created.txt', content)
    appendFileContent('outputs/created.txt', 'New line appended')
    deleteFile('fileToDelete.txt')
    
    #reading string line by line
    for line in content.splitlines():
        print 'line:', line
    
#testing file search by pattern
if False:
    searchFiles.searchFiles('/Users/paolobaioni/Documents/Music/Italiana/883/', '*.mp3')
    
#testing email sending
if False:
    import sendEmail

#testing periodic action
if False:
    import periodicTask
    
#testing threads management  
if False:
    import manageThreads
    
#testing database
if False:
    connect('mydatabase.db')
    createUserTable()
    insertUser('Paolo', 43)
    insertUser('Clemence', 37)
    results = executeCommand("""SELECT * FROM users""")
    for user in results:
        print user
    dropUserTable()
    disconnect()
    
        