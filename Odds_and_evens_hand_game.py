import random as ran
class Error(Exception):
    pass
class  OddEventextError(Error):
   pass
class  OnetoSixError(Error):
   pass
def roundinput():
  while True:
      try:
        Round=int(input("User to enter the Round ".center(50))) 
        return Round 
      except ValueError:
        print("Please input integer only... ") 
def userchoiceinput():  
   while True:
    try:
      userchoice=int(input("User to enter the number 1 to 6 "))  
      if(userchoice>7 or userchoice<1):
       raise OnetoSixError
      return userchoice
    except ValueError:
      print("Please input integer only... ")   
    except OnetoSixError:
      print("Please input integer value 1 to 6 only... ")      
def choiceinput():
   while True:
    try:
      choice=input("User to enter the choice even or odd ") 
      if(choice!="even" and choice!="odd") :
         raise OddEventextError
      return choice   
    except OddEventextError:
      print("Please Enter even or odd only... ") 

whochoice_oddandeven_points={"User":["",0,0],"Computer":["",0,0]} 
listplayer=list(whochoice_oddandeven_points.keys())      
Round= roundinput()
choice= choiceinput()
RountCount=0

while RountCount<Round:
  whochoice_oddandeven_points["User"][2]= userchoiceinput()       
  number=[1,2,3,4,5,6]
  whochoice_oddandeven_points["Computer"][2]=ran.choice(number)
  points={'even':0,'odd':0}
  if(choice=='even'):
    whochoice_oddandeven_points["User"][0]='even'
    whochoice_oddandeven_points["Computer"][0]='odd'
  else:
    whochoice_oddandeven_points["User"][0]='odd'
    whochoice_oddandeven_points["Computer"][0]='even'    

  finaloutput=whochoice_oddandeven_points["User"][2]+whochoice_oddandeven_points["Computer"][2]
  if(finaloutput%2==0):
      if(whochoice_oddandeven_points["User"][0]=='even'):
       whochoice_oddandeven_points["User"][1]=whochoice_oddandeven_points["User"][1]+1
      else:
       whochoice_oddandeven_points["Computer"][1]=whochoice_oddandeven_points["Computer"][1]+1
  else:
    if(whochoice_oddandeven_points["User"][0]=='odd'):
       whochoice_oddandeven_points["User"][1]=whochoice_oddandeven_points["User"][1]+1
    else:
       whochoice_oddandeven_points["Computer"][1]=whochoice_oddandeven_points["Computer"][1]+1    
  RountCount+=1
  print(whochoice_oddandeven_points)
  print("|| {} {} ||".format(listplayer[0].center(10),listplayer[1].center(10)))
  print("choices")
  print("|| {} {}||".format(whochoice_oddandeven_points[listplayer[0]][0].center(10),whochoice_oddandeven_points[listplayer[1]][0]).center(10))
  print("choices number")
  print("|| {} {}||=>".format(whochoice_oddandeven_points[listplayer[0]][2],whochoice_oddandeven_points[listplayer[1]][2]),finaloutput)
  print("final points")
  print("|| {} {}||".format(whochoice_oddandeven_points[listplayer[0]][1],whochoice_oddandeven_points[listplayer[1]][1]))
print("final points")
print("|| {} {}||".format(whochoice_oddandeven_points[listplayer[0]][1],whochoice_oddandeven_points[listplayer[1]][1]))
