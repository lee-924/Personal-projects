import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


print("ODD OR EVEN GAME   - (made by lee) \n")
#---main----
again = "yes"
while again == "yes":

    def bat():
        print("----- YOU ARE BATING -----")
        x= 0
        y = 1
        bsum = 0
        while x != y:
            try:
                
                x = int(input("Enter number (0-6): "))
                if x in [1,2,3,4,5,6]:
                    y = random.randint(0,6)
                    bsum +=x
                elif x == 0:
                    bsum += y
                    print("Computer chose: ", y)
                    print("current runs: ", bsum)
                    continue
                else:
                    print("INVALID! only numbers (0-6) allowed!")
                    continue 

                print("Computer chose: ", y)
                print("current runs: ", bsum)
            except ValueError :
                print("INVALID! only numbers (0-6) allowed!")
                continue

        clear()
        print("computer and user chose ", y)
        print("SAME NUMBER!")
        
        print("------- Total runs scored by user:  ",bsum, " ------- \n")
        rtwoball(bsum)

        

    def ball():
        print("----- YOU ARE BALLING -----")
        blsum = 0
        g = 1
        h = 0
        while g != h:
            try:
                g = int(input("Enter a number (0-6): "))
                if g in [1,2,3,4,5,6]: 
                    h = random.randint(0,6)
                    blsum += h
                    print("computer chose: ", h)
                elif g == 0:
                    blsum += g
                    continue
                else :
                    print("INVALID! only numbers (0-6) allowed!")
                    continue

                

            except ValueError :
                print("INVALID! only numbers (0-6) allowed!")
                continue

        clear()
        print("computer and user chose ", h)
        print("Same number!")
        
        print("-------Total runs scored by computer: ", blsum, "======== \n")
        rtwobat(blsum)
        

    def rtwoball(bsum):
        print("---- YOU ARE BALLING ----")
        sum = 0
        g = 1
        h = 0
        while g != h:
            try:
                
                g = int(input("Enter a number (0-6): "))
                if g in [1,2,3,4,5,6]:
                    h = random.randint(0,6)
                    sum += h
                elif g == 0:
                    sum += h
                    print("User chose :    ", g)
                    print("computer chose: ", h)
                    continue
                else:
                    print("INVALID! only numbers (0-6) allowed!")
                    continue 
            except ValueError:
                print("INVALID! only numbers (0-6) allowed!")
                continue 

            
            print("User chose :    ", g)
            print("computer chose: ", h)
            if sum < bsum: 
                continue
            elif sum > bsum: 
                print("------- 🎇 Computer won 🎇 -------\n")
                break
            else: 
                print("-----🎉🎇🎇 You won 🎇🎇🎉------\n")
            
            print("USER RUNS: ", bsum)
            print("COMPUTER RUNS: ",sum)

    def rtwobat(blsum):
        print("----- YOU ARE BATING -----")
        x= 0
        y = 1
        sum = 0
        while x != y: 
            try:
                
                x = int(input("Enter number (0-6): "))
                if x in [1,2,3,4,5,6]:
                    y = random.randint(0,6)
                    sum +=x
                elif x == 0:
                    sum += x
                    print("Computer chose: ", y)
                    print("current runs: ", sum)
                    continue
                else:
                    print("INVALID! only numbers (0-6) allowed!")
                    continue  

            except ValueError : 
                print("INVALID! only numbers (0-6) allowed!")
                continue


             
            print("Computer chose: ", y)
            print("current runs: ", sum)
            if sum < blsum: 
                continue
            elif sum > blsum: 
                print("------- 🎇 Computer won 🎇 -------\n")
                break
            else: 
                print("-----🎉🎇🎇 You won 🎇🎇🎉------\n")
            
        print("USER RUNS: ", blsum)
        print("COMPUTER RUNS: ",sum)
        


    def user():
        print("CHOOSE WHICH MODE")
        bt = int(input("Enter Bating or Balling (1/2): "))
        if bt == 1:
            print("User chooses bating  \n")
            bat()
        elif bt == 2: 
            print("User chooses balling  \n")
            ball()


    def computer():
        t = random.randint(1,2)
        if t == 1:
            print("Computer chooses bating \n")
            ball()
        elif t == 2: 
            print("Computer chooses balling \n")
            bat()


#First part of the game
    choose = input("Choose odd or even: ")
    oe= int(input("Select a number between 1 and 6: "))


    a = random.randint(0,7)
    print("(user) ", oe,"+", a, " (computer)", "= ", (oe + a))



    if (a + oe) % 2 == 0:
        if choose == "even": 
            print("-- you won -- \n")
            user()
        else :
            print("-- computer won -- \n")
            computer()

    else: 
        if choose == "odd":
            print("-- you won -- \n")
            user()
        else:
            print("-- computer won -- \n")
            computer()

    again = input("\nDo you want to play again (yes/no): ")
