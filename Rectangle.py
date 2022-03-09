class Rectangle:
    def area(self):
        return self.height * self.width 
    

rectangle1 = Rectangle()

rectangle1.height = 4
rectangle1.width = 3

print(f'La surface du rectangle est de {rectangle1.area()}.')
