####################################################################
# Title: Eat or no eat? Pizza or no pizza?
# Programmer:  Tabitha Wong
# Last modified: 
# Purpose: This program helps the user decide if
# they should eat and if they should buy a pizza
#####################################################################
#check if user is hungry
HungerLevel = input("Are you hungry?")
if HungerLevel in ["yes", "yeah", "Yeah", "Yes", "YES", "YES!", "y", "Y", "sure", "uh huh", "Yes!", "yes!"]:
  #check if user likes pizza!
 PizzaLove = input("Do you like pizza?")
 if PizzaLove in ["yes", "yeah", "Yeah", "Yes", "YES", "YES!", "y", "Y", "sure", "uh huh", "Yes!", "yes!"]:

   #check if user has enough money for a pizza
   MoneyHave = int(input("How much money do you have? $"))

   #prompt user to buy pizza if they have at least $7
   if MoneyHave == 7:
     print("Perfect! You can and should buy a pizza! Pizzas are the bomb.com!")
   #calculate how much user will have left after they buy pizza
   elif MoneyHave > 7:
     MoneyLeft = MoneyHave - 7
     print("Perfect! You'll have $"+str(MoneyLeft)+" left after you buy a pizza! You're so lucky!")
   #calculate how much user needs to buy pizza
   else:
     MoneyToHave = 7 - MoneyHave
     print("Aww darn :( You need $"+str(MoneyToHave)+" more to buy a pizza. Better start working!")
 #scold user for not liking pizza
 else:
   print("Well I guess we can't be friends.")

else:

 #user inputs how long it has been since their last meal
 EatTime = int(input("How many hours has it been since you've eaten?"))

 #prompt user to eat if it has been over 5 hours
 if EatTime > 5:
   print("Woah! You should eat even if you aren't hungry!")
   #calculate how long ago user should have eaten
   HoursSince = EatTime - 5
   if HoursSince == 1:
     print("It's been 1 hour since the last time you should've had a meal!")
   else:
     print("It's been "+ str(HoursSince)+ " hours since the last time you should've had a meal!")
   #prompt user to buy pizza if they have at least $7
   MoneyHave = int(input("How much money do you have? $")
   )
   if MoneyHave == 7:
     print("Perfect! You can and should buy a pizza! Eat and enjoy!")
   #calculate how much money user will have left after buying a pizza
   elif MoneyHave > 7:
     MoneyLeft = MoneyHave - 7
     print("Perfect! You'll have $"+str(MoneyLeft)+" left after you buy a pizza! Savour every bite!")
   #calculate how much money user needs to buy a pizza
   else:
     MoneyToHave = 7 - MoneyHave
     print("Uh oh. You need $"+str(MoneyToHave)+" more to buy a pizza. Guess you'd better get a job or starve!")
 #calculate how long user can wait before eating again
 elif 0 < EatTime < 5:
   HoursLeft = 5 - EatTime
   if EatTime == 1:
     print("Well, I guess you have 1 hour left before you should eat your next meal. I recommend pizza :)")
   else:
     print("Well, I guess you have " + str(HoursLeft)+" hours left before you should eat your next meal. I recommend pizza :)")
 #scold user for inputting hours incorrectly
 else:
   print("Can you even tell time?")
