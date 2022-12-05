import random as ran
class Error(Exception):
    """Base class for other exceptions"""
    pass
class  OddEventextError(Error):
   pass
class  OnetoSixError(Error):
   pass
while True:
    try:
      Round=int(input("User to enter the Round ")) 
      break  
    except ValueError:
      print("Please input integer only... ") 
while True:
    try:
      userchoice=int(input("User to enter the number 1 to 6 "))  
      if(userchoice>7 and userchoice<1):
       raise OnetoSixError
      break  
    except ValueError:
      print("Please input integer only... ")   
    except OnetoSixError:
      print("Please input integer value 1 to 6 only... ")      
while True:
    try:
      choice=input("User to enter the choice even or odd ") 
      if(choice!="even" or choice!="odd") :
         raise OddEventextError
      break   
    except OddEventextError:
      print("Please Enter even or odd only... ")         

number=[1,2,3,4,5,6]
computerchoice=ran.choice(number)
  
finaloutput=computerchoice+userchoice
if(finaloutput%2==0):
    pass
else:
    pass