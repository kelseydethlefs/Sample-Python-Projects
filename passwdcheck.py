"""
  Password Checker.  Assignment 1, CIS 210

  Checks passwords for length, uppercase letters, lowercase letters, and digits.
  """

#get password from command line
import sys
if (len(sys.argv) > 1) :
    passwd = sys.argv[1]
else:
    print("Usage: python3 passwdcheck.py 9999")
    exit(1)  ## Quit the program right here, indicating a problem

#set booleans to False
isUpper = False
isLower = False
hasDigits = False

#is password > 6 characters?
if (len(passwd) < 5):
    print ("Password must be at least 6 characters long")

#running check on password
for char in passwd:
    #check if password has a lowercase letter in it
    if (char.islower()):
        isLower = True
    #does password have an uppercase letter in it?
    elif (char.isupper()):
        isUpper = True
    #does password have a digit in it?
    elif (char.isdigit()):
        hasDigits = True
    

#Bring up flags if booleans are still false.
if (isLower == False):
    print ("Password must include lower case letters")
if (isUpper == False):
    print ("Password must include upper case letters")
if (hasDigits == False):
    print ("Password must include digits")

#If nothing is flagged, give praise to user.
if (isLower == True and isUpper == True and hasDigits == True and len(passwd) > 5):
    print ("Good password")
