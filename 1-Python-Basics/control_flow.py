temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's a cool day.")


age = 20
has_licence = True

if age >= 18 and has_licence:
    print("You can drive.")
else:
    print("You cannot drive.")

has_ticket = True

if has_ticket:
    if age >= 18:
        print("You can enter the concert.")
    else:
        print("You cannot enter the concert due to age restriction.")
else:
    print("You cannot enter the concert without a ticket.")

first_name = "John"
last_name = "Doe"
print(f"Full name: {first_name} {last_name}")

has_permissions = age >= 18 and has_licence
print(f"Does user have permissions? {has_permissions}")

