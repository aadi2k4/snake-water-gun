import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,0,-1])
younum = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake",-1: "water",0: "gun"}
you = youDict[younum]
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
    print("Match is draw!")
else:
    '''
    if(computer == -1 and you == 1): #-2(computer-you)
        print("You Win!")
    elif(computer == -1 and you == 0): #-1
        print("You Lose!")
    elif(computer == 1 and you == -1): #2
        print("You Lose!")
    elif(computer == 1 and you == 0): #1
        print("You Win!")
    elif(computer == 0 and you == -1): #1
        print("You Win!")
    elif(computer == 0 and you == 1): #-1
        print("You Lose!")

    The below value is written on the basis of the value of computer - you
    '''
    if((computer-you)==-1 or (computer-you)== 2):
        print("You Lose!")
    else:
        print("You Win!")