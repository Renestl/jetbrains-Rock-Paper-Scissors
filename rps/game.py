import random

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

option = {'rock': {'rock': 'Draw',
                   'paper': 'Lose',
                   'scissors': 'Win'},
          'paper': {'rock': 'Win',
                    'paper': 'Draw',
                    'scissors': 'Lose'},
          'scissors': {'rock': 'Lose',
                       'paper': 'Win',
                       'scissors': 'Draw'}
          }

user_option = input()


while True:
    if user_option != '!exit' and user_option not in list(option):
        print('Invalid input')
        user_option = input()
    elif user_option == "!exit":
        print("Bye")
        break
    else:
        comp_option, output = random.choice(list(option[user_option].items()))

        outcome = {'Lose': f'Sorry, but the computer chose {comp_option}',
                   'Draw': 'There is a draw ({})'.format(comp_option),
                   'Win': 'Well done. The computer chose {} and failed'.format(comp_option)
                   }

        print(outcome[output])

        user_option = input()
