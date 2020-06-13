import github
import mysql.connector
import os
import os.path
import time
import sys

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="teju1sid",
        database="duel"
        )
except:
    print("Install the game to play.")
    time.sleep(3)
    quit()
else:
    pass

path = "C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms"

cursor=mydb.cursor()

os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")

try:
    filee=open(f"{path}\\DUEL_new\\Menu\\logged_in.txt",'r')
    user=filee.read()
    filee.close()
except:
    print("-------------------------DUEL\n")
    print("Welcome to Duel!\n")
    print("\nBut...you need to log in to enter the game.\n")
    os.system(f"{path}\\DUEL_new\\Menu\\login.py")
else:
    if user.strip()=="":
        print("-------------------------DUEL\n")
        print("Welcome to Duel!\n")
        print("\nBut...you need to log in to enter the game.\n")
        os.system(f"{path}\\DUEL_new\\Menu\\login.py")
    else:
        pass

cursor.execute(f"select m_id,curr_quest from mem where user=\"{user}\"")

for x in cursor:
    mid,cq=x[0],x[1]

print("-------------------------DUEL\n")
print("Welcome to Duel!\n")

if cq==1:
    os.system(f"{path}\\DUEL_new\\Menu\\tutorial.py")

print(f"Player ID : {mid}\n")

while True:
    print("-------------------------Main menu\n")
    print("1.Campaign\n2.Beginner's Arena\n3.Characters\n4.Star Forge\n5.Trade Centre\n6.The Grand Arena\n7.Dark Arena\n8.Logout\n9.Uninstall DUEL\n")
    ch=input("Menu : ")
    print()
    ch=ch.strip()
    if ch=='1':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\quest.py")
    if ch=='2':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\arena.py")
    if ch=='3':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\characters.py")
    if ch=='4':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\shop.py")
    if ch=='5':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\trade.py")
    if ch=='6':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\The_Grand_Arena.py")
    if ch=='7':
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\special.py")
    if ch=='8':
        print("Logged out.\n")
        os.remove(f"{path}\\DUEL_new\\Menu\\logged_in.txt")
        os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")
        os.system(f"{path}\\DUEL_new\\Menu\\login.py")
    if ch=='9':
        os.system('cls')
        cursor.execute("drop database duel")
        print("Game uninstalled.")
        time.sleep(2)
        quit()
