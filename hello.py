import requests


response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())


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