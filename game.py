print("Made by Niveditha N \n Visit https://github.com/WCoder007/Rock-Paper-Scissors for more info ")
lose = ("Sorry, The Computer Won")
win  = ("congratulations, You Won")
lives = 3 
computer_lives = 5 
score = 0
draw = 0
while(True):
    print("To start, fill in the following details")
    username = input("Enter your Username : ")
    password = input("Enter your Password : ") # I am directly taking the password, use getpass for better security
    search = open("Users.csv","r")
    for line in search:
        if username and password in line:
            print("Access Granted")
            start_menu = """
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
 
***********************************************************LOGO HERE******************************************************************

------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
Game Rules:
You start with 3 lives.
If you win you get a extra life.
If you loose you loose a life.
If you draw the lives stay the same.
-----------------------------------------
To see a list of rules type rules.
-----------------------------------------
At any point type exit to leave the game.
-----------------------------------------
The computer has lives as well.
Think you can beat the computer with your luck?
Good Luck!
It's Game On!
-----------------------------------------
"""



