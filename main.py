'''
02/25/2021

Review 

for loop
Repeat a set of statement a certain number of times.

for LCV in Sequence:
  Body Statement

Loop Control Variable
An ordinary int variable that is initialized, tested, and changed as the loop executes.

Sequence
An iteration statement
- range(#)
- list

[0,1,2,3]
["one", "hundred", "two"]

ex.

for x in range(4):
  print (x)

> 0
  1
  2
  3

print ("while loop")
switch = 0

while (switch > -20):
  print (switch)
  switch += 1

print ("for loop")
for x in ["one", "hundred", "two", 4, 6, True]:
  print (x)

range() function
Generates a list of integers
- 1 argument; range(#) >> range(stop)
- 2 arguments; range(#,#) >> range(start, stop)
- 3 arguments; range(#,#,#) >> range(start, stop, step)

range(5)  # [0, 1, 2, 3, 4]
range(1,4)  # [1, 2, 3]
range(3,12,3) # [3, 6, 9]
'''


# Exercise 1
# Outputs: 2x hello, 2x new year, 1x 2021
for x in range(5):
  if (x < 2):
    print ("hello")
  elif (x < x):
    print ("Python")
  elif (x < 4):
    print ("new year")
  elif (x < 1):
    print ("bye")
  else:
    print (2021)


# Exercise 2
# Outputs: 1x hello, 2x Python, 1x new year, 1x bye, 2x 2021
for x in range(4, 11):  # [4, 5, 6, 7, 8, 9, 10]
  if (x < 5):
    print ("hello")
  elif (x < 7):
    print ("Python")
  elif (x < 8):
    print ("new year")
  elif (x < 9):
    print ("bye")
  else:
    print (2021)


# Exercise 3
# Outputs: 2x hello, 1x Python, 1x new year, 2x bye, 2x 2021
for x in range(7, 29, 3): # [7, 10, 13, 16, 19, 22, 25, 28]
  if (x < 11):  # 11, 12, 13
    print ("hello")
  elif (x < 14): # 14, 15, 16
    print ("Python")
  elif (x < 17):  # 17, 18, 19
    print ("new year")
  elif (x < 24): # 23, 24, 25
    print ("bye")
  else:
    print (2021)