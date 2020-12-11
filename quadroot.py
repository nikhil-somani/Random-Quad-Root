# This project will find roots of a quadratic equation. Coefficients (a, b, c) are assumed to be in binary number system. Each bits of the binary number is randomly generated. Then the binary number will be converted to decimal number. After converting a, b, and c to decimal we will get the roots of the quadratic equation

from random import randint, seed
from datetime import datetime
from cmath import sqrt


seed(datetime.now())


# # calculator for power and remainder
# def calculator(a, b, mode):
#   # if/else block
    
#   return result


# random binary number generator
def randBinary():
  binar = []
  bitSize = 5
  for i in range(bitSize):
    rand = randint(0, 1)
    # will append here using rand on binar list
    binar.append(rand)
  return binar



# function for bin to decimal
# input a list of binary digits index 0 should have the leftmost bit
def bintodec(binary): 
  dec = 0
  # loop for the calculation
  for i in binary:  
    multiplier = len(binary) - 1
    r = i * pow(2, multiplier)
    dec += r
    multiplier -= 1
  return dec



def randNumberGenerator():
  # call randBinary() and assign to a varible
  # call bintodec() with the variable assigned above as the argument and assign the call with a variable named decimal
  temp = randBinary()
  decimal = bintodec(temp)
  return decimal



# finding root of a quadratic function given a, b, and c of ax^2+bx+c.


def findRoot():
  # call randNumberGenerator() three times and assign those calls to a, b, and c respectively

  a = randNumberGenerator() 
  b = randNumberGenerator()
  c = randNumberGenerator()  

  if(a):
    # find the two roots and assign those as r1 and r2.
    mode = 4 * a * c
    t = pow(b, 2)
    d = 2 * a
    r1 =  ( - b + sqrt(t - mode)  )   /  d
    r2 = ( -b - sqrt(t - mode)) / d
    return a, b, c, r1, r2
  else:
    findRoot()



a, b, c, root1, root2 = findRoot()


print('a: {}, b: {}, c: {}, root1: {}, root 2: {}'.format(a, b, c, root1, root2))

