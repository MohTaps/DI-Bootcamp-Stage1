def ordonner(mots):
  
  mots = [mot.strip() for mot in mots.split(',')]
    
  
  mots.sort()
  
  
  mots_ordonner = ','.join(mots)
  
  return mots_ordonner


mots = input('\nVeuillez saisir les differents mots que vous separerez avec une virgule svp: ')


mots_ordonner = ordonner(mots)

print(f'\n\tVoici les mots ordonner: {mots_ordonner}')

'''def trier_mots(mots):
  
  mots = [mot.strip() for mot in mots.split(',')]
  
  
  mots.sort()
  
 
  mots_tries = ','.join(mots)
  
  return mots_tries


mots = input('Saisissez une séquence de mots séparés par des virgules: ')


mots_tries = trier_mots(mots)
print(f'Voici les mots triés: {mots_tries}')'''

