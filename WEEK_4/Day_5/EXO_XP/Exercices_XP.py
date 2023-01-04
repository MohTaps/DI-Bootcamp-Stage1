print("******************************************************")
print("*     BIENVENNUE DANS LE JEU TIC TAC TOE             *")
print("*                                                    *")
print("*                                                    *")
print("* Deux joueurs a savoir un jour X et un joueur O     *")
print("*                                                    *")
print("*                                                    *")
print("* lignes commes abscisses et colonnes comme ordonnées*")
print("******************************************************")

print()





tableau=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]



def affichage_du_tableau():
    ecart=(5*"***")
    print(f"          {ecart}") 
    for tab in tableau:
        print(f"          * {tab[0]}  | {tab[1]}  |{tab[2]}  *")
        print(f"          * ---|--- |---*")
    
    print(f"          {ecart}") 




affichage_du_tableau()
def symbole(joueur_sigle):
    print(f"\nJoueur {joueur_sigle} a votre tour de jouer")
    ligne=int(input("\nEnter une ligne Enter une ligne, 1 pour la premiere, 2 pour deuxieme et 3 pour la derniere ligne: "))

    while ligne<1 or ligne>3:
        ligne=int(input("\nVeuillez entrer une ligne comprise entre 1 et 3: "))
    colonne=int(input("\nEnter une colonne, 1 pour la premiere, 2 pour deuxieme et 3 pour la derniere colonne : "))

    while colonne<1 or colonne>3:
        colonne=int(input("\nVeuillez entrer une colonne comprise entre 1 et 3: "))

    if tableau[ligne-1][colonne-1]==" ":
        tableau[ligne-1][colonne-1]=joueur_sigle
        affichage_du_tableau()
    else:
        print(f"La case choisie est occuper! Veuillez en choisir un autre... ")
        symbole(joueur_sigle)



    
def estGagnant():

    if tableau[0][0]!=" " and (tableau[0][0]==tableau[0][1] and tableau[0][0]==tableau[0][2]):
        return 1
    elif tableau[1][0]!=" " and (tableau[1][0]==tableau[1][1] and tableau[1][0]==tableau[1][2]):
        return 1
    elif tableau[2][0]!=" " and(tableau[2][0]==tableau[2][1] and tableau[2][0]==tableau[2][2]):
        return 1
    elif tableau[0][0]!=" " and (tableau[0][0]==tableau[1][0] and tableau[0][0]==tableau[2][0]):
        return 1
    elif tableau[0][1]!=" " and (tableau[0][1]==tableau[1][1] and tableau[0][1]==tableau[2][1]):
        return 1
    elif tableau[0][2]!=" " and (tableau[0][2]==tableau[1][2] and tableau[0][2]==tableau[2][2]):
        return 1
    elif tableau[0][0]!=" " and (tableau[0][0]==tableau[1][1] and tableau[0][0]==tableau[2][2]):
        return 1
    elif tableau[0][2]!=" " and (tableau[0][2]==tableau[1][2] and tableau[0][2]==tableau[2][0]):
        return 1
    else:
        return 0



    
def jouer():
    for i in range(4):
        symbole('X')
        if estGagnant():
            print("Bravoo Joueur X vous avez gagner!")
            break
        symbole('O')
        if estGagnant():
            print("Bravoo Joueur O vous avez gagner!")
            break
    else:
        print("Vous etes a egalité!")
        
    

            
jouer()