class Position:

    # constructor
    def __init__(self, x=None, y=None):
        if x is None or y is None:
            self.__x = 0
            self.__y = 0
        else:
            self.__x = x
            self.__y = y

    # getters and setters

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, y):
        self.__x = y

    def set_y(self, y):
        self.__y = y

    def set_pos(self, x=None, y=None):
        if x is None and y is None:
            self.__x, self.__y = pag.position()
        else:
            self.__x = x
            self.__y = y

    def get_pos(self):
        return (self.__x, self.__y)


    def show(self):
        print("x =", self.get_x(), "\ny =", self.get_y(), '\n')
