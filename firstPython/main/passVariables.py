#this allows to access the global variables
import globalVariables
#this allows to access the namespace of the calling script
import __init__

print 'the script has access to calling script\'s variable:', __init__.variableToPass

print 'the script has access to global variable 1:', globalVariables.global1

print 'the script has access to global list:', globalVariables.globalList
