import mysql.connector
import os
import os.path
import time
import random

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

cursor.execute(f"select m_id,credits,power_points,stars from mem where user=\"{user}\"")

for x in cursor:
    mid,creds,power,st=x

sumcred=0
sumstar=0
sumpow=0


print("-------------------------The Grand Arena\n")

ver=input("Enter Player ID : ")
ver=ver.strip()

if ver==mid:
    print("\nValid ID.")
    print("Welcome and good luck.\n")
    time.sleep(2)
    pass
else:
    print("\nInvalid ID. You will have to leave for security purposes.\n")
    time.sleep(2)
    os.system('cls')
    quit()
    
cursor.execute(f"select c_id,name,rating,power_lvl from memchars where m_id=\"{mid}\" order by rating")

print("-------------------------Character list\n")

li=[]
li3=[]
coutlvl=0
    
for x in cursor:
    if x[2]>=1000:
        li.append(x[0])
        li3.append(x[2])
        print(f"{x[0]} {x[1]}[{x[2]}]")

print("\n-------------------------\n")

for lvll in li3:
    if lvll>=1000:
        coutlvl+=1

if coutlvl<3:
    print("\nYou need atleast 3 contenders of rating 1000 (Recommended : 4500) or above to play.\n")
    time.sleep(4)
    os.system('cls')
    quit()

n=0
li2=[]

liname=[]
liatt=[]
lihlt=[]
lirate=[]
liplvl=[]

while n<3:

    chars=input("Enter intended Contender ID (Type '000' to exit arena) : C_")
    chars=chars.strip()

    choice="C_"+chars
    choice=choice.strip()

    if chars=='000':
        os.system("cls")
        quit()

    if choice not in li:
        print("\nInvalid ID.\n")
        continue
    elif choice in li2:
        print("\nYou have already chosen this contender.\n")
        continue
    else:
        cursor.execute(f"select c_id, name, rating, power_lvl, atk, health from memchars where c_id=\"{choice}\" and m_id=\"{mid}\"")
        for m in cursor:
            cid,name,rate,lvl,att,hlt=m
        liname.append(name)
        liatt.append(att)
        lihlt.append(hlt)
        lirate.append(rate)
        li2.append(cid)
        liplvl.append(lvl)
        n+=1
        continue

print("\nYour contenders :\n")
for i in range(0,3):
    print(f"{liname[i]}[{lirate[i]}]")

cid1=li2[0]
cid2=li2[1]
cid3=li2[2]

name1=liname[0]
name2=liname[1]
name3=liname[2]

rate1=lirate[0]
rate2=lirate[1]
rate3=lirate[2]

att1=liatt[0]
att2=liatt[1]
att3=liatt[2]

hlt1=lihlt[0]
hlt2=lihlt[1]
hlt3=lihlt[2]

lvl1=liplvl[0]
lvl2=liplvl[1]
lvl3=liplvl[2]

time.sleep(2)
print(f"\nEntering The Grand Arena...\n")
time.sleep(2)
os.system('cls')

den=0
dch=0
ddch=0
roundno=0
mych=0

print("Think you're tough, huh? ...")
time.sleep(2)
print("You've got some skin showing up here.")
time.sleep(2)
print("If you're not the best, you don't belong here.")
time.sleep(2)
print("Word of caution. Friz is gonna test you.")
time.sleep(2)
print("Trust me, you would rather die than face Friz.")
time.sleep(2)
print("He's got a temper. He ain't going easy on ya. He's got his Guardian gear on.")
time.sleep(3)
print("Oh, and the rewards are just...ah.... You up for it?")
time.sleep(2)

cursor.execute("select name from chars")

lienname=[]

for nn in cursor:
    lienname.append(nn[0])

enemname=random.choice(lienname)

while True:

    time.sleep(2)
    os.system('cls')
        
    if dch==3:
        print("\nAll of your contenders lost.")
        time.sleep(2)
        print("\nReport :\n")
        time.sleep(1)
        print(f"Rounds survived       : {roundno}")
        time.sleep(1)
        print(f"Credits acquired      : {sumcred}")
        time.sleep(1)
        print(f"Star points acquired  : {sumstar}")
        time.sleep(1)
        print(f"Power points acquired : {sumpow}")
        time.sleep(3)
        print("Going to main menu...")
        time.sleep(3)
        filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
        filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
        filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
        filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
        filee.write("mydb.commit()\n")
        filee.write("c+=1\n")
        filee.write("load()\n")
        filee.close()
        os.system('cls')
        quit()
            
    print(f"-------------------------Round {roundno+1}\n")
    for j in range(0,3):
        print(f"{li2[j]} {liname[j]}[{lirate[j]}]     Health : {lihlt[j]}")

    print()

    fightch=input("Enter intended Contender ID for the fight(Type '000' to exit arena) : C_")
    fightch=fightch.strip()

    roundch="C_"+fightch
    roundch=roundch.strip()

    if fightch=='000':
        print("\nReport :\n")
        time.sleep(1)
        print(f"Rounds survived       : {roundno}")
        time.sleep(1)
        print(f"Credits acquired      : {sumcred}")
        time.sleep(1)
        print(f"Star points acquired  : {sumstar}")
        time.sleep(1)
        print(f"Power points acquired : {sumpow}")
        time.sleep(3)
        filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
        filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
        filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
        filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
        filee.write("mydb.commit()\n")
        filee.write("c+=1\n")
        filee.write("load()\n")
        filee.close()
        os.system('cls')
        quit()

    if roundch not in li2:
        print("\nInvalid ID.\n")
        continue
    else:
        statno=li2.index(roundch)
        ratech=lirate[statno]
        attch=liatt[statno]
        inattch=attch
        hltch=lihlt[statno]
        if hltch==0:
            print("\nLow health.\n")
            continue
        namech=liname[statno]
        lvlch=liplvl[statno]
        hltin=hltch

    if ddch==0:
        if enemname=="Guardian Friz":
            inenemyhlt=10000+(roundno*100)
        else:
            inenemyhlt=7100+(roundno*100)
    elif ddch==1:
        ddch=0
        inenemyhlt=enemyhlt

    if enemname=="Guardian Friz":
        enemyatt=1255+(25*roundno)
    else:
        enemyatt=1155+(25*roundno)
    enemyhlt=inenemyhlt

    charge=0

    if name=="Guardian Friz":
        enemyrate=2770+(roundno*20)
    else:
        enemyrate=2150+(roundno*20)

    print("--------------------\n")

    print(f"\n{namech}[{ratech}] Health : {hltch}  -vs- {enemname}[{enemyrate}] Health : {enemyhlt}")

    print()

    souls=0
    soulch=0
    strike=0
    mych=0

    while True:

        time.sleep(3)
        os.system('cls')

        while True:

            print("--------------------\n")
            if lvlch<3:
                turn=input("1.Strike\n2.Charge\n3.Crit. Strike\n4.Heal\n\nYour choice (Type '0' to quit the fight) : ")
            elif lvlch>=3:
                if ratech<=2150:
                    turn=input("1.Strike\n2.Charge\n3.Crit. Strike\n4.Heal\n5.Rage (Uses 15 charges. Atk +2)\n\nYour choice : ")
                else:
                    turn=input("1.Strike\n2.Charge\n3.Crit. Strike\n4.Heal\n5.Rage (Uses 15 charges. Atk +5)\n\nYour choice : ")
                    

            print()
            if ratech>2150:
                if soulch>0:
                    print(f"{namech} : Soul Damage [{10*soulch}]")
                    enemyhlt=enemyhlt-(10*soulch)
                    soulch=soulch-1
                    if enemyhlt<=0:
                        enemyhlt=0
                        print("You won!")
                        den=1
                        break
            if turn=='0':
                dch+=1
                ddch=1
                hltch=0
                mych=1
                lihlt[statno]=0
                print("You quit the fight.\n")
                print("--------------------\n")
                break
            elif turn=='1':
                chatt=random.randint(attch,attch+5)
                enemyhlt=enemyhlt-chatt
                print(f"{namech} : Strike [{chatt}]")
                if ratech>2150:
                    if soulch==0:
                        souldamch=random.randint(1,8)
                        lucksoulch=random.randint(1,10)
                        if lucksoulch==5:
                            soulch=souldamch
                            print(f"{namech} : Soul Wound")
                        else:
                            pass
                if enemyhlt<=0:
                    print("--------------------\n")
                    print("You won!")
                    den=1
                    break
                break
            elif turn=='2':
                charge+=1
                print(f"{namech} : Charge [+1]")
                break
            elif turn=='3':
                chatt=(random.randint(attch,attch+5))*charge
                enemyhlt=enemyhlt-chatt
                print(f"{namech} : Crit. Strike [{chatt}]")
                if enemyhlt<=0:
                    print("--------------------\n")
                    print("You won!")
                    den=1
                    break
                charge=0
                break
            elif turn=='4':
                if charge==0:
                    print(f"{namech} : Heal failed.")
                    break
                hltch=hltch+20
                if hltch>hltin:
                    hltch=hltin
                charge=charge-5
                if charge<0:
                    charge=0
                print(f"{namech} : Heal [+20]")
                break
            elif turn=='5':
                if lvlch>=3:
                    if charge<15:
                        print(f"{namech} : Rage failed.")
                        break
                    if ratech>2150:
                        charge=charge-15
                        attch=attch+5
                        print(f"{namech} : Rage [Atk +5]")
                        break
                    else:
                        charge=charge-15
                        attch=attch+2
                        print(f"{namech} : Rage [Atk +2]")
                        break 
                else:
                    print("Invalid choice.\n")
                    print("--------------------\n")
                    continue
            else:
                print("Invalid choice.\n")
                print("--------------------\n")
                continue

        if den==1:
            lihlt[statno]=hltch
            den=0
            break

        if ddch==1:
            lihlt[statno]=hltch
            break

        while True:
            enmove=random.randint(1,3)
            if souls>0:
                print(f"{enemname} : Soul Damage [{10*souls}]")
                hltch=hltch-(10*souls)
                souls=souls-1
                if hltch<=0:
                    hltch=0
                    print("You lost!")
                    ddch+=1
                    mych=1
                    dch+=1
                    break
            if enemname=="Guardian Friz":
                if strike==25:
                    strike=0
                    attch=inattch
                strike+=5
                strk=strike*100
                attch=attch-strk
                if attch<=0:
                    attch=0
                print(f"{enemname} : Guardian Aura [Opponent Atk -{strk}]")
            if enmove==1:
                enchatt=random.randint(enemyatt,enemyatt+5)
                hltch=hltch-enchatt
                print(f"{enemname} : Strike [{enchatt}]")
                if souls==0:
                    souldam=random.randint(1,8)
                    lucksoul=random.randint(1,5)
                    if lucksoul==3:
                        souls=souldam
                        print(f"{enemname} : Soul Wound")
                    else:
                        pass
                print("\n--------------------\n")
                if hltch<=0:
                    hltch=0
                    print("You lost!")
                    ddch+=1
                    dch+=1
                    mych=1
                    break
                print(f"{namech} health : {hltch}  Charges : {charge}\n{enemname} health : {enemyhlt}\n")
                break
            elif enmove==2:
                enchatt=random.randint(100,(roundno+3)*100)
                hltch=hltch-enchatt
                enemyhlt=enemyhlt+enchatt
                print(f"{enemname} : Life Transfer [{enchatt}]")
                if hltch<=0:
                    hltch=0
                    print("--------------------\n")
                    print("You lost!")
                    mych=1
                    ddch+=1
                    dch+=1
                    break
                continue
            elif enmove==3:
                if enemname=="Guardian Friz":
                    enrage=random.randint(100,roundno+500)
                    enemyatt=enemyatt+enrage
                    print(f"{enemname} : !@#? the Guardian Code [Atk +{enrage}]\n")
                    print("--------------------\n")
                    print(f"{namech} health : {hltch}  Charges : {charge}\n{enemname} health : {enemyhlt}\n")
                elif enemyrate>2500:
                    enrage=random.randint(30,roundno+70)
                    enemyatt=enemyatt+enrage
                    print(f"{enemname} : Rage [Atk +{enrage}]\n")
                    print("--------------------\n")
                    print(f"{namech} health : {hltch}  Charges : {charge}\n{enemname} health : {enemyhlt}\n")
                else:
                    enrage=random.randint(10,roundno+40)
                    enemyatt=enemyatt+enrage
                    print(f"{enemname} : Rage [Atk +{enrage}]\n")
                    print("--------------------\n")
                    print(f"{namech} health : {hltch}  Charges : {charge}\n{enemname} health : {enemyhlt}\n")
                break

        if ddch==1:
            lihlt[statno]=hltch
            mych=1
            break

    if mych==1:
        mych=0
        continue
                    
    cr=random.randint(500,800)
    creds=creds+cr
    sumcred+=cr
    print(f"You earnt {cr} credits!")
    
    luck1=random.randint(1,2)
    if luck1==2:
        sttt=random.randint(40,80)
        st+=sttt
        sumstar+=sttt
        print(f"You earnt {sttt} star points!")
        cursor.execute(f"update mem set stars={st} where m_id=\"{mid}\"")
        
    luck2=random.randint(1,3)
    if luck2==2:
        pwr=random.randint(20,50)
        power+=pwr
        sumpow+=pwr
        print(f"You earnt {pwr} power points!")
        cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
        
    cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
    mydb.commit()
    
    while True:
        nexq=input("Proceed to next round? (y/n) : ")
        if nexq.lower().strip()=="y":
            roundno+=1
            enemname=random.choice(lienname)
            if (roundno+1)%3==0:
                enemname="Guardian Friz"
                strike=0
            os.system('cls')
            break
        elif nexq.lower().strip()=="n":
            print("\nReport :\n")
            time.sleep(1)
            print(f"Rounds survived       : {roundno+1}")
            time.sleep(1)
            print(f"Credits acquired      : {sumcred}")
            time.sleep(1)
            print(f"Star points acquired  : {sumstar}")
            time.sleep(1)
            print(f"Power points acquired : {sumpow}")
            time.sleep(3)
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
            filee.write("mydb.commit()\n")
            filee.write("c+=1\n")
            filee.write("load()\n")
            filee.close()
            os.system('cls')
            os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")
            quit()
        else:
            print("\nInvalid choice.\n")
            continue
        
            
                
                
                
        

                
                
            
        
        
        
        
            
    
            
