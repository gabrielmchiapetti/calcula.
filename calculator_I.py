#                                                                                   Calculator Version I
#                                                                            Made by @gabrielmchiapetti on GitHub
#                                                                   _____________________________________________________
#                                                                                   Coded in Python 3.12.2

import time
import math

print("ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣 𝕀")
time.sleep(1)
print("𝘔𝘢𝘥𝘦 𝘉𝘺 @𝘨𝘢𝘣𝘳𝘪𝘦𝘭𝘮𝘤𝘩𝘪𝘢𝘱𝘦𝘵𝘵𝘪")
time.sleep(1)
number_one = int(input("Number One: "))
number_two = int(input("Number Two: "))
time.sleep(1)
equation = str(input("What equation would you like to resolve? |+|-|*|/| "))

if equation == ("+"):
    print("The result of the equation is:")
    time.sleep(1)
    print(number_one + number_two)
    time.sleep(1)
    print("Thanks for using our service!")
    quit()
elif equation == ("-"):
    print("The result of the equation is:")
    time.sleep(1)
    print(number_one - number_two)
    time.sleep(1)
    print("Thanks for using our service!")
    quit()
elif equation == ("*"):
    print("The result of the equation is:")
    time.sleep(1)
    print(number_one * number_two)
    time.sleep(1)
    print("Thanks for using our service!")
    quit()
elif equation == ("/"):
    print("The result of the equation is:")
    time.sleep(1)
    print(number_one / number_two)
    time.sleep(1)
    print("Thanks for using our service!")
    quit()
