import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

#---main----
again = "yes"
while again == "yes":

    def bat():
        print("----- YOU ARE BATING -----")
        x= 0
        y = 1
        bsum = 0
        while x != y: 
            x = int(input("Enter number (0-6): "))
            y = random.randint(0,6)
            bsum +=x 
            print("Computer chose: ", y)
            print("current runs: ", bsum)

        print("SAME NUMBER, GAME OVER")
        print("------- Total runs:  ",bsum, " -------")
        rtwoball(bsum)

        

    def ball():
        print("----- YOU ARE BALLING -----")
        blsum = 0
        g = 1
        h = 0
        while g != h:
            g = int(input("Enter a number (0-6): "))
            h = random.randint(0,6)
            blsum += h
            print("computer chose: ", h)

    
        print("Same number!")
        print("-------Total runs scored by computer: ", blsum, "========")
        rtwobat(blsum)
        

    def rtwoball(bsum):
        print("---- YOU ARE BALLING ----")
        sum = 0
        g = 1
        h = 0
        while g != h: 
            g = int(input("Enter a number (0-6): "))
            h = random.randint(0,6)
            sum += h
            print("User chose     :", g)
            print("computer chose: ", h)
            if sum < bsum: 
                continue
            elif sum > bsum: 
                print("computer won")
                break
        else: 
            print("-----You won------")
        
        print("USER RUNS: ", bsum)
        print("COMPUTER RUNS: ",sum)

    def rtwobat(blsum):
        print("----- YOU ARE BATING -----")
        x= 0
        y = 1
        sum = 0
        while x != y: 
            x = int(input("Enter number (0-6): "))
            y = random.randint(0,6)
            sum +=x 
            print("Computer chose: ", y)
            print("current runs: ", sum)
            if sum < blsum: 
                continue
            elif sum > blsum: 
                print("computer won")
                break
        else: 
            print("-----You won------")
        
        print("USER RUNS: ", blsum)
        print("COMPUTER RUNS: ",sum)
        
        

                    
        
        
        



    def user():
        print("CHOOSE WHICH MODE")
        bt = int(input("Enter bat/ball (1/2): "))
        if bt == 1:
            print("User chooses bating")
            bat()
        elif bt == 2: 
            print("User chooses balling")
            ball()


    def computer():
        print("Please choose a number: ")
        t = random.randint(1,2)
        if t == 1:
            print("Computer chooses bating")
            ball()
        elif t == 2: 
            print("Computer chooses balling")
            bat()



    choose = input("Enter odd or even: ")
    oe= int(input("Enter a number between 1 and 6: "))


    a = random.randint(0,7)
    print("computer chose: ", a)





    if (a + oe) % 2 == 0:
        if choose == "even": 
            print("i win")
            user()
        else :
            print("computer wins")
            computer()

    else: 
        if choose == "odd":
            print("i win")
            user()
        else:
            print("computer wins")
            computer()

    again = input("Do you want to play again (yes/no): ")


