class Star:
    def __init__(self, id, name, x_coord, y_coord, description, constellation_id, size):
        self.id = id
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.description = description
        self.constellation_id = constellation_id
        self.size = size

class Constellation:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.stars = []  # список звезд в созвездии