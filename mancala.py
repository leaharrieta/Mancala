"""
File: mancala.py
Author: Leah Arrieta
Date: 11.03.2023
E-mail: leaha3@umbc.edu
Description: The purpose of this program is to play a game of Mancala.
"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
NUM_CUPS = 6


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be
        of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be lists of strings.  Each string should be BLOCK_WIDTH in length, and each list
        should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least
    BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least
    BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def get_player(player_one, player_two):
    """
    A function to store the players names
    :param player_one: the first players name
    :param player_two: the second players name
    """
    return player_one, player_two


def run_game():
    """
    A function to run the game with helper functions
    """
    player_1 = input('Player 1 please tell me your name: ')
    player_2 = input('Player 2 please tell me your name: ')
    get_player(player_1, player_2)

    all_cells = []
    cup_count = 4
    mancala_count_1 = 0
    mancala_count_2 = 0
    game_over = True

    for i in range(12):
        current_cell = []
        if 0 <= i < 6:
            current_cell.append(f"Cup {i + 1} ")
        else:
            current_cell.append(f"Cup {i + 2} ")
        for j in range(BLOCK_HEIGHT - 1):
            # 'stones' to be a space below 'cups'
            if j == (BLOCK_HEIGHT - 4):
                current_cell.append("Stones")
            elif j == (BLOCK_HEIGHT - 3):
                current_cell.append(f"{cup_count}")
            else:
                current_cell.append(" " * BLOCK_WIDTH)

        all_cells.append(current_cell)

    top_rows = all_cells[0:NUM_CUPS]
    bottom_rows = all_cells[::-1]

    first_mancala = []
    second_mancala = []
    for i in range(BLOCK_HEIGHT * 2 + 1):
        if i == (BLOCK_HEIGHT - 2):
            first_mancala.append(f"{player_1} ")
            second_mancala.append(f"{player_2} ")
        elif i == (BLOCK_HEIGHT + 2):
            first_mancala.append("Stones")
            second_mancala.append("Stones")
        elif i == (BLOCK_HEIGHT + 3):
            first_mancala.append(f'{mancala_count_1}')
            second_mancala.append(f'{mancala_count_2}')
        else:
            first_mancala.append(" " * BLOCK_WIDTH)
            second_mancala.append(" " * BLOCK_WIDTH)

    stone_count_list = []
    stone_count_list.append(first_mancala[8])
    stone_count_list.append(top_rows[0][3])
    stone_count_list.append(top_rows[1][3])
    stone_count_list.append(top_rows[2][3])
    stone_count_list.append(top_rows[3][3])
    stone_count_list.append(top_rows[4][3])
    stone_count_list.append(top_rows[5][3])
    stone_count_list.append(second_mancala[8])
    stone_count_list.append(bottom_rows[6][3])
    stone_count_list.append(bottom_rows[7][3])
    stone_count_list.append(bottom_rows[8][3])
    stone_count_list.append(bottom_rows[9][3])
    stone_count_list.append(bottom_rows[10][3])
    stone_count_list.append(bottom_rows[11][3])

    draw_board(top_rows, bottom_rows, first_mancala, second_mancala)
    player_turn(player_1, player_2, stone_count_list, top_rows, bottom_rows, first_mancala, second_mancala)


def winner(is_game_over, player_one_score, player_two_score, stone_list):
    """
    A function to determine the winner of the game
    :param is_game_over: a boolean, when equal to False will terminate the game
    :param player_one_score: the stone count of player one mancala at index 0
    :param player_two_score: the stone count of player two mancala at index 7
    :param stone_list: the list of all stone values
    """
    # check cups 1-6
    for i in range(1, 7):
        if stone_list[i] == '0':
            is_game_over = False
    # check cups 8-13
    for i in range(8, 14):
        if stone_list[i] == '0':
            is_game_over = False

    # compares the value of the two players mancala and determines the winner based off of the higher value
    if not is_game_over:
        if player_one_score > player_two_score:
            print(f'{player_one} is the winner!')
        elif player_one_score < player_two_score:
            print(f'{player_one} is the winner!')


def player_turn(player_one, player_two, stone_count_list, top_rows, bottom_rows, first_mancala, second_mancala):
    """
    A function to have the players take turns
    :param player_one: player 1, represented by a value of 0
    :param player_two: player 2, represented by a value of 1
    :param stone_count_list: a list containing all board stone values
    :param top_rows: the top row of the game board, cups 1-6
    :param bottom_rows: the bottom row of the game board, cups 8-13
    :param first_mancala: the first players mancala, index 0
    :param second_mancala: the second players mancala, index 7
    """

    players = [player_one, player_two]
    current_player = 0
    game_over = True
    mancala_1_stones = stone_count_list[0]
    mancala_2_stones = stone_count_list[7]
    while game_over:
        player_move = int(input(f'{players[current_player]} what cup do you want to move? '))
        # checks the user enters a cup number in the range 1-13
        while player_move < 1 or player_move > 13:
            print('That cup number is invalid. Please enter another 1-13')
            player_move = int(input(f'{players[current_player]} what cup do you want to move? '))

        check_cup(player_move, current_player, players, stone_count_list)
        update_board(top_rows, bottom_rows, stone_count_list)
        winner(game_over, mancala_1_stones, mancala_2_stones, stone_count_list)
        draw_board(top_rows, bottom_rows, first_mancala, second_mancala)

        current_player = 1 - current_player


def check_last_cup(end_cup, stone_count_list):
    """
    A function to give the player another turn if their last stone landed in a mancala
    :param end_cup: the last index a stone landed in
    :param stone_count_list: the list of all cup stone values
    """
    end_cup = last_cup
    if end_cup == stone_count_list[0] or end_cup == stone_count_list[7]:
        print('Your last stone landed in a mancala. Go again!')
        player_cup_move = int(input(f'{player_names[player_turn]} what cup do you want to move? '))


def check_cup(player_cup_move, player_turn, player_names, stone_count_list):
    """
    A function to check if the user inputs a valid cup number and that the selected cup is not empty
    :param player_cup_move: the cup the user entered to move the stones from
    :param player_turn: 0 or 1, represents if the turn is for player 1 or player 2
    :param player_names: the list that contains the players names
    :param stone_count_list: the list that contains the value of all stones of the board
    """
    cup_index = player_cup_move

    # checks the cup the user selects is not empty
    while stone_count_list[cup_index] == '0':
        print('This cup is empty. Please choose another.')
        player_cup_move = int(input(f'{player_names[player_turn]} what cup do you want to move? '))
        cup_index = player_cup_move

    # subtracts all stones from the cup the user selected and distributes them in a clockwise direction
    if stone_count_list[cup_index] != '0':
        new_cup_count = int(stone_count_list[cup_index])
        stone_count = new_cup_count - new_cup_count
        stone_count_list[cup_index] = str(stone_count)
        # adds one stone in a clockwise direction, from new_cup_count value
        for i in range(1, new_cup_count + 1):
            next_cup_index = (cup_index + i) % len(stone_count_list)
            new_stone_count = int(stone_count_list[next_cup_index]) + 1
            stone_count_list[next_cup_index] = str(new_stone_count)

        # this is where i would call check_last_cup function buttt it's giving error so i commented out
        # last_cup = stone_count_list[new_cup_count]
        # check_last_cup(last_cup, stone_count_list)


def update_board(top_row, bottom_row, stone_list):
    """
    A function to update the stone values on the board
    :param top_row: updates the top row values, cups 1-6
    :param bottom_row: updates the bottom row values, cups 8-13
    :param stone_list: the list of all stone values for the board
    :return:
    """
    top_stones = stone_list[1:7]
    for i in range(len(top_stones)):
        top_row[i][3] = str(top_stones[i])

    bottom_stones = stone_list[13:7:-1]
    for i in range(len(bottom_stones)):
         bottom_row[i][3] = str(bottom_stones[i])

    # i can't get the mancala to reflect the updated stone value so
    # this print shows the calculation is being done, it's just not displaying
    # print(stone_list)


if __name__ == "__main__":
    run_game()
