class Bird:
    # Attributes
    weight = 24
    size = 4
    feather_color = "Brown"

    # Constructor - setup every variable
    def __init__(self, weight, size, feather_color):
        self.feather_color = feather_color
        self.size = size
        self.weight = weight

    def __str__(self):
        return "   Color:  " + str(self.feather_color) + "   Size:   " + str(self.size) + "    Weight:     " + str(self.weight)

    def get_feather_color(self):
        return self.feather_color

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def set_feather_color(self, new_feather):
        self.feather_color = new_feather

    def set_size(self, new_size):
        self.size = new_size

    def set_weight(self, new_weight):
        self.weight = new_weight

