from math import sqrt
import CustomException

#catch exception locally
try:
    a = int(input("Enter a positive integer for square root: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
else:
    print 'The square root is:', sqrt(a)

def raiseCustomException():
    #this exception must be handled in the calling script in order to avoid crash
    raise CustomException("Message from custom exception: something went wrong")