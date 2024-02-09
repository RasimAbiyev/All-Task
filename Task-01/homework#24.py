# """
# - Functions -
# A. Define a function greet_with_message that takes a username and a 
# message (with a default value of "Hello") as parameters and prints 
# the message along with the username.
def greet_with_message(username, message="Hello"):
    print(message, username)

greet_with_message("Rasim")

# B. Write a function calculate_discount that calculates the discounted 
# price of an item based on the original price and a discount rate 
# (default to 10%). Return the discounted price.
def calculate_discount(original_price, discount_rate):
    discounted_price = original_price * (1 - discount_rate)
    return discounted_price

original_price = 100
discount_rate = 0.1
discounted_price = calculate_discount(original_price, discount_rate)
print(discounted_price)

# C. Create a function sum_all that takes any number of arguments using 
# the asterisk operator in the parameter definition and returns the sum 
# of all the arguments.
def sum_all(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
result = sum_all(numbers)
print(result)

# D. Write a function calculate_product that takes at least two arguments
# and calculates their product. Use the asterisk operator in the parameter 
# definition to handle multiple arguments.
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

numbers = [2, 3, 4]
result = calculate_product(numbers)
print(result)

# E. Write a function sum_of_numbers that takes a variable number of integers
# as parameters and returns their sum.
def sum_of_numbers():
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers()
print(result)

# F. Create a function calculate_power that takes two parameters: a base number
# and an exponent, and returns the result of raising the base to the given exponent.
def calculate_power(base, exponent):
    return base ** exponent

result = calculate_power(2, 3)
print(result)

# G. Define a function named greet_user that takes a parameter username and prints 
# a greeting message like: "Hello, [username]!".
def greet_user(username):
    print(f"Hello, {username}!")

greet_user("John")

# H. Write a function called calculate_area that takes the radius of a circle as a 
# parameter and returns the area of the circle.
def calculate_area(radius):
    area = 3.14 * (radius ** 2)
    return area

radius = 5
area = calculate_area(radius)
print(area)

# I. Create a function average that takes a list of numbers as a parameter and calculates 
# the average of those numbers.
def average(numbers):
    return sum(numbers) / len(numbers)

numbers_list = [1, 2, 3, 4, 5]
avg = average(numbers_list)
print(avg)

# J. Implement a function maximum_number that takes a variable number of integers as 
# parameters and returns the largest number.
def maximum_number(numbers):
    return max(numbers)

numbers = [3, 5, 1, 7, 9]
result = maximum_number(numbers)
print(result)

# K. Define a function greet_with_salutation that takes a username and a salutation 
# (with a default value of "Mr.") as parameters and prints a greeting using the provided salutation.
def greet_with_salutation(username, salutation="Mr."):
    print(salutation, username)

greet_with_salutation("Abiyev")

# L. Write a function calculate_cost that calculates the total cost of purchasing a
# given quantity of items, considering a unit price and tax rate (default tax rate is 5%).
def calculate_cost(unit_price, quantity, tax_rate=0.05):
    cost = unit_price * quantity
    total = cost + (cost * tax_rate)
    return total

unit_price = 10
quantity = 3
total_cost = calculate_cost(unit_price, quantity)
print(total_cost)

# M. Create a function concatenate_strings that takes a variable number of strings as parameters 
# and concatenates them into a single string, separated by spaces.
def conactenate_strings():
    result = ""
    for arg in arguments:
        result += arg + " "
    return result.strip()

arguments = ("Hello", "world", "!")
result = conactenate_strings()
print(result)

# N. Write a function calculate_sum_and_product that takes at least two numbers as arguments 
# and returns both their sum and product. Use the asterisk operator in the parameter definition 
# to handle multiple arguments.
def calculate_sum_and_product(numbers):
    total = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total, product

numbers = [2, 3, 4, 5]
result, product_result = calculate_sum_and_product(numbers)
print(result)
print(product_result)

# O. Write a function find_max_min that takes a list of numbers as a parameter and returns both 
# the maximum and minimum numbers from the list. Use if statements to handle edge cases.
def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num

number_list = [4, 7, 2, 9, 1]
max_number, min_number = find_max_min(number_list)
print(max_number)
print(min_number)

# P. Create a function calculate_grade that takes a student's numerical score as a parameter and
# returns their corresponding letter grade based on the following scale:
# 90-100: 'A'
# 80-89: 'B'
# 70-79: 'C'
# 60-69: 'D'
# Below 60: 'F'
# Handle any invalid scores (less than 0 or greater than 100) by returning 'Invalid Score'.
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
score1 = 85
grade1 = calculate_grade(score1)
print(score1, grade1)

# Q. Write a function solve_quadratic that takes the coefficients of a quadratic equation 
# (a, b, c) as parameters and returns the real roots (if any) of the quadratic equation. 
# Use the quadratic formula.
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return root1, root2

a = 1
b = -3
c = 2
root1, root2 = solve_quadratic(a, b, c)
print(root1)
print(root2)

# R. Implement a function is_palindrome that takes a string as a parameter and returns True
# if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
def is_palindrome(string):
    return string == string[::-1]

string1 = "radar"
print(is_palindrome(string1))

# S. Create a function sort_numbers that takes three numbers as parameters and returns them in 
# ascending order as a tuple.
def sort_numbers(num1, num2, num3):
    sorted_nums = sorted([num1, num2, num3])
    return tuple(sorted_nums)

result = sort_numbers(3, 1, 2)
print(result)

# T. Write a function calculate_tax that takes an income amount and a tax rate as parameters 
# and calculates the tax amount. Return a tuple containing the tax amount and the net income 
# (income after tax).
def calculate_tax(income, tax_rate):
    tax_amount = income * tax_rate
    net_income = income - tax_amount
    return tax_amount, net_income

income = 50000
tax_rate = 0.2
tax, net = calculate_tax(income, tax_rate)
print(tax)
print(net)

# U. Create a function calculate_discounted_price that takes the original price and a discount 
# percentage as parameters. Return a tuple containing the discounted price and the amount saved.
def calculate_discounted_price(original_price, discount_percentage):
    amount = original_price * (discount_percentage / 100)
    discount_percentage = original_price - amount
    return discount_percentage, amount

original_price = 100
discount_percentage = 20
discount, amount_saved = calculate_discounted_price(original_price, discount_percentage)
print(discount)
print(amount_saved)

# Quiz.
# 1. What does the following function do?
def greet_user(username):
    print("Hello, " + username + "!")

#     = a) Greets the user with a customized message.
#     b) Prints "Hello, user!".
#     c) Defines a function but doesn't execute any action.
#     d) Raises an error due to an invalid function definition.

# 2. Which of the following functions best describes the calculations of the area of a circle?
#     a) calculate_circle_area(radius)
#     b) compute_circle_area(diameter)
#     c) get_circle_area(radius)
#     = d) calculate_area_circle(radius)

# 3. What is the purpose of a default parameter in a function?
#     a) It ensures the function returns a default value.
#     = b) It allows the function to have optional parameters.
#     c) It restricts the function to accept a specific type of argument.
#     d) It is used to specify the default return value of the function.

# 4. In Python, how do you pass a variable number of arguments to a function?
#     a) Using lists as arguments
#     b) Using tuples as arguments
#     = c) Using the asterisk (*) operator in the parameter definition
#     d) Using the exclamation mark (!) in the parameter definition

# 5. Which of the following functions best describes the calculations of the sum of a list of numbers?
#     = a) sum_list(numbers)
#     b) calculate_sum(numbers)
#     c) add_numbers(*numbers)
#     d) sum_all(*numbers)

# 6. What does the asterisk (*) operator do in the function definition?
#     a) Multiplies the function's output by the provided argument.
#     = b) Allows the function to take a variable number of arguments.
#     c) Raises an error due to an invalid operator usage.
#     d) Converts the argument to a string before passing it to the function.

# 7. Consider the following function:
def greet_user(username="Guest"):
    print("Hello, " + username + "!")

#     What is the default value for the username parameter in this function?
#     = a) "Guest"
#     b) "User"
#     c) None
#     d) "Hello"

# 8. In the following function, what happens if no value is provided for the message parameter?
def greet_with_message(username, message="Hello"):
    print(message + ", " + username + "!")

#     a) The function raises an error.
#     = b) The function uses the default value "Hello" for the message.
#     c) The function uses the default value "World" for the message.
#     d) The function uses the default value "Hi" for the message.

# 9. Which of the following is a valid function definition using default parameters?
#     = a) def calculate_area(radius, pi=3.14159):
#     b) def calculate_area(pi=3.14159, radius):
#     c) def calculate_area(radius=, pi=3.14159):
#     d) def calculate_area(radius=3.14159, pi):

# 10. Consider the function below:
def calculate_discount(price, discount_rate=0.1):
    return price * (1 - discount_rate)

#     What is the default discount rate used if not provided?
#     = a) 10%
#     b) 20%
#     c) 5%
#     d) 15%

# 11. Given the function:
def multiply(a, b=2):
    return a * b

#     If we call multiply(5), what will be the result?
#     = a) 10
#     b) 5
#     c) 7
#     d) 15

# 12. In the following function definition, what does the * represent?
def display_names(*names):
    for name in names:
        print(name)

#     a) It denotes multiplication in the function.
#     = b) It allows passing a variable number of names as arguments.
#     c) It signifies that 'names' is a string.
#     d) It raises an error in the function.

# 13. Given the function below:
def greet_with_messages(*messages):
    for message in messages:
        print(message)

#     If we call greet_with_messages("Hello", "Bonjour", "Hola"), how many messages will be printed?
#     = a) 3
#     b) 2
#     c) 1
#     d) 0

# 14. Consider the function definition:
def generate_pattern(symbol='*', count=5):
    return symbol * count

#     If we call generate_pattern(count=3), what will be the result?
#     = a) '***'
#     = b) '***'
#     c) '**'
#     d) '*****'

# 15. You have a list of numbers: [12, 5, 78, 43, 67, 89, 45, 23]. What will the function find_max_min return for this list?
#     a) (12, 5)
#     b) (5, 89)
#     c) (5, 12)
#     = d) (89, 5)

# 16. If the score provided to the function calculate_grade is 75, what will be the output of the function?
#     = a) 'C'
#     b) 'B'
#     c) 'D'
#     d) 'F'
   
# 17. For the quadratic equation with coefficients a=1, b=-5 and
# c=6, what will the function solve_quadratic return?
#     a) (-2, 3)
#     b) (-3, 2)
#     = c) (2, 3)
#     d) (-2, -3)

# 18. If the input string to the function is_palindrome is "radar", 
# what will the function return?
#     = a) True
#     b) False
      
# 19. For the input numbers 5, 2, 8, what will be the output of the function sort_numbers?
#     = a) (2, 5, 8)
#     b) (8, 5, 2)
#     c) (5, 2, 8)
#     d) (2, 8, 5)

# 20. If the income is $5000 and the tax rate is 20%, what will be the output of 
# the function calculate_tax?
#     = a) (1000, 4000)
#     = b) (4000, 1000)
#     c) (2000, 3000)
#     d) (2500, 2500)

# 21. If the original price is $100 and the discount rate is 25%, what will be the 
# output of the function calculate_discounted_price?
#     = a) (75.0, 25.0)
#     = b) (25.0, 75.0)
#     c) (100.0, 25.0)
#     d) (75.0, 100.0)
# """