print("Debian system management tools.")
try:
    with open('/bin/sudo') as check_sudo:
        onlycheck = check_sudo.read()
except FileNotFoundError:
    havesudo = "no"
import os
os.system("uname -a")

choose = True
while choose:
    chos = "1"
    def check_sudo_main():
        if havesudo == "no":
            print("Please install sudo!")
            exit()
    check_sudo_main()
    if chos == "1":
        #Reserved position
        print("What do you want to do?")
        print("1.install apache http server.")
        chosa = input("Please input.")
        if chosa == "1":
            import os
            checkapache = os.system("sudo apt install -y apache2")
            os.system("clear")
            eromes = 0
            if eromes == checkapache:
                print("OK.")
                #break
            else:
                print("Error.")
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
            import time
            print("You can see the log in 10s.")
            time.sleep(10)
    else:
        print("Please select a valid selection!")
