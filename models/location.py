class Location():
    """Class to contain all location fields"""

    def __init__(self, id, name, address, animals=None):
        self.id = id
        self.name = name
        self.address = address
        self.animals = animals
