####################################################################
# Title:  Equation of a Trinomial
# Programmer:  Tabitha Wong
# Last modified: 
# Purpose: This program takes as input the a, b, and c values of a
# trinomial and determines the equation that will be created
#####################################################################
#user inputs a,b,and c values
a = int(input("Input your a value here:"))
b = int(input("Input your b value here:"))
c = int(input("Input your c value here:"))

#check for presence of x^2 term
if a == 0:
   aOutput = ""
   #check for presence of x term
   if b == 0:
       bOutput = ""
       #check for presence and value of constant term
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = str(c)
   #check for value of x term      
   elif b == 1:
       bOutput = "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b == -1:
       bOutput = "-x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b < 1:
       bOutput = str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   else:
       bOutput = str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)

#check for value of x^2 term       
elif a == 1:
   aOutput = "x^2"
   if b == 0:
       bOutput = ""
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = str(c)
          
   elif b == 1:
       bOutput = "+x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b == -1:
       bOutput = "-x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b < 1:
       bOutput = str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   else:
       bOutput = "+" + str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)

          
elif a == -1:
   aOutput = "-x^2"
   if b == 0:
       bOutput = ""
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = str(c)
          
   elif b == 1:
       bOutput = "+x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b == -1:
       bOutput = "-x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b < 1:
       bOutput = str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   else:
       bOutput = "+" + str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)

          
else:
   aOutput = str(a) + "x^2"
   if b == 0:
       bOutput = ""
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b == 1:
       bOutput = "+x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b == -1:
       bOutput = "-x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   elif b < 1:
       bOutput = str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)
          
   else:
       bOutput = "+" + str(b) + "x"
      
       if c == 0:
           cOutput = ""
       elif c < 0:
           cOutput = str(c)
       else:
           cOutput = "+" + str(c)

          
#Output trinomial
print("The trinomial is" + " " + aOutput + bOutput + cOutput)

