import re
matrix = [
[7,'i',3],
['T','s','i'],
['h','%','x'],
['i',' ','#'],
['s','M',' '],
['&','a',' '],
['#','t','%'],
['^','r','!'],
		]

for i in matrix:
	print("\n\t_______________________")
	for j in i:
		print("\t ",j," | ",end="")
print("\n\t_______________________")

chaine = ""
chaine_entiere = list(zip(*matrix))
print()
print(chaine_entiere)
print()
for elem in chaine_entiere:
	for ce in elem:
		chaine = chaine + str(ce)
caract_speciale = '[@_!#$%^&*()<>?}{~:]+'

liste_symbole = re.findall(caract_speciale,chaine)

suppression_symbole = re.sub(caract_speciale,' ',chaine)

chaine_liste = list(suppression_symbole)

for special in chaine_liste:
	if special.isdigit():
		chaine_liste.remove(special)

phrase_cacher = "".join(chaine_liste)
print(f"\nLe message coder est : {phrase_cacher}")