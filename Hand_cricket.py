import random

user_score = 0
com_score = 0

# --- TOSS ---
while True:
    user_pick = input("Enter odd/even: ").lower()
    if user_pick not in ["odd", "even"]:
        print("Invalid! Enter odd or even")
    else:
        break
print(f"You chose {user_pick}.")

com_select = random.randint(1, 9)
while True:
    user_select = int(input("Enter one number between 1 to 9: "))
    if user_select not in range(1, 10):
        print("Invalid! Select number between 1 to 9")
    else:
        break

total = com_select + user_select
print(f"Computer chose {com_select}. Total = {total}")

if total % 2 == 0:
    result = "even"
else:
    result = "odd"

# --- FIRST INNINGS ---
if result == user_pick:
    print("You won the toss!")
    while True:
        user_choice = input("Enter batting/bowling: ").lower()
        if user_choice not in ["batting", "bowling"]:
            print("Invalid! Enter batting or bowling")
        else:
            break
    print(f"You chose {user_choice}")

    # User won toss - first innings
    while True:
        while True:
            user_move = int(input("Enter number between 1 to 10: "))
            if user_move not in range(1, 11):
                print("Invalid number")
            else:
                break
        com_move = random.randint(1, 10)
        print(f"Your choice {user_move} and computer choice {com_move}")

        if user_move != com_move:
            print("Still not out")
            if user_choice == "batting":
                user_score += user_move
                print(f"Your score: {user_score}")
            else:
                com_score += com_move
                print(f"Computer score: {com_score}")
        else:
            if user_choice == "batting":
                print("You got out!")
            else:
                print("Computer got out!")
            break

    # --- SECOND INNINGS ---
    if user_choice == "batting":
        target = user_score + 1
        print(f"\nTarget is {target} for computer")
        print("Second innings: Computer batting")
        
        while True:
            while True:
                user_move = int(input("Enter number between 1 to 10: "))
                if user_move not in range(1, 11):
                    print("Invalid number")
                else:
                    break
            com_move = random.randint(1, 10)
            print(f"Your choice {user_move} and computer choice {com_move}")

            if user_move != com_move:
                print("Still not out")
                com_score += com_move
                print(f"Computer score: {com_score}")
                if com_score >= target:
                    print("Computer won!")
                    break
            else:
                print("Computer got out!")
                break
    else:
        target = com_score + 1
        print(f"\nTarget is {target} for you to win")
        print("Second innings: Your batting")
        
        while True:
            while True:
                user_move = int(input("Enter number between 1 to 10: "))
                if user_move not in range(1, 11):
                    print("Invalid number")
                else:
                    break
            com_move = random.randint(1, 10)
            print(f"Your choice {user_move} and computer choice {com_move}")

            if user_move != com_move:
                print("Still not out")
                user_score += user_move
                print(f"Your score: {user_score}")
                if user_score >= target:
                    print("You won!")
                    break
            else:
                print("You got out!")
                break

else:
    # --- COMPUTER WON TOSS ---
    print("You lose the toss!")
    com_choice = random.choice(["batting", "bowling"])
    print(f"Computer chose {com_choice}")

    # First innings - computer chose
    while True:
        while True:
            user_move = int(input("Enter number between 1 to 10: "))
            if user_move not in range(1, 11):
                print("Invalid number")
            else:
                break
        com_move = random.randint(1, 10)
        print(f"Your choice {user_move} and computer choice {com_move}")

        if user_move != com_move:
            print("Still not out")
            if com_choice == "batting":
                com_score += com_move
                print(f"Computer score: {com_score}")
            else:
                user_score += user_move
                print(f"Your score: {user_score}")
        else:
            if com_choice == "batting":
                print("Computer got out!")
            else:
                print("You got out!")
            break

    # --- SECOND INNINGS ---
    if com_choice == "batting":
        target = com_score + 1
        print(f"\nTarget is {target} for you to win")
        print("Second innings: Your batting")
        
        while True:
            while True:
                user_move = int(input("Enter number between 1 to 10: "))
                if user_move not in range(1, 11):
                    print("Invalid number")
                else:
                    break
            com_move = random.randint(1, 10)
            print(f"Your choice {user_move} and computer choice {com_move}")

            if user_move != com_move:
                print("Still not out")
                user_score += user_move
                print(f"Your score: {user_score}")
                if user_score >= target:
                    print("You won!")
                    break
            else:
                print("You got out!")
                break
    else:
        target = user_score + 1
        print(f"\nTarget is {target} for computer")
        print("Second innings: Computer batting")
        
        while True:
            while True:
                user_move = int(input("Enter number between 1 to 10: "))
                if user_move not in range(1, 11):
                    print("Invalid number")
                else:
                    break
            com_move = random.randint(1, 10)
            print(f"Your choice {user_move} and computer choice {com_move}")

            if user_move != com_move:
                print("Still not out")
                com_score += com_move
                print(f"Computer score: {com_score}")
                if com_score >= target:
                    print("Computer won!")
                    break
            else:
                print("Computer got out!")
                break

# --- FINAL RESULT ---
print("\n--- Match Over ---")
print(f"Your score: {user_score}")
print(f"Computer score: {com_score}")

if user_score > com_score:
    print("You won the match! 🏆")
elif com_score > user_score:
    print("Computer won the match!")
else:
    print("It's a tie!")