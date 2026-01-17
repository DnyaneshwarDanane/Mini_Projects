import random
choices = ["rock" , "paper" ,"scissor"]

print("------Welcome to Rock Scissor paper Game-------")
 
while True:
    user = input("Ener your choice RPS (or 'exit' to exit) : ").lower().strip()


    if user == "exit":
        print(" your are exit from game")
        break
    if user not in choices:
        print("invalid input!,try again")
    
    computer = random.choice(choices)
    print("print comper choice : ",computer)

    if computer == user:
        print("your are tie")

    elif ((user == "rock" and computer == "scissor")
          or
          (user == "scissor" and computer == "paper") 
          or
          (user == "paper" and computer =="rock")):
        
        print("you win!")

    else:
        print("compter win")

