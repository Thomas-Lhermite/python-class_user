from ctypes import sizeof


class Cat:
    size = 0
    name = "inconnu"
    age = 0


    def __init__(self, name, size, couleur):
        self.name = name
        self.size = size
        self.couleur = couleur

    def grow(self, aug, age):
        self.size = self.size + aug 
        self.age = self.age + age
    
    def showcolor(self, color):
        self.color = color


class Korat(Cat):
    def special(self, color):
        self.color = "Blue"




       
        

chat1 = Cat("Minou", 23, "noir")
chat2 = Cat("Kittie", 17, "blanc")

print(f"AVANT Kittie mesure maintenant {chat2.size}.")
print(f"AVANT Minou mesure maintenant {chat1.size}.")
print(f"AVANT Kittie mesure maintenant {chat2.age}.")
print(f"AVANT Minou mesure maintenant {chat1.age}.")
chat1.grow(2, 1)
chat2.grow(1.5, 1)
print(f"APRES Kittie mesure maintenant {chat2.size}.")
print(f"APRES Minou mesure maintenant {chat1.size}.")
print(f"APRES Kittie mesure maintenant {chat2.age}.")
print(f"APRES Minou mesure maintenant {chat1.age}.")


print(f"La couleur de Kittie est {chat2.couleur}.")
print(f"La couleur de Minou est {chat1.couleur}.")



print(f"La couleur des yeux de Kittie est {chat2.color}.")
print(f"La couleur des yeux de Minou est {chat1.color}.")