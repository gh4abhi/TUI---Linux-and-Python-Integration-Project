import os
import getpass

os.system("tput setaf 1")
print("\t\t\tWelcome to my TUI that makes life simple")
os.system("tput setaf 7")

print("\t\t\t----------------------------------------")

password =getpass.getpass("Enter the password : ")
if password != 'Menu':
    print("Incorrect Password")
    exit()
print("Where you want to perform your task (Local/Remote) : ",end="")
location = input()
print(location)

if location == "Remote":
	ip = input("Enter the IP of the System")


while True:
	print("""        Press 1: To see date
        Press 2: To check Calender
	Press 3: Configure Web Server
	Press 4: To create User
	Press 5: Create File
	Press 6: To setup Networking
	Press 7: To exit
		        """)

	print("Enter your choice : ",end="")
	ch = int(input())

	print(ch)
      

	if location == 'Local':
		if ch==1:
		     os.system("date")
		elif ch==2:
		     os.system("cal")
		elif ch==3:
		     os.system("yum install httpd")
		elif ch==4:
		     print("Enter username - ",end="")
		     create_Username = input() 
		     os.system("useradd {}".format(create_Username))
		elif ch==5:
		     os.system("date")
		elif ch==6:
		     os.system("date")
		elif ch==7:
		     exit()
		else:
		     print("Option not supported")
		input("Press Enter to continue ")
		os.system("clear")     
	elif location == "Remote":
		if ch==1:
		     os.system("ssh {} date".format(ip))
		elif ch==2:
		     os.system("ssh {} cal".format(ip))
		elif ch==3:
		     os.system("yum install httpd")
		elif ch==4:
		     print("Enter username - ",end="")
		     create_Username = input() 
		     os.system("ssh {0} useradd {1}".format(ip,create_Username))
		elif ch==5:
		     os.system("date")
		elif ch==6:
		     os.system("date")
		elif ch==7:
		     exit()
		else:
		     print("Option not supported")
		input("Press Enter to continue ")
		os.system("clear")
	else:
		print("Doesn't Support")
