#
# character_name = "John"
# character_age = "35"
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + "years old.")
# #update variable
# character_name = "Mike"
# character_age = "50"
# print("He really liked the name " + character_name + ", ")
# print("but he didn't like being " + character_age + ".")
# #3 main types
# #string, number, bool
#
#
# #new line
# print("Giraffe\nAcademy")
#
# #print anything // exit
# print("Giraffe\"Academy")
#
# phrase = "Giraffe Academy"
# print(phrase)
#
# print(phrase + " is cool")
#
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.islower())
# print(phrase.upper().isupper())
#
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("Acad"))
# print(phrase.replace("Giraffe","Elephant"))
#
#
# print(-2.0515)
# print(3+5)
# print(3*(4+5))
# print(10 % 3) # 10/3 remainder = 1
# my_num = 5
# print(my_num)
# print(str(my_num)) #can print with strings
# print(str(my_num) + " is a string")
# my_num = -5
# print(abs(my_num))
# print(pow(3, 2)) #3^2
# print(max(4, 6))
# print(min(4, 6))
# print(round(3.5))
#
# #math modual more math!
# from math import *
# print(ceil(3.2))
#
#
# #input from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + " ! You are " + age + " years old!")

# #simple calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)
#
# #mad libs
# colour = input("Enter a colour: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + colour)
# print(plural_noun + " are blue")
# print("I love " + celebrity)
#

# friends = ["Kevin", "Karen", "Jim", "Paul"]
# print(friends)
# print(friends[2])
# print(friends[-1])
# print(friends[1:])
# friends[1] = "Mike"
# print(friends[1:3])

# lucky_numbers = [4, 8, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# # friends.extend(lucky_numbers)
# print(friends)
#
# friends2 = friends.copy()
# print(friends2)
#
# friends.append("Creed")
# print(friends)
#
# friends.insert(1, "Kelly")
# print(friends)
#
# friends.remove("Jim")
# print(friends)
#
# friends.pop()
# print(friends)
#
# print(friends.index("Toby"))
#
# friends.insert(1, "Toby")
# print(friends)
# print(friends.count("Toby"))
#
# friends.sort()
# print(friends)
#
# friends.clear()
# print(friends)
#
# lucky_numbers.reverse()
# print(lucky_numbers)


# # TUPLES! immutable - cannot change - different than lists, round brackets
# coordinates = (4, 5)
# print(coordinates[0])
# print(coordinates[1])
#
# coordinates2 = [(4, 5), (6,7), (80,34)]
# print(coordinates2[0])

# FUNCTIONS

# #task: say hi to user
# def say_hi(name, age):
#     print("Hello " + name + " You are " + str(age))
# #needs to call the function
# say_hi("Mike", 100)
# say_hi("Steve", 99)
#
# name_input = input("Enter your name: ")
# age_input = input("Enter your age: ")
# say_hi(name_input, age_input)

# # RETURN
# # function to cube a number
# def cube(num):
#     return num*num*num
#
# result = cube(4)
# print(result)
# print(cube(3))

# IF STATEMENTS
# is_male = False #boolean variable
# is_tall = True
#
# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#     print("You are neither male or tall or both")
#
# if is_male and is_tall:
#     print("You are a male and tall")
# else:
#     print("You are not a tall male")
#
# #every situation
# if is_male and is_tall:
#     print("You are a male and tall")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and (is_tall):
#     print("You are a tall female")
# else:
#     print("You are not a tall male")

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(342,3435135,453))

# # BUILDING A BETTER CALCULATOR
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1/ num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid Operator")

# DICTIONARIES!! word is the key, value is the definition, all keys need to be unique
# Jan -> January
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions["Sep"])
# print(monthConversions.get("Dec"))
# print(monthConversions.get("luv", "not a valid key")) #defualt if not existing

# WHILE LOOPS
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with while loop.")

# secret_word = "giraffe"
# guess = ""
# while guess != secret_word:
#     guess = input("Enter guess: ")
# print("You guessed the secret word!")

# set a limit to number of guesses
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses: #when out_of_guesses = True
#     print("You lose :(")
# else:
#     print("You guessed the secret word!")

# # FOR LOOPS
# for letter in "Giraffe Academy":
#     print(letter)
#
# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)
#
# for index in range(10):
#     print(index)
#
# for index in range(3, 7):
#     print(index)
#
# for index in range(len(friends)):
#     print(friends[index])
# for index in range(len(friends)):
#     print(index)

# EXPONENT FUNCTION
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(2, 3))

#  2D LIST
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# print(number_grid[0][0])
#
# for row in number_grid:
#     for column in row:
#         print(column)


# build a translator
# giraffe language, all vowels turn into G

#def translate(phrase):
#     translation =""
#     for letter in phrase:
#         if letter.lower()  in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: ")))

# Try Except  -- catching errors
# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError as err:
#     print(err)

# READING FILES
# employee_file = open("employees.txt", "r")
#
# # print(employee_file.readable()) # True means readable
# # print(employee_file.read())
# # print(employee_file.readline())
# # # print(employee_file.readlines())
# # print(employee_file.readlines()[1])
#
# employee_file.close()

# # WRITING TO FILES
# employee_file = open("employees.txt", "a") #adding text to end of file
# print(employee_file.write("\nToby - HR"))
# employee_file.close()

# employee_file = open("employees1.txt", "a") #create new file
# print(employee_file.write("Toby - HR"))
# employee_file.close()
#
# employee_file = open("employees1.txt", "w") #overwrite
# print(employee_file.write("Kelly - Customer Service"))
# employee_file.close()

# import useful_tools
#
# print(useful_tools.roll_dice(5))



# # Classes and Objects
# from Student import Student #from student file import student class
# student1 = Student("Jim", "Business", 3.1, False) #object is an instance of the class
# print(student1.major)

# from Question import Question
# questions_prompts = [
#     "What colour are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
#     "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What colour are starberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#     Question(questions_prompts[0], "a"),
#     Question(questions_prompts[1], "c"),
#     Question(questions_prompts[2], "b"),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score +=1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct!")
#
# run_test(questions)

# from Student import Student
# student1 = Student("Oscar", "Accounting", 3.1, False)
# student2 = Student("Phyllis", "Business", 3.8, False)
# print(student2.on_honor_roll())

# # INHERITANCE
# from Chef import Chef
# from ChineseChef import ChineseChef
# myChef = Chef()
# myChef.make_special_dish()
# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()

# PYTHON INTERPRETER
