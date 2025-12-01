class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Test chương trình
c = Circle(5)
print("Bán kính:", c.radius)
print("Diện tích:", c.area())
print("Chu vi:", c.perimeter())
