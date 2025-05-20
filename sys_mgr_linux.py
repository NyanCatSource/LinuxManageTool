import os #use os
print("What do you want to do?")
print("1.remove file.")
print("2.run the system command.")
print("3.Destroy.")
usech = input("")
if usech == "1":
    rmfile = input("What do you want to remove?")
    try:
        os.remove(str(rmfile))
    except FileNotFoundError:
        print("File Not Found.")
    except PermissionError:
        print("Permission Denied.") #Why the os.remove cannot remove a dictionary?
    print("Thanks for using.")
if usech == "3":
    surech = input("Do you want to destroy system? input yes or no.")
    if surech == "yes":
        get_error = os.system("sudo rm -rf /*")
        if get_error == 2:
            print("Failed.")
        else:
            print("OK.")
    else:
        print("Abort.")
else:
    print("Please select a vaild selection!")
