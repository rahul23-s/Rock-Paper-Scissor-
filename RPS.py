import random

CPU=0
player=0
Draws=0
print("---------ROCK PAPER SCISSOR---------\n\nOne with More wins out of 10 Games will be The WINNER\n")
print("ENTER YOUR NAME:",end="")
name=input()

i=0
while(i<10):
    options= ["Rock","Paper","Scissor"]
    comp_choice= random.choice(options)

    user_choice= input("\nCHOOSE\nRock(r) Paper(p) Scissor(s):\n")
    user_choice=user_choice.capitalize()
    print("\nComputer Chose:",comp_choice)
    if comp_choice=="Rock" and user_choice=="R":
        print("DRAW")
        Draws=Draws+1
        i=i+1
    elif comp_choice=="Rock" and user_choice=="P":
        print(name,"WINS")
        player=player+1
        i=i+1
    elif comp_choice=="Rock" and user_choice=="S":
        print("CPU WINS")
        CPU=CPU+1
        i=i+1    
    elif comp_choice=="Paper" and user_choice=="R":
        print("CPU WINS")
        CPU=CPU+1 
        i=i+1       
    elif comp_choice=="Paper" and user_choice=="P":
        print("DRAW")
        Draws=Draws+1
        i=i+1    
    elif comp_choice=="Paper" and user_choice=="S":
        print(name,"WINS")
        player=player+1 
        i=i+1   
    elif comp_choice=="Scissor" and user_choice=="R":
        print(name,"WINS")
        player=player+1
        i=i+1    
    elif comp_choice=="Scissor" and user_choice=="P":
        print("CPU WINS")
        CPU=CPU+1 
        i=i+1    
    elif comp_choice=="Scissor" and user_choice=="S":
        print("DRAW")
        Draws=Draws+1
        i=i+1
    else :
        print("Invalid Entry ! Choose Again" )
    

print(name,":",player)
print("CPU:",CPU)
print("DRAWS:",Draws)
if player>CPU:
    print("!!!!!!!!",name,"WINS!!!!!!!!")
elif CPU>player:
    print("!!!!!!!!CPU WINS!!!!!!!!")
elif CPU==player:
    print("!!!!!!!!GAME DRAWS!!!!!!!!")    
        