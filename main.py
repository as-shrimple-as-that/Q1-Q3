from time import sleep

ask = str(input('\nWhich program do you wish to launch? (Q1, Q2, Q3, Q4)\n'))

if ask == str("Q1"):
  #Q1Pythagoras
  sleep(1)
  from math import sqrt
  print("\n|---------------------")
  print("\nWelcome to Q1Pythagoras! This program will ask you for 2 values(a and b), and find the c value using the Pythagorean Theorum!\n")
  
  a = float(input("Please enter your a value.\n"))
  b = float(input("Please enter your b value.\n"))
  
  if a*b == float(0):
    quit("You cannot have a length of 0!\n")
  elif a < float(0) or b < float(0):
    quit("You cannot have a negative length!\n")
  else:
    print("That checks out, calculating...\n")

  sleep(1)

  c = sqrt((a**2)+(b**2))
  print("Your c value is", round(c, 5), "!")

  quit("\nEOF\n")

if ask == str("Q2"):
  #Q2RandomRange
  sleep(1)
  from random import randrange
  print("\n|---------------------")
  print("\nWelcome to Q2RandomRange! This program will ask you for 2 values, and find a random number between the two.")

  sleep(1)

  a = int(input("\nPlease enter your minimum value. \n"))
  b = int(input("Please enter your max value.\n"))

  if a > b:
    quit("Your minimum can't be bigger than your max!\n")
  elif a == b or b == a:
    quit("Your values can't be the same!\n")

  sleep(1)

  print("Your random number is", randrange(a,b), "!")

  quit("EOF")




if ask == str("Q3"):
  #Q3Addition

  sleep(1)

  from random import randrange
  print("\n|---------------------")
  print("\nWelcome to Q3Addition! The program will generate 2 random numbers, and ask you to answer the question of a + b! If you're right, then horray! If you're not, then you don't get a free full scholarship!")

  a = int(randrange(1, 100))
  b = int(randrange(1, 100))
  ans = a + b

  sleep(1)

  print('\nWhat is', a, "+", b, "?")
  uans = int(input())
  if uans != ans:
    quit("\nGuess who won't be persuing higher education for completely free?\n")
  else:
    print("Congratulations!\n You got it right, however... \n \nThere never was a free full scholarship 🤣🤣")

  quit("\nEOF\n")

if ask == str("Q4"):
  #Q4Picture

  from time import sleep
  from progress.bar import IncrementalBar

  with IncrementalBar('Processing...', max=324) as bar:
    for i in range(324):
        sleep(0.1)
        bar.next()
  print("\nheh, there's nothing here. use the other link, i just wanted to troll a little lol")