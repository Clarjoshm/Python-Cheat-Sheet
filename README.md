# Python-Cheat-Sheet
Basic Python Inputs
=======================================================================================
Commands
---------------------------------------------------------------------------------------
Print                            //Shows words that are typed into console
=                                //Creates Variable
+                                //Allows user to combine two words or more commands
str()                            //Converts non-strings into strings
%                                //Combines the string with variables
len()                            //prints length of variable put inside the brackets
.upper()                         //Makes everything uppercase
.lower()                         //Makes everything lowercase 

COMPARATORS
Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)



========================================================================================
Descriptions
----------------------------------------------------------------------------------------
Variable                         //Can assign an object a name by using an equal sign
Concatenation                    //Used to combine strings together using a + sign
Strings                          //A string is a sequence of characters
Control flow                     //The ability to choose outcomes based on what else is happening in the program.

=========================================================================================
Examples
-----------------------------------------------------------------------------------------

DATE AND TIME

from datetime import datetime
now = datetime.now()

print '%02s/%02s/%04s' % (now.month, now.day, now.year) + ' %02s:%02s:%02s' % (now.hour, now.minute, now.second)

-------------------------------------------------------------------------------------------

ASK AND USER RESPOND

name = raw_input("What's your name?")
print name

original = raw_input("Enter a word:")
if len(original) > 0:
  print original
else:
  print "Enter a word"
  
