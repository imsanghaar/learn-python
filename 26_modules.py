# Modules - A file in which code is written
# Modules help to organize code into manageable sections
# They also help to reuse code across multiple programs
# Importing a module
# Modules:
# import math
# import random
# 
# import calculator # From calculator.py
from calculator import add # With this we can make custom modules
add_result = add(10,100)
print(add_result)

# math
import math as mt
print(mt.sqrt(25))
# add_result = calculator.add(10,10)
# sub_result = calculator.sub(10,100)
# multiply_result = calculator.multiply(10,10)
# divide_result = calculator.divide(10,100)
# print(add_result)