sandwich_type = ""
subtotal = 0.0

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25


bev = input("Do you want a drink? ")

if bev == "yes":
    bevsel = input("Large: $2.25, Medium: $1.75, Small: $1.00    What size do you want?       ")
    if bevsel == "Large":
        print("Okay! A large drink is $2.25")
        subtotal += 2.25
    elif bevsel == "Medium":
        print("Okay! A medium drink is $1.75")
        subtotal += 1.75
    else:
        print("Okay! A small drink is $1")
        subtotal += 1
else:
    print("You don't want a drink? At a restaurant? What are you, some kind of inhuman species?")

print("Current price is: $",subtotal)
