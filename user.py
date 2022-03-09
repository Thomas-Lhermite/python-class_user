class User:

    def __init__(self, id, name, password):
        self.__init__
        self.name = name
        self.password = password
        self.id = id
    def check_password(self, password):
        return self.password == password

class Admin(User):
    def manage(self):
        print(f"{self.name} est un administrateur !")

class SuperAdmin(Admin):
    def manage(self):
        print(f"{self.name} est un super-administrateur !")

#Création d'un objet de type User
john = User()
john.name = "John"
kevin = Admin()
kevin.name = "Kévin"
didier = SuperAdmin()
didier.name = "Didier"
laurent = Admin()
laurent.name = "Laurent"
thomas = SuperAdmin()
thomas.name = "Thomas"



kevin.manage()
didier.manage()
laurent.manage()
thomas.manage()



