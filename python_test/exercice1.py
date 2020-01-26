import numpy as np

class Circle:
    def __init__(self, radius):
        self.r = radius
    
    def area(self):
        area = np.pi * (self.r * self.r)
        return area

    def perimeter(self):
        perimeter = 2 * np.pi * self.r
        return perimeter

def main():
    r = 1
    circle = Circle(r)
    area = circle.area()
    perimeter = circle.perimeter()
    print(f"radius is {r}")
    print(f"area is {area}")
    print(f"perimeter is {perimeter}")

main()