import random
game = ["rock", "paper", "scissors"]
secret = random.choice(game)
while True:
    user_choice = input("Enter your choice (rock/ paper/scissors): ").lower()
    if user_choice not in game:
	    print("Invalid choice! Please choose rock, paper or scissors")
    else:
	    break
print("Computer choice is", secret, "and yours choice is", user_choice)

if user_choice == secret:
	print("Tie!")
elif user_choice=="rock" and secret=="scissors":
	print("You win!")
elif user_choice=="paper" and secret=="rock":
	print("You win!")
elif user_choice=="scissors" and secret=="paper":
	print("You win!")
else:
	print("Oops! You lose")
