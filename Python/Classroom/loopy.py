# For loop for going through a grocery list

grocery_list = ["apples", "bananas", "oranges", "pears", "grapes"]

for item in grocery_list:
    print(item)

# For loop for going through a dictionary

hobby_dict = {"Ahmed": "Brætspil", "Line": "Gaming", "Shizuka": "Madlavning", "Mads": "Klatring"}

for key in hobby_dict:
    print(key + " likes " + hobby_dict[key])

# List comprehension for listing all even numbers from 1 to 100

even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)

# List comprehension for listing all odd numbers from 1 to 100

odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print(odd_numbers)

# List comprehension for listing all numbers from 1 to 100 that are divisible by 3

divisible_by_3 = [x for x in range(1, 101) if x % 3 == 0]
print(divisible_by_3)

# List comprehension for listing all numbers from 1 to 100 that are divisible by 3 and 5

divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)

# list comprehension that runs through a list and multiplies each number by 2 and adds 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [x * 2 + 1 for x in list1]
print(list2)