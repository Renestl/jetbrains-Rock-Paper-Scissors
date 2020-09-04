import random

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

# default_option = {'rock': {'rock': 'Draw',
#                            'paper': 'Lose',
#                            'scissors': 'Win'},
#                   'paper': {'rock': 'Win',
#                             'paper': 'Draw',
#                             'scissors': 'Lose'},
#                   'scissors': {'rock': 'Lose',
#                                'paper': 'Win',
#                                'scissors': 'Draw'}
#                   }

winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
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


def get_options():
    default_options = ['rock', 'paper', 'scissors']
    options = input().split(",")

    if len(options) < 3:
        return default_options
    else:
        return options


def game():
    #  Greet user and get previous score, if available
    user_name = input('Enter your name: ')
    greet_player(user_name)
    rating = read_ratings(user_name)

    game_options = get_options()

    print("Okay, let's start")

    user_option = input()

    while True:
        if user_option != '!exit' and user_option != '!rating' and user_option not in list(game_options):
            print('Invalid input')
            user_option = input()
        elif user_option == "!exit":
            print("Bye")
            break
        else:
            if user_option == '!rating':
                print(f'Your rating: {rating}')
            else:
                # comp_option, output = random.choice(list(default_option[user_option].items()))
                comp_option = random.choice(list(game_options))

                outcome = {'Lose': {'result': f'Sorry, but the computer chose {comp_option}',
                                    'points': 0},
                           'Draw': {'result': 'There is a draw ({})'.format(comp_option),
                                    'points': 50},
                           'Win': {'result': 'Well done. The computer chose {} and failed'.format(comp_option),
                                   'points': 100}
                           }

                if user_option == comp_option:
                    game_result = outcome['Draw'].get('result')
                    game_points = outcome['Draw'].get('points')
                    print(game_result)
                    rating += game_points
                elif comp_option in list(winning_cases[user_option]):
                    game_result = outcome['Win'].get('result')
                    game_points = outcome['Win'].get('points')
                    print(game_result)
                    rating += game_points
                else:
                    game_result = outcome['Lose'].get('result')
                    print(game_result)

                # game_result = outcome[output].get('result')
                # game_points = outcome[output].get('points')

                # rating += game_points

            user_option = input()


game()
