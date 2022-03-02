class User:
    def check_password(self, password):
        return self.password == password

#Création d'un objet de type User
john = User()

#Définition d'attribut pour cet objet
john.id = 1
john.name = 'John'
john.password = '12345'

print(f'Bonjour, je suis {john.name}.')
print(f'Mon id est le {john.id}.')
print(f'Mon mot de passe est {john.password}.')

print(f'Vérification du mot de passe "1234" = {john.check_password("1234")}.')
print(f'Vérification du mot de passe "12345" = {john.check_password("12345")}.')