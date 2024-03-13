sandwich_type = ""
order = [ "", "", "", 0]
subtotal = 0.0

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
order[0] = input("Sandwich Choice: ")

# Calculating Sandwich Price
if order[0] == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif order[0] == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

# Beverage Choice
order[2] = input("Do you want a beverage? yes or no")
if order[2] == "yes":
    order[3] = input("What size beverage would you like? Small, Medium, or Large")
    if order[3] == "small":
        print("You chose small, so $1.00")
        subtotal += 1
    if order[3] == "medium":
        print("You chose medium, so $1.75")
        subtotal += 1.75
    if order[3] == "large":
        print("You chose large, so $2.25")
        subtotal += 2.25

# Fries
order.append( input("Do you want french fries? Yes or No"))
if order. == "yes":
    fry_size = input("What size fries would you like? Small, Medium, or Large")
    if fry_size == "small":
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            subtotal += 2
        else:
            print("You chose small fries for $1")
            subtotal += 1
    elif fry_size == "medium":
        print("You chose medium for $1.50")
        subtotal += 1.50
    else:
        print("You chose large fries for $2")
        subtotal += 2

# Kethcup
ketchup = float(input("HJow many ketup packets would you like? $0.25 each"))
if ketchup >= 0:
    subtotal += ketchup * .25

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

print(sandwich_type)
if bev_choice == "yes":
    print(bev_size)
if fry_choice == "yes":
    print(fry_size)

print(subtotal)