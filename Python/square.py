#(One way to Import Function)
from functions import square  
for i in range(10):
    print(f"The square of {i} is {square(i)}")

#(Second way to Import Function)
import functions 
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")