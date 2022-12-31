# Exercice 1 : Convertir Des Listes En Dictionnaires


cles = ['Dix', 'Vingt', 'Trente', 'Quarante', 'Cinquante', 'Soixante']
valeurs = [10, 20, 30, 40, 50, 60]

mon_dico = dict(zip(cles,valeurs))
print(mon_dico)

# Exercice 2 : Cinemax

famille = {'Sidiki': 43, 'Issouf': 13, 'Yann': 5, 'Sacha': 8, 'Clement': 2}
prix_total = 0

for nom, age in famille.items():
    if age < 3:
        prix_billet = 0
    elif age >= 3 and age <= 12:
        prix_billet = 10
    else:
        prix_billet = 15
    print(f"{nom} doit payer {prix_billet*100} fcfa.")
    prix_total += prix_billet
print(f"La somme totale que doit payer la famille pour avoir acces a la salle de cine est de {prix_total*100} fcfa.")
print()


famille = {}
nomss = []
agges = []
while True:
    nom = input("Entrez votre nom svpp ou tapez 'q' pour quitter : ")
    nomss.append(nom)
    if nom == 'q':
        break
    age = int(input("Entrez votre age svpp : "))
    agges.append(age)
    famille[nom] = age

prix_total = 0
for nom, age in famille.items():
    if age < 3:
        prix_billet = 0
    elif age >= 3 and age <= 12:
        prix_billet = 10
    else:
        prix_billet = 15
    print(f"{nom} doit payer {prix_billet*100} fcfa.")
    prix_total += prix_billet

famille = dict(zip(nomss,agges))
print()
print(famille)
print(f"\nLa somme totale que doit payer la famille pour avoir acces a la salle de cine est de {prix_total*100} fcfa.")



# Exercice 3 : Zara

# question 2


marque = {
    "nom": "Zara",
    "date_de_creation": 1975,
    "nom_du_createur": "Amancio Ortega Gaona",
    "classification": ["men", "women", "children", "home"],
    "concurrents": ["Gap", "H&M", "Benetton"],
    "numero_boutique": 7000,
    "couleur_maj": {
        "France": "blue",
        "Espagne": "red",
        "Etats_Unis": ["pink", "green"]
    }
}

print(marque)
print()

# question 3


marque["numero_boutique"] = 2

print("\tApres changements\n")
print(marque)
print()


# question 4

print(f"Les clients de Zara sont : {', '.join(marque['classification'])}.")
print()

# question 5

marque["pays_de_creation"] = "Espagne"
print("\tApres ajout\n")
print(marque)
print()

# question 6

if "concurrents" in marque:
    marque["concurrents"].append("Desigual")
print("\tApres ajout de la marque\n")
print(marque)
print()

# question 7

del marque["date_de_creation"]
print("\tApres ajout de la date de creation\n")
print(marque)
print()

# question 8

print(marque["concurrents"][-1])
print()

# question 9

print(', '.join(marque['couleur_maj']['Etats_Unis']))
print()

# question 10

print(len(marque))
print()

# question 11

print(marque.keys())
print()


# question 12

more_on_zara = {
    "date_de_creation": 1975,
    "numero_boutique": 10000
}


# question 13

marque.update(more_on_zara)

# question 14 

print(marque["numero_boutique"])


