# Project Obj. = count from count(min) to max.
# count is where you are starting from.
# 2 variables
# num = for every number in max
import random


count = 0
max = int(random.randint(1, 1000000))


while count < max:
    print(count)
    count += 1
print(F"The max value is {max}.")
