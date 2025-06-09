from hello import chai

chai(5)

# Python import 

import keyword
import dict
import random
import math
import calendar

print(keyword.kwlist)
print(dict.var)
print(calendar.month(2025,5))
print(math.floor(random.random()*10))

a=10
b=0

try:
  print(a/b)

except:
  print("Error in division as you can't dmivide any number by 0")

else:
  print("Goot to go")



file = open("C:\\Users\\user\\coders\A.txt","w")
file.write("Hello Python world\n How's going everything. I am Aniket chauhan")
print("File created successfully and typed as well")

file = open("C:\\Users\\user\\coders\A.txt","r")
print("\n", file.read(100))