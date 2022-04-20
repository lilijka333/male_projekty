from random import randint
from math import sqrt
GAME_WIDTH = 10
GAME_HEIGH = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGH)
player_x = randint(0, GAME_WIDTH)
player_y = randint(0, GAME_HEIGH)
player_found_key = False
steps = 0
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)


while not player_found_key:

    print()
    print("Możesz udac sie w kierunkach okreslonych jako [W/A/S/D]")
    move = input('Dokąd idziesz? ')
    steps += 1

    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGH:
                print("Auć uderzasz w ścianę")
                player_y = GAME_HEIGH

        case 's':
            player_y -= 1
            if player_y < 0:
                print("Auć uderzasz w ścianę")
                player_y = 0

        case 'a':
            player_x -= 1
            if player_x < 0:
                print("Auć uderzasz w ścianę")
                player_x = 0

        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print("Auć uderzasz w ścianę")
                player_x = GAME_WIDTH

        case 'q':
            print('Koniec gry')
            quit()

        case '_':
            print('Nie wiem dokąd idziesz...')
            continue

    if player_x == key_x and player_y == key_y:
        print('Brawo wygrałeś!!!')
        print(f'Potrzebowałeś {steps} kroków')
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_after_move < distance_before_move:
        print('Cieplej')
    else:
        print("zimno")

    distance_before_move = distance_after_move
