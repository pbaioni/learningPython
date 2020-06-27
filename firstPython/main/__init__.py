from askInput import *
from manageFiles import readFileContent, writeFile, appendFileContent, deleteFile
import os
import  searchFiles

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
    #testing loops
    execfile('loops.py')
    
if False:
    #testing lists
    execfile('lists.py')
    
if False:
    #testing arguments
    #IMPORTANT: do NOT import the script if you use os.system to execute it
    os.system('python manageArguments.py 7 5')
    
if False:
    #testing passing variables between scripts
    variableToPass = 10
    #this executes the passVariables script
    import passVariables
    
if False:
    #testing colors
    import manageColors
    
if False:
    #testing colors
    import manageDates
    
if False:
    #testing file search
    searchFiles.searchFiles('/Users/paolobaioni/Documents/Music/Italiana/883/', '*.mp3')
    
if False:
    #testing email sending
    import sendEmail

