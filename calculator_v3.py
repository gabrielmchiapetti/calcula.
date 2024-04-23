#-# Free and open source calculator, DO NOT SELL OR MAKE PROFIT ON THIS PROJECT

#-# Originally made by Chasmín (Gabriel M. Chiapetti)
# Feel free to change!

# This program is recommended to run on a terminal (MSDOS, linux console or similar)

#####################################################

import time # P.s: if deleted will (kinda of) break the whole code (until all the time derivables are gone)

#####################################################

equationlist = ["*", "/", "+", "null"]  # »»»»» Not really used until now, maybe used in future updates «««««

#####################################################

print("                                                                ")

print("     XXXXX   XXXXX  X     XXXXX  X    X  X       XXXXX        V3") # Ascii title art, feel free to make it cooler :D
print("     X      X    X  X     X      X    X  X      X    X          ")
print("     X      X****X  X     X      X    X  X      X****X          ")
print("     X      X    X  X     X      X    X  X      X    X   0O0    ")
print("     XXXXX  X    X  XXXXX XXXXX  XXXXXX  XXXXX  X    X   O0O    ")
print(" ")

time.sleep(1.2)
print(" ________________________________________________________________ ")
print("|WORK IN PROGRESS - Type 4 for more infomation! -VRS: 3.2.8_a 132|")
print(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

print(" ")

time.sleep(1)

print("What you want to do? ")
time.sleep(1)
print(" ")
print("1 - Calculate") # Will print the options!
print("2 - Details")   # Will show details
print("3 - Quit")
select = int(input("?: "))  # Will detect what select input to work on [you can change for an string data type for text selection]

if select == 1:    # If select = 1 then:

    numberone = int(input("Number 1: "))  # Number one input
    numbertwo = int(input("Number 2: "))  # Number two input

    equation = str(input("What equation? |*|/|+|-|"))  # Will detect what equation to work on

    if equation == "*" or "x" or "X" or "multiplication" or "multiply":
        print("The result is:")
        time.sleep(1)
        print(numberone * numbertwo)

    elif equation == "/" or "_" or "division" or "divide":
        print("The result is:")
        time.sleep(1)
        print(numberone / numbertwo)

    elif equation == "+" or "plus" or "addition" or "add":
        print("The result is:")
        time.sleep(1)
        print(numberone + numbertwo)


    elif equation == "@" or "test":
        print("The result is:")
        time.sleep(2)
        print("BUGGED")
        time.sleep(1)
        print("this is a test")
        time.sleep(1)
        print(numberone)
        time.sleep(1)
        print(numbertwo)
        time.sleep(1)
        print("QUITTING")
        quit()


    else:
        print("That wasn't an equation option!")
        time.sleep(1)
        print("Quitting, please restart CALCULA.")
        quit()

elif select == 2:                      #Ascii art for details selection
    print(" ")
    print(" _____________________________________                                 ")
    print(" | \/-0- Details and licensing -0-\/  \                                ")
    print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(" | »» CALCULA. V3 ««                                                  |")
    print(" |********************************************************************|")
    print(" | »Codename: Rainy; Version: 3.2.8_a                                 |")
    print(" | »WhsN: Added 4 option, restart and check that for more information↓|")
    print(" | Removed subtractio operation      (^^^)                            |")
    print(" |********************************************************************|")
    print(" | »Using and modifying: This calculator is open source, free to use↓ |")
    print(" | and can be modified and republished by any person for non ↓        |")
    print(" | commercial purposes only.                                          |")
    print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("  \               »-Restart the calculator to go back-«              /")
    print("   0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O0O")
    print(" ")
    # Feel completely free to modify the Ascii art in the way you want!
    quit()

elif select == 3:  # Detect if selection is set to the quit value
    print("Quitting...")
    quit()

elif select == 4:

    print(" ")
    print(" ______________________________________________________")
    print("|I recently saw a bug that made me fool, every time I  |")
    print("|do a subtraction operation for example, 10 - 2 instead|")
    print("|of showing 8, it shows 20 (ToT) [i tried to change the|")
    print("|code but nothing changed], I'm trying to solve it ASAP|")
    print("|______________________________________________________|")
    print("  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print(" ")

#If you want to add one more option, add here ^^^ (Before the else statement, so it can check correctly)

else:  # Show a text and quit if it was not an detected option
    print("That wasn't a select option!")
    time.sleep(1)
    print("Quitting, please restart CALCULA.")
    quit()

