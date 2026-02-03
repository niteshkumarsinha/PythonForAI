# variables 

"""
Multi line comments
Docstring for 1-Python-Basics.variables
"""

name = "Alice"
print(f"Hello, {name}!")

age = 30
print(f"{name} is {age} years old.")
print(f"In five years, {name} will be {age + 5} years old.")


is_student = True
print(f"Is {name} a student? {'Yes' if is_student else 'No'}")


first_name = "John"
last_name = "Doe"
print(f"Full name: {first_name} {last_name}")

total = 10 - 7
print(f"Total after subtraction: {total}")

power = 2 ** 3
print(f"2 to the power of 3 is: {power}")


message = "Hello, World!"
print(message)

greeting = "Hi there!"
print(greeting)

string_length = len(message)
print(f"Length of message: {string_length}")


multiline_string = """This is a
multi-line string.
Made using triple quotes.
"""
print(multiline_string)

long_dash = "--------------------"
print(long_dash)

separator = "-" * 20
print(separator)

repeated_message = "Echo! " * 3
print(repeated_message)

print(len(first_name))


is_logged_in = False
print(f"Is user logged in? {is_logged_in}")
is_admin = True
print(f"Is user an admin? {is_admin}")
is_active = True
print(f"Is user active? {is_active}")
has_permissions = False
print(f"Does user have permissions? {has_permissions}")

passed = total > 5
print(f"Has the user passed? {passed}")

can_vote = age >= 18
print(f"Can the user vote? {can_vote}")
is_senior = age >= 65
print(f"Is the user a senior citizen? {is_senior}")

print(age == 20)

result = (5 + 3) * 2
print(f"Result of (5 + 3) * 2: {result}")
difference = 15 - 4
print(f"Difference of 15 - 4: {difference}")
quotient = 20 / 4
print(f"Quotient of 20 / 4: {quotient}")
remainder = 10 % 3
print(f"Remainder of 10 % 3: {remainder}")
squared = 4 ** 2
print(f"4 squared is: {squared}")

can_drive = age >= 16 and has_permissions
print(f"Can the user drive? {can_drive}")

print(not is_logged_in)
print(not is_admin)
drunk = True
print(f"Is the user drunk? {drunk}")

score = 10
score += 5
print(f"Updated score: {score}")

full_name = first_name + " " + last_name
print(f"Full name using concatenation: {full_name}")

string = f"Hi There, My name is {full_name}."
print(string.lower())
print(string.upper())

text = "   Hello, World!   "
print(text.strip())

print(text.replace("World", "Python"))

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
print(words)



