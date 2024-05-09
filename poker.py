cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')

# map every item in cards to corresponding number 1-14
cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}


# left1 = input(f"Enter your card played: ")
# left2 = input("Enter your card played: ")
# left3 = input("Enter your card played: ")
#
# right1 = input("Enter your card played: ")
# right2 = input("Enter your card played: ")
# right3 = input("Enter your card played: ")

def check_straight(card1, card2, card3):
    player_card = [card1, card2, card3]
    # sort them in order to see if they're consecutive
    player_card.sort()
    for i in range(len(player_card) - 2):
        # check if there are 3 consecutive values
        if (player_card[i] + 1 == player_card[i + 1]) and (player_card[i + 1] + 1 == player_card[i + 2]):
            # return greatest value
            return max(player_card)
        else:
            return 0


def check_3ofa_kinda(card1, card2, card3):
    player_card = [card1, card2, card3]
    # sort them in order to see if they're consecutive
    player_card.sort()
    # check if all 3 are the same
    for i in range(len(player_card) - 2):
        if player_card[i] == player_card[i+1] and player_card[i] == player_card[i+2]:
            # return that number and value
            return player_card[i]
    # return 0
    return 0


def check_royal_flush(card1, card2, card3):
    return_value = check_straight(card1, card2, card3)
    # if value = 14, return 14
    if return_value == 14:
        return 14
    # else return 0
    return 0

# calculate scores of left and right players and evaluate who wins
def play_cards(left1, left2, left3, right1, right2, right3):

    left_check_straight = check_straight(left1, left2, left3)
    right_check_straight = check_straight(right1, right2, right3)

    left_check_straight3 = check_straight(left1, left2, left3)
    right_check_straight3 = check_straight(right1, right2, right3)

    left_check_royal = check_royal_flush(left1, left2, left3)
    right_check_royal = check_royal_flush(right1, right2, right3)

    if left_check_straight and right_check_straight:
        # if left wins, return -1
        if left_check_straight > right_check_straight:
            return -1
        # if neither win, return 0
        elif left_check_straight == right_check_straight:
            return 0
        # if right win, return 1
        else:
            return 0

    # if both play 3 of a kind the higher value wins
    if left_check_straight3 and right_check_straight3:
        # if left wins, return -1
        if left_check_straight3 > right_check_straight3:
            return -1
            # if neither win, return 0
        elif left_check_straight3 == right_check_straight3:
            return 0
            # if right win, return 1
        else:
            return 0

    # if one plays straight and the other has 3 of a kind, straight wins
    if left_check_straight and right_check_straight3:
        return -1
    elif right_check_straight and left_check_straight3:
        return 1
    else:
        return None

   # if one player plays a royal flush and the other doesn’t, the flush wins.
    if left_check_royal and not right_check_royal:
        return -1
    elif right_check_royal and not left_check_royal:
        return 1
    else:
        return None
