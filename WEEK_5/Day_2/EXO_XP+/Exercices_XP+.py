class Family:

    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        dico = {}
        for elem in kwargs:
            dico.update({elem : kwargs[elem]})
        self.members.append(dico)

    def is_18(self,name):
        for membre in self.members:
            if name == membre['name']:
                if membre['age'] >= 18:
                    return True
                else:
                    return False
        return False

    def family_presentation(self):
        print(self.last_name)
        i = 1
        for membre in self.members:
            print(i,":",membre['name'])
            i+=1

famille = Family("TAPSOBA")
famille.born(name = 'Angela', age = 25, gender = 'Female', is_child=True)
famille.born(name = 'Moh', age = 12, gender = 'Male', is_child=True)
print(famille.is_18('Angela'))
print(famille.is_18('Moh'))
famille.family_presentation()

# Exercice 2 : La Famille Des Indestructibles

class TheIncredibles(Family):
    def __init__(self,lastname):
        super().__init__(lastname)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
             'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
             'incredible_name': 'SuperWoman'}
        ]
    def use_power(self, name):
        for membre in self.members:
            if name == membre['name']:
                if membre['age'] > 18:
                    print(f"{membre['power']}")
                else :
                    raise Exception(f"{name} n'a pas plus de 18 ans")
            else:
                print(f"{name} n'est pas membre de cette famille")

    def incredible_presentation(self):
        super().family_presentation()
        print('\nChaque membre à comme pouvoir : ')
        i = 1
        for membre in self.members:
            print(i,':',membre['power'])
            i += 1

famille = TheIncredibles("ZONGO")
famille.born(name = 'Raissa', age = 9, gender = 'Female', is_child=True, power = 'Unknown Power', incredible_name= 'Baby')
famille.born(name = 'Moh', age = 22, gender = 'Male', is_child=True, power = 'Speak to animals', incredible_name= 'Moh')
famille.incredible_presentation()