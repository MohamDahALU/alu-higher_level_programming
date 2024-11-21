

class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1