import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings , winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # current_symbols = all_symbols will be a reference so change will be made to the all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="") 

        print()

def deposit():
    while True:
        money = input("Deposit the money : $")
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

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if(total_bet > balance):
            print(f"You dont have enough money to bet:( , Your balance : {balance}")
        else :
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet : ${lines*bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines : ", *winning_lines) #splat operator is to unpack elements of a list, set, tuple etc

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is : ${balance}")
        answer = input("Press enter to play (q to quin).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

    

main()

    