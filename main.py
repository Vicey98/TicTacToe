import itertools


def win(game, current_player):
    def all_same(line):
        if line[0] == line[1] == line[2] and line[0] != 0:
            return True
        else:
            return False

    #horizontal
    for row in game:
        if all_same(row):
            print("Horizontal Win. Player {} Win!".format(current_player))
            return True
    #vertical
    for i in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[i])
        if all_same(check):
            print("Vertical Win. Player {} Win!".format(current_player))
            return True
    # diagonal '\'
    diag_check = []
    for i in range(len(game[0])):
        diag_check.append(game[i][i])
    if all_same(diag_check):
        print("Diagonal Win. Player {} Win!".format(current_player))
        return True
    # diagonal '/'
    rev_diag = [row[-i-1] for i, row in enumerate(game)]
    if all_same(rev_diag):
        print("Diagonal Win. Player {} Win!".format(current_player))
        return True
    # game tie



def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("Spot already taken")
            return False
        else:
            game_map[row][column] = player
        print("   0  1  2")
        for count, col in enumerate(game_map):
            print(count, col)
        return True
    except IndexError:
        print("Out of bounds")
        return False
    except:
        print('Try Again')
        return False


def main():
    play = True
    players = [1,2]

    while play:
        game = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        player_cycle = itertools.cycle([1,2])
        game_board(game, just_display=True)
        game_won = False
        while not game_won:
            current_player = next(player_cycle)
            played = False
            while not played:
                print('Current Player: {}'.format(current_player))
                row_choice = int(input('What row? '))
                column_choice = int(input('What column? '))
                played = game_board(game, current_player, row_choice, column_choice)
                print("----------------")
                if not any(0 in row for row in game):
                    print("It's a tie!")
                    played = True
            if win(game, current_player):
                game_won = True
        user_restart = input("Another round? y/n")
        if user_restart == 'y':
            print("Next Round!")
        elif user_restart == 'n':
            print("Later bo")
            play = False
        else:
            print("Invalid lemme yeet outta here")
            play = False





if __name__ == '__main__':
    main()
