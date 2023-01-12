from translate import Translator
traducteur= Translator(to_lang="en",from_lang="fr")
mots_francais= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt", "Je ne suis pas d'accord avec vous","Soldat au front de tous les combats",
"BURKINA de Thomas SANKARA jamais l'échine tu ne courberas"]
mots_anglais= {}
for mot in mots_francais:
    mots_anglais.update({mot:traducteur.translate(mot)})
print(mots_anglais)

