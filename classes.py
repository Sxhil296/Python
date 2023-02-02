class Point:
    def __init__(self, x, y):   #constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 2
# print(point2.x)

point = Point(10, 20)
print(point.x)
print(point.y)