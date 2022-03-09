class User:

    def __init__(self, id, name, password):
        self.name = name
        self.password = password
        self.id = id
        print(f"{self.name} vient d\'être crée.")

    def __str__(self) :
        return f"{self.name, self.id}"
    def check_password(self, password):
        return self.password == password

class Admin(User):
    def manage(self):
        print(f"{self.name} est un administrateur !")

class SuperAdmin(Admin):
    def manage(self):
        print(f"{self.name} est un super-administrateur !")


user1= User(1, 'John', '12345')
user2 = Admin(1, 'Faustin', '67890')
user3 = SuperAdmin(1, 'Théo', '163758')
etablissement = 'Lycée NDLP'
service = 'Service informatique'
liste_divers = [etablissement, service, user1, user2, user3]

for item in liste_divers:
    print(item)       