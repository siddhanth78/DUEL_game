import os
import os.path
import time
import mysql.connector
import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="teju1sid",
    database="duel"
    )

cursor=mydb.cursor()

sql="insert into chars values(%s,%s,%s,%s,%s,%s,%s)"

val=[

( "C_105","Sam",100,1 ,   15 ,    300 ,   10 ),
( "C_111","Rocky",250 ,3 ,  105 ,    700 ,   95 ),
( "C_119","Spike",100 ,1 ,   15 ,    300 ,   10 ),
( "C_136","Jean",150 ,2 ,   25 ,    400 ,   40 ),
( "C_144","Ingram",550 ,4 ,  285 ,   1600 ,  200 ),
( "C_187","Rick",150 ,2 ,   25 ,    400 ,   40 ),
( "C_209","Sarah",100 , 1 ,   15 ,    300 ,   10 ),
( "C_243","Aaron",250 , 3 ,  105 ,    700 ,   95 ),
( "C_302","Scarlet",250 ,3 ,  105 ,    700 ,   95 ),
( "C_312","Jake",100 ,1 ,   15 ,    300 ,   10 ),
( "C_337","Dom",150 ,2 ,   25 ,    400 ,   40 ),
( "C_347","Friz",2150 ,5 , 1105 ,   6900 , 2000 ),
( "C_356","Tyler",250 , 3 ,  105 ,    700 ,   95 ),
( "C_358","Tom",100 ,1 ,   15 ,    300 ,   10 ),
( "C_375","Reinmann",550 ,4 ,  285 ,   1600 ,  200 ),
( "C_385","Cade",100 , 1 ,   15 ,    300 ,   10 ),
( "C_405","Pump",150 , 2 ,   25 ,    400 ,   40 ),
( "C_429","Hardy",150 , 2 ,   25 ,    400 ,   40 ),
( "C_438","Ryder",550 ,4 ,  285 ,   1600 ,  200 ),
( "C_558","Finn",150 , 2 ,   25 ,    400 ,   40 ),
( "C_598","Steve",100 , 1 ,   15 ,    300 ,   10 ),
( "C_641","Destroyer",1150 , 5 ,  605 ,   3400 ,  550) ,
( "C_655","Reaper",1150 , 5 ,  605 ,   3400 ,  550 ),
( "C_658","Charles",550 , 4 ,  285 ,   1600 ,  200 ),
( "C_662","Joe",100 ,  1 ,   15 ,    300 ,   10 ),
( "C_691","Jenny",150 , 2 ,   25 ,    400 ,   40 ),
( "C_703","James",150 , 2 ,   25 ,    400 ,   40 ),
( "C_715","Roman",1150 , 5 ,  605 ,   3400 ,  550 ),
( "C_737","Gina",100 , 1 ,   15 ,    300 ,   10 ),
( "C_765","Elsa",250 , 3 ,  105 ,    700 ,   95 ),
( "C_776","Robin",250 , 3 ,  105 ,    700 ,   95 ),
( "C_803","Koby",150 , 2 ,   25 ,    400 ,   40 ),
( "C_807","Kate",100 , 1 ,   15 ,    300 ,   10 ),
( "C_855","Bob",150 , 2 ,   25 ,    400 ,   40 ),
( "C_867","Sky",250 , 3 ,  105 ,    700 ,   95 ),
( "C_905","Chris",100 , 1 ,   15 ,    300 ,   10 ),
( "C_921","Dru",550 , 4 ,  285 ,   1600 ,  200 ),
( "C_935","Jerry",100 ,1 ,   15 ,    300 ,   10 ),
( "C_942","Jeff",550 , 4 ,  285 ,   1600 ,  200 ),
( "C_945","Jack",100 ,1 ,   15 ,    300 ,   10 ),
( "C_985","Rob",100 ,1 ,   15 ,    300 ,   10 ),
( "C_997","Howard",100 , 1 ,   15 ,    300 ,   10)

]

cursor.executemany(sql,val)
mydb.commit()

c=0

def load():
    global c
    if c>3:
        c=0
    li=["|","/","-","\\"]
    sys.stdout.write("\r"+li[c])
    sys.stdout.flush()

#--------------------New user created

cursor.execute('insert into mem values("Q7Z41","andril","asap2000",1,100,0,30)')
mydb.commit()
c+=1
load()
cursor.execute('update mem set credits=1600 where m_id="Q7Z41"')
cursor.execute('update mem set power_points=2 where m_id="Q7Z41"')
mydb.commit()
c+=1
load()
