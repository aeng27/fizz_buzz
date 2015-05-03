n = 45
title = 'Fizz buzz counting up to {0}'.format(n)
print (title)
for number in range (1,n+1):
    if number % 3 == 0 and number % 5 == 0:
      print ('Fizz Buzz')
    elif number % 3 == 0:
      print ('Fizz')
    elif number % 5 == 0:
      print ('Buzz')
    else:
      print(number)
      