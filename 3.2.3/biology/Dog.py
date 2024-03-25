class Dog:
    #Attributes
    fur = True
    legs = 4
    fur_color = "Brown"

    #Constructor - setup every variable
    def __init__(self, fur, legs_num, color):
        self.fur = fur
        self.legs = legs_num
        self.fur_color = color

    def __str__(self):
        return "fur:  " + str(self.fur) + "Legs:   " + str(self.legs) + "Fur color:     " + str(self.fur_color)