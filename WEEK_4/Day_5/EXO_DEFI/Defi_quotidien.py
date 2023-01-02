def ordonner(mots):
  
  mots = [mot.strip() for mot in mots.split(',')]
    
  
  mots.sort()
  
  
  mots_ordonner = ','.join(mots)
  
  return mots_ordonner


mots = input('\nVeuillez saisir les differents mots que vous separerez avec une virgule svp: ')


mots_ordonner = ordonner(mots)

print(f'\n\tVoici les mots ordonner: {mots_ordonner}')
