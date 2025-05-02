import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


print("ROCK PAPER SCISSOR GAME  - (made by lee) \n")

# MAIN PROGRAM

ag = "yes"
while ag == "yes": 
    def comp():
        r = random.randint(0,2)
        return r

    ask = int(input("Enter how many rounds you wanna play: "))

    print("Game set to : \n", "--  Best of", ask, "-- \n")

    print("\n Enter any one of the following \n Enter 0: ROCK \n Enter 1: SCISSOR \n Enter 2: PAPER \n")
            

    def game(): 
        pl = 0
        cl = 0
        dict = {0: "rock", 1: "scissor", 2: "paper"}
        for i in range(1,ask+1):
            print("-- Round", i, "begins -- \n")
            
            try:
                ur = int(input("Enter your choice: "))
                if ur not in [0, 1, 2]:
                    print("Invalid number! Please enter 0, 1, or 2.\n")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.\n")
                continue

            cp = comp()
            print("\n" , "(user)", dict[ur], ":" , dict[cp], "(computer)")

            if ur== cp: 
                print("-- Its a Draw -- \n \n")
            elif ur== 0 :
                if cp== 1 :
                    print("-- USER WINS -- \n \n")
                    pl += 1
                else :
                    print("-- COMPUTER WINS -- \n \n")
                    cl += 1
            elif ur== 1:
                if cp== 2:
                    print("-- COMPUTER WINS -- \n \n")
                    cl += 1
                else: 
                    print("-- USER WINS -- \n \n ")
                    pl += 1
            elif ur == 2:
                if cp== 0:
                    print("-- USER WINS -- \n \n")
                    pl += 1
                else :
                    print("-- COMPUTER WINS -- \n \n")
                    cl += 1
            
        return cl,pl


    def win(cop,pop): 
        print("------ FINAL RESULT ------ \n")
        print("Score: \n","user: " ,pop , "\n Computer: ", cop)
        if pop > cop :
            print("===== USER WINS =====")
        elif cop == pop :
            print("===== DRAW =====")
        else :
            print("===== COMPUTER WINS =====")


    cop,pop = game()
    clear()
    win(cop,pop)
    ag = input("Play again? \n yes/no : ")
    clear()

