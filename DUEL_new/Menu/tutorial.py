import mysql.connector
import os
import os.path
import time

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="teju1sid",
    database="duel"
    )

cursor=mydb.cursor()

path = "C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms"

print("-------------------------Tutorial\n")
print("So you finally found The Grand Arena...")
time.sleep(2)
print("But, you have no one and we don't allow loners here...")
time.sleep(2)
print("However...")
time.sleep(1)
print("I'm not that sort of a guy.")
time.sleep(2)
print("I'm Friz, the first Star and the last of The Guardians.")
time.sleep(2)
print("I'm here to guide you through this arena.")
time.sleep(2)
print("First off...let me get you some mates...\n")
time.sleep(2)
os.system('cls')
os.system(f"{path}\\DUEL_new\\Menu\\shop.py")
