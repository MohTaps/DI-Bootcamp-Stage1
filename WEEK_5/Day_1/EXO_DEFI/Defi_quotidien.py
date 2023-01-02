class Ferme:
  def __init__(self, nom):
    self.nom = nom
    self.animaux = {}

  def ajouter_un_animal(self, animal, compteur=1):
    if animal in self.animaux:
      self.animaux[animal] += compteur
    else:
      self.animaux[animal] = compteur

  def information(self):
    info = f"La ferme {self.nom} \n"
    for animal, compteur in self.animaux.items():
      info += f"{animal:<7}: {compteur}\n"
    return info

  def type_animaux(self):
    return sorted(self.animaux.keys())

  def info_type(self):
    animal_types = self.type_animaux()
    if len(animal_types) == 0:
      return "La ferme ne possède aucun animal."
    elif len(animal_types) == 1:
      return f"La ferme de {self.nom} a des {animal_types[0]}s."
    else:
      last_animal = animal_types.pop()
      return f"La ferme de {self.nom} a des {', '.join(animal_types)}, et {last_animal}."

macdonald = Ferme("McDonald")
macdonald.ajouter_un_animal('boeufs',5)
macdonald.ajouter_un_animal('moutons')
macdonald.ajouter_un_animal('moutons')
macdonald.ajouter_un_animal('chevres', 12)
print(macdonald.information())
print()
print()
print(macdonald.type_animaux())
print(macdonald.info_type())
