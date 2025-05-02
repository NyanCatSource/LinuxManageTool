print("Linux system management tools.")
import os
os.system("uname -a")
print("Which package manager does your system use?")
print("1.APT")
print("2.pip")
print("3.yum")
choose = True
while choose:
    chos = input("Input 1 or 2 or 3:")
    if chos == "1":
        #Reserved position
        print()
    elif chos == "2":
        #Reserved position
        print()
    elif chos == "3":
        print() #Reserved position
    else:
        print("Please select a valid selection!")
