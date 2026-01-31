import day9art
print(day9art.logo)

def find_winner(auction_dict):
    winner = ""
    highest_bid = 0
    for key in auction_dict:
        if auction_dict[key] > highest_bid:
            winner = key
            highest_bid = auction_dict[key]
    print(f"The winner is {winner} with a bid of {highest_bid}")


auction_dict = {}
again = "yes"

while again == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    auction_dict[name] = bid

    again = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if again == "yes":
        print("\n" * 50)
    else:
        find_winner(auction_dict)