print("Linux system management tools.")
try:
    with open('/bin/sudo') as check_sudo:
        onlycheck = check_sudo.read()
except FileNotFoundError:
    havesudo = "no"
import os
os.system("uname -a")
print("Which package manager does your system use?")
print("1.APT")
print("2.apk")
print("3.yum")
choose = True
while choose:
    chos = input("Input 1 or 2 or 3:")
    if havesudo == "no":
        print("Please install sudo!")
        break
    pass
    if chos == "1":
        #Reserved position
        print("What do you want to do?")
        print("1.install apache http server.")
        chosa = input("Please input.")
        if chosa == "1":
            import os
            checkapache = os.system("sudo apt install -y apache2")
            os.system("clear")
            eromes = 2
            if eromes == checkapache:
                print("Install Failed.")
                break
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
