print("Linux system management tools.")
try:
    with open('/bin/sudo') as check_sudo:
        onlycheck = check_sudo.read()
except FileNotFoundError:
    print("Please install sudo!")
    import os
    os.system("apt install sudo")
    os.system("yum install sudo")

import os
os.system("uname -a")
print("Which package manager does your system use?")
print("1.APT")
print("2.pip #disabled")
print("3.yum")
choose = True
while choose:
    chos = input("Input 1 or 2 or 3:")
    if chos == "1":
        #Reserved position
        print("What do you want to do?")
        print("1.install apache http server.")
        chosa = input("Please input.")
        if chosa == "1":
            import os
            os.system("sudo apt install apache2")
            os.system("service apache2 start")
            print("Do you want to stop the firewall and selinux?")
            chosb = input("type yes or no.")
            if chosb == "yes":
                chossysd = input("Is your system have systemd?,input yes or no.")
                if chossysd == "yes":
                    import os
                    os.system("systemctl stop ufw")
                if chossysd == "no":
                    import os
                    os.system("service ufw stop")
                import os
                os.system("setenforce 0")
                choose = False
            if chosb == "no":
                print("Thanks for using it.")
                choose = False
            else:
                print("Please select a valid selection!")
    elif chos == "2":
        #Reserved position
        print()
    elif chos == "3":
        print() #Reserved position
    else:
        print("Please select a valid selection!")
