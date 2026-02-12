person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

person["age"] = 31
print(person["age"])   # Output: 31

person["country"] = "USA"
print(person["country"])  # Output: USA

del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

print(person.keys())    # Output: dict_keys(['name', 'age', 'country'])
print(person.values())  # Output: dict_values(['John', 31, 'USA'])
print(person.items())   # Output: dict_items([('name', 'John'), ('age', 31), ('country', 'USA')])   


empty = ()
point = (3, 5)
print(empty)  # Output: ()
print(point)  # Output: (3.5)

print(point[0])  # Output: 3
print(point[1])  # Output: 5
# point[0] = 4  # This will raise a TypeError since tuples are immutable

