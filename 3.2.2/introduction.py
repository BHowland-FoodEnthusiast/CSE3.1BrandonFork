'''''
import random
def random_number():
    n1 = random.randint(30, 50)
    print(n1)


x = 0
while x < 1000:
    x += 1
    random_number()
'''''

def larger_val(num1, num2):
    if num1 > num2:
        return("Larger value:" , num1)
    elif num1 < num2:
        return("Larger value:" , num2)
    else:
        return("They are the same.")
larger_val(num1=int(input("Number 1:")), num2=int(input("Number 2:")))
print()