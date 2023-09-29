import random as rm

def choose_option():
    options = ('Piedra', 'Papel', 'Tijera')
    user_option = input('Piedra, Papel o Tijera ==> ').capitalize()

    if user_option not in options:
      print('Esta opcion no es valida!!')
      # continue 
      return None, None
      
    computer_option = rm.choice(options)
    
    print('User option ==>', user_option)
    print('Computer option ==>', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins ):
  if user_option == computer_option:
    print('Es un empate!!')
  elif user_option == 'Piedra':
    if computer_option == 'Tijera':
      print('Piedra gana a Tijera')
      print('User gana!!')
      user_wins += 1
    else:
      print('Papel gana a Piedra')
      print('Computer gana!💻💻💻')
      computer_wins += 1
  elif user_option == 'Papel':
    if computer_option == 'Piedra':
      print('Papel gana a Piedra')
      print('User gana!!')
      user_wins += 1
    else:
      print('Tijera gana a Papel')
      print('Computer gano!!')
      computer_wins += 1
  elif user_option == 'Tijera':
    if computer_option == 'Papel':
      print('Tijera gana a Papel')
      print('User gana!!!')
      user_wins += 1
    else:
        print('Piedra gana a Tijera')
        print('Computer gana !!!')
        computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:
    
      print('*' * 10)
      print('ROUND', rounds)
      print('*' * 10)
  
      print('Score ==> Computer ', computer_wins)
      print('Score ==> User', user_wins)
      rounds += 1  
  
      user_option, computer_option = choose_option()
      user_wins, computer_wins = check_rules(user_option, computer_option,       user_wins, computer_wins)
    
      
      
      if computer_wins == 2:
        print('El rotundo ganador es la computadora')
        break
  
      
      if user_wins == 2:
        print('El rotundo ganador es el usuario')
        break

run_game()