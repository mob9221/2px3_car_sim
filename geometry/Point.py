class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_tuple(self):
        return self.x, self.y

    def toString(self):
        return str(self.x) + "," + str(self.y)

    @staticmethod
    def t2p(tup):
        return Point(tup[0], tup[1])

    @staticmethod
    def string2point(string: str):
        list_int = string.split(',')
        return Point(int(list_int[0]), int(list_int[1]))