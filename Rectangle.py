from Position import Position
class Rectangle:
    # constructor
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # getters and setters

    def get_left_up(self):
        left_up = Position(self.__x1, self.__y1)
        return left_up

    def get_right_down(self):
        right_down = Position(self.__x2, self.__y2)
        return right_down

    def set_left_up(self, pos):
        self.__x1 = pos.get_x()
        self.__y1 = pos.get_y()

    def set_right_down(self, pos):
        self.__x2 = pos.get_x()
        self.__y2 = pos.get_y()

    def get_cortege(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def set(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # methods
    def show(self):
        print('------------------------')
        print("left up corner:")
        self.get_left_up().show()
        print("\nright down corner:")
        self.get_right_down().show()
        print('------------------------')

