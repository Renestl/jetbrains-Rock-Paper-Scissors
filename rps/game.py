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


def read_ratings(player_name):
    ratings_file = open('rating.txt', 'r')
    ratings_dict = {}

    for line in ratings_file:
        name, rating = line.split()
        ratings_dict[name] = int(rating)

    if player_name in ratings_dict:
        ratings_file.close()
        return ratings_dict[player_name]
    else:
        ratings_file.close()
        return 0


def greet_player(name):
    print(f'Hello, {name}')


def game():
    #  Greet user and get previous score, if available
    user_name = input('Enter your name: ')
    greet_player(user_name)
    rating = read_ratings(user_name)

    user_option = input()

    while True:
        if user_option != '!exit' and user_option != '!rating' and user_option not in list(option):
            print('Invalid input')
            user_option = input()
        elif user_option == "!exit":
            print("Bye")
            break
        else:
            if user_option == '!rating':
                print(f'Your rating: {rating}')
            else:
                comp_option, output = random.choice(list(option[user_option].items()))

                outcome = {'Lose': {'result': f'Sorry, but the computer chose {comp_option}',
                                    'points': 0},
                           'Draw': {'result': 'There is a draw ({})'.format(comp_option),
                                    'points': 50},
                           'Win': {'result': 'Well done. The computer chose {} and failed'.format(comp_option),
                                   'points': 100}
                           }

                game_result = outcome[output].get('result')
                game_points = outcome[output].get('points')

                print(game_result)

                rating += game_points

            user_option = input()


game()
