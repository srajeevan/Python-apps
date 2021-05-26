# Odd or Even Project
# print("What number are you thinking?")
num = input("WHat number are you thinking?")
mod = int(num) % 2
if mod > 0:
    # print("That is an odd number")
    print("The number you have entered is", num, "and it is odd")
else:
    print("That is an even number")
