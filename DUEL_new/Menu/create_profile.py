import mysql.connector
import random
import time
import os
import os.path

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="teju1sid",
    database="duel"
    )

cursor=mydb.cursor()

path = "C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms"

print("-------------------------Create profile\n")
while True:
    try:
        print("-------------------------New profile\n")
        print("Generating ID...")
        time.sleep(2)
        mid=""
        no1=random.randint(0,9)
        no2=random.randint(10,99)
        ch1=random.randint(65,90)
        ch2=random.randint(65,90)
        mid=str(chr(ch1))+str(no1)+str(chr(ch2))+str(no2)
        print(f"\nID : {mid}")
        name=input("New username : ")
        name=name.strip()
        if name=="":
            print("\nThis field must be filled.\n")
            continue
        password=input("New password : ")
        password=password.strip()
        if password=="":
            print("\nThis field must be filled.\n")
            continue
        cursor.execute(f"insert into mem values(\"{mid}\",\"{name}\",\"{password}\",1,100,3,30)")
    except:
        print("\nUsername/password/ID has already been used.\n")
        continue
    else:
        print("\nYour profile has been created.\n")
        mydb.commit()
        file=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
        file.write("\n#--------------------New user created\n\n")
        file.write(f"cursor.execute('insert into mem values(\"{mid}\",\"{name}\",\"{password}\",1,100,0,30)')\n")
        file.write("mydb.commit()\n")
        file.write("c+=1\n")
        file.write("load()\n")
        file.close()
        time.sleep(3)
        break

time.sleep(2)
os.system('cls')
os.system(f"{path}\\DUEL_new\\Menu\\login.py")
    

    
