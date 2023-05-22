# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# 2. Print the difference between the largest and smallest value:

difference = max(numbers) - min(numbers)
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

has_two_twos = False
for i in range(len(numbers) - 1):
    if numbers[i] == 2 and numbers[i + 1] == 2:
        has_two_twos = True
        break
print(has_two_twos)

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.

partial_sum = 0
ignore_section = False
for num in numbers:
    if num == 6:
        ignore_section = True
    elif num == 7:
        ignore_section = False
    elif not ignore_section:
        partial_sum += num
print(partial_sum)

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.

unlucky_sum = 0
skip_next = False
for i in range(len(numbers)):
    if numbers[i] == 13 or skip_next:
        skip_next = False
        continue
    unlucky_sum += numbers[i]
    if i < len(numbers) - 1 and numbers[i + 1] == 13:
        skip_next = True
print(unlucky_sum)








