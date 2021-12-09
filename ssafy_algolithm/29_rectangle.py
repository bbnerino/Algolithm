class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    

class Rectangle:
    def __init__(self,a,b):
        self.left= a
        self.right= b

    def get_area(self):
        return abs(self.left.x - self.right.x) * abs(self.left.y - self.right.y)
    def get_perimeter(self):
        return 2*abs(self.left.x - self.right.x) + 2*abs(self.left.y - self.right.y)
    def is_square(self):
        return bool(abs(self.left.x - self.right.x) == abs(self.left.y - self.right.y))

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 =Point(6,4)
r2 =Rectangle(p3,p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())