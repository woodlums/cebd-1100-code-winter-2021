#from DemoFunctions.BasicMath import *

import DemoFunctions.BasicMath as m
import DemoFile as x


print("Adding Demo")
n1 = int(input("Please enter number 1: "))
n2 = int(input("Please enter number 2: "))

result = m.add(n1, n2)


print("The result is : " + str(result))


print(x.DemoFcn1())