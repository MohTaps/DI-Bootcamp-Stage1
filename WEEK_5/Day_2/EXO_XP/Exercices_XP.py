# Exercice 1 : Animaux De Compagnie

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# question 1

class Siamois(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# question 2

all_cats = [Bengal('Milou',4),Chartreux('Osca',5),Siamois('Miaou', 7)]


# question 3

sara_pets = Pets(all_cats)


# question 4

sara_pets.walk()
print()
print()

# Exercice 2

class Chien:
    def __init__(self, nom, age, poids):
        self.nom = nom
        self.age = age
        self.poids = poids


    def bark(self):
        return f'Le chien {self.nom} aboie'

    def run_speed(self):
        return f'Le {self.nom} court a la vitesse de {self.poids/self.age*10} m/s'


    def fight(self, other_dog):
        if self.run_speed() * self.poids > other_dog.run_speed() * other_dog.poids:
            print(f"Le chien {self.nom} est le gagnant du combat et le chien {other_dog.nom} a perdu !!!")
        else:
            print(f"Le chien {other_dog.nom} est le gagnant du combat et le chien {self.nom} a perdu !!!")


chien_1 = Chien("Boby", 3, 40)
chien_2 = Chien("Chling", 2, 54)
chien_3 = Chien("Rex", 1, 34)


print(chien_1.bark())
print(chien_2.bark())
print(chien_3.bark())


chien_1.fight(chien_2)
chien_2.fight(chien_3)
chien_3.fight(chien_1)






