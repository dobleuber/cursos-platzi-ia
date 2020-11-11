class Campo:

    def __init__(self):
        self.drunk_coords = {}

    def add_drunk(self, drunk, coord):
        self.drunk_coords[drunk] = coord

    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        current_coord = self.drunk_coords[drunk]
        new_coord = current_coord.move(delta_x, delta_y)

        self.drunk_coords[drunk] = new_coord
        return new_coord

    def get_coord(self, drunk):
        return self.drunk_coords[drunk]