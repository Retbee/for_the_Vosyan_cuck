import random

num_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def scores(player_lst, pc_lst):
    plyer_sum = sum_of_cards(player_lst)
    pc_sum = sum_of_cards(pc_lst)

    print(f"Your final hand: {player_lst}, final score: {player_sum}")
    print(f"Computer's final hand: {pc_lst}, final score: {pc_sum}")

    if pc_sum == plyer_sum:
        print("It's a draw")
    elif pc_sum > plyer_sum:
        print("Computer wins!")
    else:
        print("Player wins!")

def overkeeping(player_lst, pc_lst):
    # 21 Выделить в отдельную константу
    player_over = sum_of_cards(player_lst) > 21
    pc_over = sum_of_cards(pc_lst) > 21

    if player_over or pc_over:
        scores(player_lst, pc_lst)
        if player_over and not pc_over:
            print("Computer wins!")
        elif pc_over and not player_over:
            print("Player wins!")
        else:
            print("Both lost!")
        return True
    return False


def adding_card(lst):
    card = random.choice(num_list)
    dealtCardIs11 = card == 11
    isExist11Card = (11 in lst and dealtCardIs11)

    # Сложные bool вычиления выделяют в отдельную переменную
    if isExist11Card or (sum_of_cards(lst) + card > 21 and dealtCardIs11):
        lst.append(1)
    else:
        lst.append(card)

    return lst


def sum_of_cards(lst):
    return sum(lst)

def keep_playing():
    pc_cards = random.choices(num_list, k=2)
    player_cards = random.choices(num_list, k=2)

    still_playing = True

    greeting = input("Welcome to the Blackjack game. Do you wanna play? Type 'y' or 'n': ")

    view = ConsolePrint()

    if greeting == "y":
        while still_playing:
            # Много лишних вызовов. Можно сохранить результат и переиспользовать
            print(f"Your cards is {player_cards}. Your score is: {sum_of_cards(player_cards)}")
            print(f"Computer's first card: {pc_cards[0]}.")

            get_cards = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_cards == 'n':
                while sum_of_cards(pc_cards) < 17: # Выделить в отдельную константу
                    adding_card(lst=pc_cards)

                scores(player_lst=player_cards, pc_lst=pc_cards)
                still_playing = False
                keep_playing()
            else:
                if sum_of_cards(pc_cards) >= 17:
                    adding_card(lst=player_cards)
                else:
                    player_cards, pc_cards = adding_card(lst=player_cards), adding_card(lst=pc_cards)

                if overkeeping(player_lst=player_cards, pc_lst=pc_cards):
                    still_playing = False
                    keep_playing()
    else:
        return print("Thanks for playing! Until next time, farewell!")


keep_playing()
