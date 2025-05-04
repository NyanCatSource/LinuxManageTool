print("Linux system management tools.")
try:
    with open('/bin/sudo') as check_sudo:
        onlycheck = check_sudo.read()
except FileNotFoundError:
    print("Please install sudo!")
    wtroot = input("Do you want to install sudo? type yes or no.")
    if wtroot == "yes":
        import os
        os.system("touch ab1227.temp")
        os.system("apt install -y sudo >> ab1227.temp")
        os.system("yum install -y sudo >> ab1227.temp")
    if wtroot == "no":
        pass
    else:
        print("not a vaild selection,skip.but the program can't run.")
        havesudo = "no"
import os
os.system("uname -a")
os.system("sudo echo")
print("Which package manager does your system use?")
print("1.APT")
print("2.pip #disabled")
print("3.yum")
choose = True
while choose:
    chos = input("Input 1 or 2 or 3:")
    if havesudo == "no":
        choose = False
    if chos == "1":
        #Reserved position
        print("What do you want to do?")
        print("1.install apache http server.")
        chosa = input("Please input.")
        if chosa == "1":
            import os
            os.system("sudo apt install apache2 >> ab1227.temp")
            os.system("sudo service apache2 start")
            print("Do you want to stop the firewall and selinux?")
            chosb = input("type yes or no.")
            if chosb == "yes":
                chossysd = input("Is your system have systemd?,input yes or no.")
                if chossysd == "yes":
                    import os
                    os.system("sudo systemctl stop ufw")
                if chossysd == "no":
                    import os
                    os.system("sudo service ufw stop")
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
        pass
    elif chos == "3":
        pass #Reserved position
    else:
        print("Please select a valid selection!")
