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

cursor.execute(f"select curr_quest from mem where user=\"{user}\"")

for xx in cursor:
    cq=xx[0]

if cq==2:
    print("This is the upgrade centre.")
    time.sleep(2)
    print("The process is simple.")
    time.sleep(2)
    print("Select. Spend. Enjoy.")
    time.sleep(2)
    print("Try this one on your own. Exit when done and you're all set.")

cout=0
res=0
wr=0

while True:
    time.sleep(2)
    os.system('cls')
    
    cursor.execute(f"select m_id,credits,power_points from mem where user=\"{user}\"")

    for x in cursor:
        mid,creds,power=x

    cursor.execute(f"select c_id,name,rating from memchars where m_id=\"{mid}\" order by rating")

    print("-------------------------Character list\n")

    li=[]
    
    for x in cursor:
        li.append(x[0])
        print(f"{x[0]} {x[1]}[{x[2]}]")

    print("\n-------------------------\n")
    char=input("Enter intended Contender ID (Type '000' to exit) : C_")
    char=char.strip()

    if char=='000':
        print()
        if res==1:
            cursor.execute(f"select c_id,name,rating,power_lvl,atk,health from memchars where c_id=\"{inchoice}\" and m_id=\"{mid}\"")
            for f in cursor:
                cid,n,rate,pl,att,hlt=f
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'r')
            play=filee.readlines()
            filee.close()
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'w')
            filee.write("")
            filee.close()
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            for ply in play:
                if "update" in ply and mid in ply and cid in ply:
                    wr=5
                    continue
                else:
                    if wr>0:
                        wr=wr-1
                        continue
                    wr=0
                    filee.write(ply)
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            filee.write(f"cursor.execute('update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
            filee.write("mydb.commit()\n")
            filee.write("c+=1\n")
            filee.write(f"load()\n")
            filee.close()
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")
        quit()

    choice="C_"+char
    choice=choice.strip()
    
    if choice not in li:
        print("\nInvalid Contender ID.\n")
        continue
    else:
        pass

    if cout==0:
        inchoice=choice
        res=0
        cout+=1

    if inchoice!=choice:
        if res==1:
            cursor.execute(f"select c_id,name,rating,power_lvl,atk,health from memchars where c_id=\"{inchoice}\" and m_id=\"{mid}\"")
            for f in cursor:
                cid,n,rate,pl,att,hlt=f
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'r')
            play=filee.readlines()
            filee.close()
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'w')
            filee.write("")
            filee.close()
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            for ply in play:
                if "update" in ply and mid in ply and cid in ply:
                    wr=5
                    continue
                else:
                    if wr>0:
                        wr=wr-1
                        continue
                    filee.write(ply)
            filee.write(f"cursor.execute('update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"')\n")
            filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
            filee.write("mydb.commit()\n")
            filee.write("c+=1\n")
            filee.write(f"load()\n")
            filee.close()
            res=0
            inchoice=choice
    else:
        inchoice=choice
        res=0

    os.system('cls')
    cursor.execute(f"select c_id,name,rating,power_lvl,atk,health from memchars where c_id=\"{choice}\" and m_id=\"{mid}\"")
    for f in cursor:
        cid,n,rate,pl,att,hlt=f

    print(f"\nStats : \n\nID : {cid}\n\nName : {n}[{rate}]\nPower level : {pl}\nAttack : {att}\nHealth : {hlt}\n")

    while True:
        print(f"Credits : {creds}\nPower points : {power}\n")
        up=input("Upgrade contender? (y/n) : ")
        if up.lower().strip()=='y':
            
            if pl==1:
                if rate>=150:
                    while True:
                        pp=input("Use 1 power point to power up? (y/n) : ")
                        pp=pp.lower().strip()
                        if pp=='y':
                            if power<1:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                power=power-1
                                cursor.execute(f"update memchars set power_lvl={pl+1} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                                mydb.commit()
                                break
                        elif pp=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                else:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*65} credits to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if creds<65*raw:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=5*raw
                                att+=2*raw
                                hlt+=10
                                creds=creds-(65*raw)
                                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                        
            if pl==2:
                if rate>=250:
                    while True:
                        pp=input("Use 2 power point to power up? (y/n) : ")
                        pp=pp.lower().strip()
                        if pp=='y':
                            if power<2:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                power=power-2
                                cursor.execute(f"update memchars set power_lvl={pl+1} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                                mydb.commit()
                                break
                        elif pp=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                else:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*140} credits to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if creds<140*raw:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=5*raw
                                att+=4*raw
                                hlt+=15*raw
                                creds=creds-(140*raw)
                                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                        
            if pl==3:
                if rate>=550:
                    while True:
                        pp=input("Use 3 power point to power up? (y/n) : ")
                        pp=pp.lower().strip()
                        if pp=='y':
                            if power<3:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                power=power-3
                                cursor.execute(f"update memchars set power_lvl={pl+1} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                                mydb.commit()
                                break
                        elif pp=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                else:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*300} credits to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if creds<300*raw:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=10*raw
                                att+=6*raw
                                hlt+=30*raw
                                creds=creds-(300*raw)
                                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                        
            if pl==4:
                if rate>=1150:
                    while True:
                        pp=input("Use 5 power point to power up? (y/n) : ")
                        pp=pp.lower().strip()
                        if pp=='y':
                            if power<5:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                power=power-5
                                cursor.execute(f"update memchars set power_lvl={pl+1} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                                mydb.commit()
                                break
                        elif pp=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                else:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*750} credits to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if creds<750*raw:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=15*raw
                                att+=8*raw
                                hlt+=45*raw
                                creds=creds-(750*raw)
                                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                        
            if pl==5:
                if rate>=2150:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*10} power points to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if power<raw*10:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=20*raw
                                att+=25*raw
                                hlt+=100*raw
                                power=power-(raw*10)
                                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue
                else:
                    while True:
                        try:
                            raw=int(input("Number of levels to go up by : "))
                        except:
                            print("\nInvalid.\n")
                            continue
                        else:
                            break
                    while True:
                        upgrade=input(f"Use {raw*1800} credits to upgrade? (y/n) : ")
                        if upgrade.lower().strip()=="y":
                            if creds<1800*raw:
                                print("\nInsufficient resources.\n")
                                break
                            else:
                                res=1
                                rate+=20*raw
                                att+=10*raw
                                hlt+=70*raw
                                creds=creds-(1800*raw)
                                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                                cursor.execute(f"update memchars set rating={rate} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set atk={att} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                cursor.execute(f"update memchars set health={hlt} where m_id=\"{mid}\" and c_id=\"{cid}\"")
                                mydb.commit()
                                break
                        elif upgrade.lower().strip()=='n':
                            print("\nUpgrade cancelled.\n")
                            break
                        else:
                            print("\nInvalid choice.\n")
                            continue

            break
        
        elif up.lower().strip()=='n':
            print("\nUpgrade cancelled\n")
            break
        else:
            print("\nInvalid choice.\n")
            continue
                        
    

    
    

