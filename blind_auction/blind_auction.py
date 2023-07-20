import os


def clear_command_history():
    os.system("history -c")


print("Welcome to the secret auction program")
participant = {}
is_participant = False
winner_statement = ""


def auction_participant(participant_name, participant_bid):
    participant[participant_name] = participant_bid


while not is_participant:
    name = input("What is your name: ")
    bid = int(input("What's your bid: $"))
    auction_participant(participant_name=name, participant_bid=bid)
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ")
    print(participant)
    maximum = max(participant, key=participant.get)

    if continue_bid == "no":
        is_participant = True
        print(f"Congratulations to {maximum} with bid ${participant[maximum]}")
