import mysql.connector
import os
import os.path
import time
import getpass

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="teju1sid",
    database="duel"
    )

cursor=mydb.cursor()

log=0

path = "C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms"

while True:
    if log>0:
        if os.path.exists(f"{path}\\DUEL_new\\Menu\\logged_in.txt")==True:
            os.remove(f"{path}\\DUEL_new\\Menu\\logged_in.txt")
        file=open(f"{path}\\DUEL_new\\Menu\\logged_in.txt",'x')
        file.close()
        file=open(f"{path}\\DUEL_new\\Menu\\logged_in.txt",'a')
        file.write(name)
        file.close()
        os.system("cls")
        os.system(f"{path}\\DUEL_new\\duel.py")
    a=0
    print("-------------------------Login\n")
    print("Type '_create_profile_' in username to create a new profile.\n")
    name=input("Username : ")
    name=name.strip()
    if name=="_create_profile_":
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\create_profile.py")
    password=getpass.getpass(prompt="Password : ")
    password=password.strip()
    cursor.execute("select user,passw from mem")
    for x in cursor:
        n,p=x[0],x[1]
        if name==n:
            if password==p:
                print("\nLogging in...")
                time.sleep(3)
                log=1
                break
    else:
        print("\nInvalid username/password.\n")
        log=0
        continue
        
    
            
        
