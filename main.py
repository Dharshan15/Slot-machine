MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        money = input("Deposit the money : ")
        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print(" Please deposit more than 0")
        else :
            print("Deposit invalid")
    return money

def get_lines():
    while True:
        lines = input("Enter the number of lines to bet (1 to "+ str(MAX_LINES) + ") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else :
            print("Enter a number")
    return lines

def get_bet():
    while True:
        money = input("Tell me the bet on each line : ")
        if money.isdigit():
            money = int(money)
            if MIN_BET <= money <= MAX_BET:
                break
            else:
                print(f"Enter a bet between ${MIN_BET} - ${MAX_BET}")
        else :
            print("Enter a number")
    return money

def main():
    balance = deposit()
    lines = get_lines()
    bet = get_bet()

main()

    