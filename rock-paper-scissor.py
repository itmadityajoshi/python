import random

user = input("Enter your choice (rock, paper, scissor) \n")

computer = ['rock', 'paper','scissor']
c_user = random.choice(computer)


# print(f"your choice {user}, computer choice {c_user}")
if (user == c_user):
    print(f"Your Both Choose {user}. and It's Tie!")
elif(user == "rock" and c_user == "scissor" ):
    print("You win")
elif( user == "paper" and c_user == "rock"):
    print("You win")
elif( user == "scissor" and c_user == "paper"):
    print("You win")
else:
    print(f"Computer win and computer choose {c_user}")


