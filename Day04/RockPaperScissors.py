rock = "rock"
paper = "paper"
scissors = "scissors"

user_Choice = input("Enter your choice (rock, paper, scissors): ").lower()
import random
choices = [rock, paper, scissors]
computer_Choice = random.choice(choices)
print(f"Computer chose: {computer_Choice}")
if user_Choice == computer_Choice:
    print("It's a tie!")
elif (user_Choice == rock and computer_Choice == scissors) or \
     (user_Choice == paper and computer_Choice == rock) or \
     (user_Choice == scissors and computer_Choice == paper):
    print("You win!")
else:    print("Computer wins!")