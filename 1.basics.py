# Task 1: create list of 100 random numbers from 0 to 1000

# importing Random module for being able to use random.sample() function:
import random
# creating a list using random.sample() function:
random_list = random.sample(range(0,1000),5)
# printing results:
print('the random list is: ' + str(random_list))


# Task 2: sort list from min to max (without using sort())

# trying usinf sorting function and printing it:
# print('sorted list (using function): ' + str(sorted(random_list)))

# sorting list using nested loops (for loop inside the for loop)
# outer 'for' loop expression:
for i in range(0, len(random_list)):
    # inner 'for' loop expression:
    for j in range(i+1, len(random_list)):
        # statement inside inner loop to execute if. checking if i is bigger or equal to j:
        if random_list[i] >= random_list[j]:
            # if condition is true put j before i in the list:
            random_list[i], random_list[j] = random_list[j], random_list[i]
# printing sorted list with no use of sorted function:
print('sorted list (using loops): ' + str(random_list))


# Task 3: calculate average for even and odd numbers

# importing the statistics module for being able to use mean() function:
import statistics
# importing mean()
from statistics import mean
#initialisation of even numbers list:
even_list = []
#initialisation of odd numbers list:
odd_list = []
# using loop to create 2 different lists using append() method. loop expression:
for i in random_list:
    #if statement of the loop (checking if the number is odd):
    if i % 2 == 0:
        # if the statement is true - add the number to odd_list:
        odd_list.append(i)
    # if the statement is false - add the number to even_list:
    else: even_list.append(i)

# Task 4: print both average result in console
# printing average of odd numbers in the list
print('odd numbers average is: ' + str(mean(odd_list)))
# printing average of even numbers in the list
print('even numbers average is: ' + str(mean(even_list)))