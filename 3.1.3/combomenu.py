sandwich_type = ""
order = ["", "", "", 0]

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
order[0] = input("Sandwich Choice: ")

# Calculating Sandwich Price
if order[0] == "chicken":
    print("You chose chicken, which will be $5.25")
    order[3] += 5.25
elif order[0] == "tofu":
    print("You chose tofu, which will be $5.75")
    order[3] += 5.75
else:
    print("You chose beef, which will be $6.25")
    order[3] += 6.25

# Beverage Choice
order[1] = input("Do you want a beverage? yes or no")
if order[1] == "yes":
    order[2] = input("What size beverage would you like? Small, Medium, or Large")
    if order[2] == "small":
        print("You chose small, so $1.00")
        order[3] += 1
    if order[2] == "medium":
        print("You chose medium, so $1.75")
        order[3] += 1.75
    if order[2] == "large":
        print("You chose large, so $2.25")
        order[3] += 2.25

# Fries
order.append(input("Do you want french fries? Yes or No"))
if order[4] == "yes":
    order.append(input("What size fries would you like? Small, Medium, or Large"))
    if order[5] == "small":
        order.append(input("Do you want to supersize that for $2? Yes or no"))
        if order[6] == "yes":
            order[5] = "large"
            order[3] += 2
        else:
            print("You chose small fries for $1")
            order[3] += 1
    elif order[6] == "medium":
        print("You chose medium for $1.50")
        order[3] += 1.50
    else:
        print("You chose large fries for $2")
        order[3] += 2

# Kethcup
order.append(float(input("How many ketchup packets would you like? $0.25 each")))
if order[7] >= 0:
    order[3] += order[7] * .25

if order[1] == "yes" and order[4] == "yes":
    order[3] -= 1

print(sandwich_type)
if order[1] == "yes":
    print(order[1])
if order[4] == "yes":
    print(order[4])

print(order[3])
