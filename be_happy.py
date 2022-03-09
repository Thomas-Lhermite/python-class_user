from curses import beep


class Animal :
    def be_happy(self) :
        print('Cet animal est heureux')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Canary(Animal):
    pass

animal1 = Dog()
animal2 = Cat()
animal3 = Canary()

animal1.be_happy()
animal2.be_happy()
animal3.be_happy()
