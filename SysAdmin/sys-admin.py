import os
import subprocess

path = '/home/ec2-user/environment/aws-restart/SysAdmin'
os.chdir(path)
#Adding a user
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter thename of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)
    
#Removing a user
def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r " + username)
    
#Adding a user to a group (1)
def add_user_to_group():
    username = input("Enter the name of the user that you wantto addto agroup: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to add the user to")
    print("The list should be separatedby spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosenGroups = input("Groups: ")
    
    #Adding a user to a group (2)
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add To:")
    found = True
    groupString = ""
    
    #Adding a user to a group (3)
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Existing Group : " + grp)
                groupString= groupString + grp + ","
        if found == False:
            print("-New Group : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
    #Adding a user to a group (4)
    groupString = groupString[:-1] + " "
    confirm = ""
    while confirm != "Y" and confirm != "N" :
        print("Add user '" + username + "' to thesegroups? (Y/N)")
        confirm = input().upper()
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username)
        print("User '" + username + "' added")

#Handling packages (1)
def install_or_remove_packages():
    iOrR= ""
    while iOrR!= "I" and iOrR!= "R":
        print("Would you like to install orremove packages? (I/R)")
        iOrR= input().upper()
    if iOrR == "I":
        iOrR= "install"
    elif iOrR == "R":
            iOrR= "remove"

    #Handling packages (2)
    print("Entera list of packages to install")
    print("The list should be separated by spaces, for example:")
    print(" package1package2package3")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
    packages = input().lower()
    if packages == "default":
        packages = "defaultPackages"
    if iOrR == "install":
        os.system("sudo yum install " + packages)
    
    #Handling packages (3)
    elif iOrR == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                os.system("sudo yum --purge " +iOrR + " " + packages)
                break
            elif choice == "N":
                os.system("sudo yum " + iOrR + "" + packages)
                break
        os.system("sudo yum autoremove")
        
    #Handling packages (4)
    def clean_environment():
        os.system("sudo apt-get autoremove")
        os.system("sudo apt-get autoclean")
    
    #Handling packages (5)
    def update_environment():
        os.system("sudo apt-get update")
        os.system("sudo apt-get upgrade")
        os.system("sudo apt-get dist-upgrade")

install_or_remove_packages()
    
    