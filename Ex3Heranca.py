class BaseClass(object):
    pass


class DerivedClass(BaseClass):
    pass


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s


if __name__ == '__main__':
    r = Rectangle(10, 20)
    print(r.area())  # Output: 12 r.perimeter() # Output: 14

    s = Square(5)
    print(s.area())  # Output: 4 s.perimeter() # Output: 8
