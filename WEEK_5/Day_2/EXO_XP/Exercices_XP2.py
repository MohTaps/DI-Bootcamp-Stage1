from Exercices_XP import Chien

class PetChien(Chien):
	    def __init__(self, nom, age, poids, trained=False):
	        super().__init__(nom, age, poids)
	        self.trained = trained

	    def train(self):
	        print(f"{self.bark()}")

	    def play(self, *args):
	        word = self.nom + ", "
	        for elem in range(0, len(args)):
	            if elem == len(args) - 1:
	                word += args[elem]
	            elif elem == len(args) - 2:
	                word += args[elem] + " et "
	            else:
	                word += args[elem] + ", "
	        print(f"{word}, all play together")

	    def do_a_trick(self):
	        import random
	        if self.trained == True:
	            nb_hasard = random.randint(1, 4)
	            if nb_hasard == 1:
	                print(f"{self.nom} does a barrel roll")
	            elif nb_hasard == 2:
	                print(f"{self.nom} stands on his back legs")
	            elif nb_hasard == 3:
	                print(f"{self.nom} shakes your hand")
	            else:
	                print(f"{self.nom} plays dead")
	        else :
	            print("Buzzzzz")

print()
print()
chien_1 = PetChien("Boby", 3, 40, True)
chien_2 = PetChien("Chling", 2, 54, True)
chien_3 = PetChien("Rex", 1, 34, False)

print()
print()
chien_1.train()
chien_2.play(chien_1.nom,chien_2.nom)
chien_3.do_a_trick()
chien_3.do_a_trick()
chien_1.do_a_trick()