import sys
if len(sys.argv) == 1:
   user_input = raw_input ("Pick a number to count up to: ")
elif len (sys.argv) > 2:
      user_input = raw_input ("Please pick only one number to count up to: ")
else:
      user_input = sys.argv[1]
instructions = True
while instructions:
    try:
      int(user_input)
      instructions = False
    except ValueError:
      user_input = raw_input ("Please enter one number only: ")
n = user_input
title = 'Fizz buzz counting up to {0}'.format(n)
print(title)
for number in range (1,int(n)+1):
    if number % 3 == 0 and number % 5 == 0:
      print ('Fizz Buzz')
    elif number % 3 == 0:
      print ('Fizz')
    elif number % 5 == 0:
      print ('Buzz')
    else:
      print(number)