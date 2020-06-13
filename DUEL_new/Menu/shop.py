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

file=open(f"{path}\\DUEL_new\\Menu\\logged_in.txt",'r')
user=file.read()
file.close()

cursor.execute(f"select m_id,curr_quest,stars from mem where user=\"{user}\"")

for x in cursor:
    mid,cq,st=x

print("-------------------------Star Forge\n")
time.sleep(1)
if cq==1:
    print("Welcome to The Forge.")
    time.sleep(2)
    print("This is the very place where I was born.")
    time.sleep(2)
    print("I noticed your pockets and it looks like you have some special currency with you...")
    time.sleep(2)
    print("Well, lucky for you, that is exactly what we need.")
    time.sleep(2)
    print("You can buy contenders for star points(the special currency)...anytime you want.")
    time.sleep(2)
    print("You also need your ID for verification of transaction so, remember your ID.")
    time.sleep(2)
    print("Enter your ID exactly the way it is...don't switch around numbers or enter in lowercase letters instead of uppercase...")
    time.sleep(3)
    print("Entering the wrong ID can get you kicked out of places so, beware.")
    time.sleep(2)
    print("I'll give your ID for now. Remember this as it will not be revealed the next time.\n")
    print(f"Player ID : {mid}\n")
    time.sleep(3)

ver=input("Enter Player ID : ")
ver=ver.strip()

if ver==mid:
    print("\nValid ID.")
    print("Buy your contenders.\n")
    time.sleep(2)
    pass
else:
    print("\nInvalid ID. You will have to leave for security purposes.\n")
    time.sleep(2)
    os.system('cls')
    quit()



while True:
    cursor.execute(f"select c_id from memchars where m_id=\"{mid}\"")
    li2=[]
    for t in cursor:
        li2.append(t[0])
    
    cursor.execute(f"select c_id, name, rating, cost from chars order by rating")

    print("-------------------------Contenders\n")

    li=[]

    for k in cursor:
        if k[0] in li2:
            continue
        li.append(k[0])
        if k[2]==100:
            print("--------------------Power level 1--+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*20+"|\n"+" "*35+"|")
        elif k[2]==150:
            print("--------------------Power level 2--+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*20+"|\n"+" "*35+"|")
        elif k[2]==250:
            print("--------------------Power level 3--+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*20+"|\n"+" "*35+"|")
        elif k[2]==550:
            print("--------------------Power level 4--+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*19+"|\n"+" "*35+"|")
        elif k[2]==1150:
            print("--------------------Power level 5--+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*19+"|\n"+" "*35+"|")
        elif k[2]==2150:
            print("--------------------Star-----------+\n"+" "*35+"|\n"+" "*35+"|"+f"\nCost : {k[3]} stars"+" "*18+"|\n"+" "*35+"|")

        length=len(f"Name : {k[1]}[{k[2]}]")
            
        print(f"Contender ID : {k[0]}"+" "*15+"|\n"+f"Name : {k[1]}[{k[2]}]"+" "*(35-length)+"|\n"+" "*35+"|")
        print("-"*35+"|\n")

    print()
    print("[--^^^--Scroll up to view contenders--^^^--]\n")
    
    print(f"\nStar points : {st}")
    char=input("\nEnter intended Contender ID (Type '000' to exit The Forge) : C_")
    char=char.strip()

    if char=='000':
        print()
        if cq==1:
            os.system('cls')
            os.system(f"{path}\\DUEL_new\\Menu\\quest.py")
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")
        quit()
        
    choice="C_"+char
    choice=choice.strip()
    
    if choice not in li:
        print("\nInvalid Contender ID.\n")
        time.sleep(2)
        os.system('cls')
        continue
    else:
        pass
    
    cursor.execute(f"select * from chars where c_id=\"{choice}\"")
    for f in cursor:
        cid,n,rate,pl,att,hlt,cost=f
    
    while True:
        buy=input(f"\nStats : \n\nID : {cid}\n\nName : {n}[{rate}]\nPower level : {pl}\nAttack : {att}\nHealth : {hlt}\n\nBuy for {cost} star points? (y/n) : ")
        buy=buy.lower().strip()
        if buy=='y':
            if st<cost:
                print("\nNot enough star points.\n")
                time.sleep(2)
                os.system('cls')
                break

            st=st-cost
            cursor.execute(f"update mem set stars={st} where m_id=\"{mid}\"")
            cursor.execute(f"insert into memchars values(\"{mid}\",\"{cid}\",\"{n}\",{rate},{pl},{att},{hlt})")
            mydb.commit()
            print(f"\n'{n}' has been added to your roster.\n")
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('insert into memchars values(\"{mid}\",\"{cid}\",\"{n}\",{rate},{pl},{att},{hlt})')\n")
            filee.write("mydb.commit()\n")
            filee.write("c+=1\n")
            filee.write("load()\n")
            filee.close()
            time.sleep(3)
            os.system('cls')
            break
        elif buy=="n":
            os.system('cls')
            break
        else:
            print("\nInvalid choice.\n")
            time.sleep(2)
            os.system('cls')
            continue


