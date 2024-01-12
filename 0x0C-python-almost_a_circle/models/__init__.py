class Base:
    __nb_objects = 0
    def __init__(self, id = None):
        if self.id != None:
            self.id = id
        else:
            __nb_objects += 1