import os
import os.path
import time
import mysql.connector
import sys

time.sleep(1)
sys.stdout.write("\rInstalling...|")
sys.stdout.flush()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="teju1sid",
    )

cursor=mydb.cursor()

try:
    cursor.execute("create database duel")
    cursor.execute("use duel")
except:
    sys.stdout.write("\rGame already installed.")
    sys.stdout.flush()
    time.sleep(2)
    quit()
else:
    pass


cursor.execute("create table mem(m_id varchar(5) not null unique,user varchar(20) not null unique,passw varchar(10) not null unique,curr_quest bigint not null,credits bigint not null,power_points bigint not null,stars bigint not null)")
sys.stdout.write("\rInstalling.../")
sys.stdout.flush()
cursor.execute("create table chars(c_id varchar(5) not null unique,name varchar(20) not null unique,rating bigint not null,power_lvl bigint not null,atk bigint not null,health bigint not null,cost bigint not null)")
sys.stdout.write("\rInstalling...-")
sys.stdout.flush()
cursor.execute("create table memchars(m_id varchar(5) not null,c_id varchar(5) not null,name varchar(20) not null,rating bigint not null,power_lvl bigint not null,atk bigint not null,health bigint not null)")
sys.stdout.write("\rInstalling...\\")
sys.stdout.flush()
os.system("C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms\\DUEL_new\\Menu\\installinfo.py")
sys.stdout.write("\rInstalling...|")
sys.stdout.flush()
time.sleep(1)
sys.stdout.write("\rInstalling...done")
sys.stdout.flush()
time.sleep(2)
