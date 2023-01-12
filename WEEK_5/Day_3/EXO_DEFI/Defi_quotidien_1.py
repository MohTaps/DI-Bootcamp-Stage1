class Cercle:
    def __init__(self,rayon,diametre):
        self.rayon=rayon
        self.diametre=diametre
        liste=[]
        self.liste=liste
        
    def aire(self):
        aire1 = 3.14*self.rayon*self.rayon
        return f"L'aire de ce cercle est {aire1}."

    def __eq__(self,autre):
        self.liste.append(self.rayon)
        self.liste.append(self.diametre)
        self.liste.append(autre.rayon)
        self.liste.append(autre.diametre)
        self.liste.sort()
        aire2 = autre.rayon*2*3.14
        aire1 = 3.14*self.rayon*self.rayon
        print("Liste trier:",self.liste)
        if aire1 == aire2:
            
            print(self.liste)
            return "Les deux cercles ont les memes dimensions."
        elif aire1 > aire2:
            
            return "Le premier cercle est le plus grand."

        else:
            return "Le deuxieme cercle est le plus grand "
    def __repr__(self,autre):
        aire2 = autre.rayon*2*3.14
        aire1 = 3.14*self.rayon*self.rayon
        return f"{self.__class__.__name__} : {aire1+aire2}"
   
        
        
        
        
cercle_1=Cercle(4,12)      
cercle_2=Cercle(6,18)  
print(cercle_1.aire())
print(cercle_1.__eq__(cercle_2))
print(cercle_1.__repr__(cercle_2))