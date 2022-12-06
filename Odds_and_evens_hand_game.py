import random as ran
class Error(Exception):
    pass
class  OddEventextError(Error):
   pass
class  OnetoSixError(Error):
   pass
def roundinput():
  l="-"*50
  while True:
      try:
        print("\n||{}||".format(l.center(50)))
        Round=int(input("||{}||=>".format("User to enter the Round".center(50))))
        return Round 
      except ValueError:
        print("||{}||".format(".................".center(50)))
        print("||{}||".format("Please input integer only...".center(50)))
def userchoiceinput(): 
   l="-"*50 
   while True:
    try:
      print("||{}||".format(l.center(50)))
      userchoice=int(input("||{}||=>".format("User to enter the number".center(50))))  
      print("||{}||".format(l.center(50)))
      # if(userchoice>7 or userchoice<1):
      #  raise OnetoSixError
      return userchoice
    except ValueError:
      print("||{}||".format(".................".center(50)))
      print("||{}||".format("Please input integer only...".center(50)))     
    # except OnetoSixError:
    #   print("||{}||".format(".................".center(50)))
    #   print("||{}||".format("Please input integer value 1 to 6 only...".center(50)))     
def choiceinput():
   while True:
    l="-"*50 
    try:
      print("||{}||".format(l.center(50)))
      choice=input("||{}||=>".format("User to enter the choice even or odd".center(50)))
      if(choice!="even" and choice!="odd") :
         raise OddEventextError
      return choice   
    except OddEventextError:
      print("||{}||".format(".................".center(50)))
      print("||{}||".format("Please Enter even or odd only... ".center(50))) 
def gameinfo():
  l="="*60 
  print("\n||{}||".format(l.center(60)))
  print("||{}||".format("Odds and evens (hand game),".center(60)))
  print("||{}||".format(l.center(60)))

  print("||{}||".format(l.center(60)))
  print("||{}||".format("Odds and evens is a simple game of chance and hand game,".center(60)))
  print("||{}||".format("involving two people simultaneously revealing a number of".center(60)))
  print("||{}||".format("fingers and winning or losing depending on whether".center(60)))
  print("||{}||".format("they are odd or even".center(60)))
  print("||{}||".format(l.center(60)))

gameinfo()  
l="-"*50
whochoice_oddandeven_points={"User":["",0,0],"Computer":["",0,0]} 
listplayer=list(whochoice_oddandeven_points.keys())      
Round= roundinput()
choice= choiceinput()
RoundCount=0

while RoundCount<Round:
  whochoice_oddandeven_points["User"][2]= userchoiceinput()       
  number=[1,2,3,4,5,6]
  whochoice_oddandeven_points["Computer"][2]=ran.choice(number)
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
  RoundCount+=1
  listplayers=listplayer[0]+" || "+listplayer[1]
  print("\n||{}||".format(l.center(50)))
  print("||{}||".format("Even and odd are selected".center(50)))
  print("||{}||".format(l.center(50)))
  whochoice_oddandeven_points0010_print=whochoice_oddandeven_points[listplayer[0]][0]+" || "+whochoice_oddandeven_points[listplayer[1]][0]+"  "
  print("||{}||".format(listplayers.center(50)))
  print("||{}||".format(l.center(50)))
  print("||{}||".format(whochoice_oddandeven_points0010_print.center(50)))
  print("||{}||".format(l.center(50)))

  print("\n||{}||".format(l.center(50)))
  print("||{}||".format("Which user etered Which number?".center(50)))
  print("||{}||".format(l.center(50)))
  print("||{}||".format(listplayers.center(50)))
  print("||{}||".format(l.center(50)))
  ll1=" "*20
  rl1=" "*24
  print("||{}{} || {}{}||=>sum={}".format(ll1,whochoice_oddandeven_points[listplayer[0]][2],whochoice_oddandeven_points[listplayer[1]][2],rl1,finaloutput))
  print("||{}||".format(l.center(50)))

  print("\n||{}||".format(l.center(50)))
  print("||{}||".format("Points".center(50)))
  print("||{}||".format(l.center(50)))
  print("||{}||".format(listplayers.center(50)))
  print("||{}||".format(l.center(50)))
  print("||{}{} || {}{}||".format(ll1,whochoice_oddandeven_points[listplayer[0]][1],whochoice_oddandeven_points[listplayer[1]][1],rl1))
  print("||{}||\n".format(l.center(50)))

print("\n||{}||".format(l.center(50)))  
print("||{}||".format("Final points".center(50)))
print("||{}||".format(l.center(50)))
print("||{}||".format(listplayers.center(50)))
print("||{}||".format(l.center(50)))
print("||{}{} || {}{}||".format(ll1,whochoice_oddandeven_points[listplayer[0]][1],whochoice_oddandeven_points[listplayer[1]][1],rl1))
print("||{}||".format(l.center(50)))

print("\n||{}||".format(l.center(50)))  
print("||{}||".format("Winner".center(50)))
print("||{}||".format(l.center(50)))
if(whochoice_oddandeven_points[listplayer[0]][1]>whochoice_oddandeven_points[listplayer[1]][1]):
  winner=listplayer[0]
elif(whochoice_oddandeven_points[listplayer[0]][1]<whochoice_oddandeven_points[listplayer[1]][1]):
  winner=listplayer[1]  
else:
   winner="Draw" 
print("||{}||".format(winner.center(50)))
print("||{}||".format(l.center(50)))  