import random
print("Welcome to the game of rock paper scissors")
option=["rock","paper","scissors"]
score=0
while True:
    user_input=input("Enter rock/paper/scissors or q to quit: ")
    if user_input=="q":
        break
    if user_input not in option:
        continue
    random_num=random.randint(0,2)
    computer_choice=option[random_num]
    print("computer picks",computer_choice)
    if user_input=="rock" and computer_choice=="scissors":
        print("you won")
        score=score+1
    elif user_input=='paper' and computer_choice=='rock':
         print("you won")
         score=score+1
    elif user_input=='scissors' and computer_choice=='paper':
         print("you won")
         score=score+1
    elif user_input==computer_choice:
        print("tie")
    else:
        print("you lost")
print("you won",score,"times")

        
        