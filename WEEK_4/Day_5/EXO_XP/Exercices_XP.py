def display_board(board):
  # Affichage de la grille Tic Tac Toe avec les positions actuelles des joueurs
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("-----------")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("-----------")
  print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_input(player, board):
  # Demande au joueur de saisir une position pour placer sa marque
  valid_positions = [str(i) for i in range(9) if board[i] == " "]
  position = input(f"Joueur {player}, choisissez une position parmi {valid_positions}: ")
  while position not in valid_positions:
    position = input("Position non valide, veuillez réessayer: ")
  return int(position)

def check_win(board):
  # Vérifie si un joueur a gagné en ayant 3 marques d'affilée
  win_conditions = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
      [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
      [0, 4, 8], [2, 4, 6]  # diagonales
  ]
  for condition in win_conditions:
    if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
      return True
  return False

def play():
  # Fonction principale du jeu Tic Tac Toe
  board = [" " for _ in range(9)]  # Initialisation de la grille avec des espaces vides
  player = "O"  # Le joueur O commence
  game_over = False
  while not game_over:
    display_board(board)  # Affichage de la grille
    position = player_input(player, board)  # Demande de la position au joueur
    board[position] = player  # Mise à jour de la grille avec la marque du joueur
    if check_win(board):  # Vérifie si un joueur a gagné
      game_over = True
      print(f"Le joueur {player} a gagné!")
    elif " " not in board:  # Vérifie s'il y a une égalité
      game_over = True
      print("Match nul!")
    else:  # Pas de gagnant, on passe au joueur suivant
      player = "X" if player == "O" else "O"
  display_board(board)  # Affichage final de la grille

# Appel
display_board(board)
