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

cursor.execute(f"select m_id,curr_quest,credits,power_points,stars from mem where user=\"{user}\"")

for x in cursor:
    mid,cq,creds,power,st=x

if cq>50:
    print("You have already finished campaign.")
    time.sleep(2)
    os.system('cls')
    quit()

if cq==50:
    os.system('cls')
    time.sleep(2)
    os.system(f"{path}\\DUEL_new\\Menu\\final_quest.py")

if cq==1:
    time.sleep(2)
    print("This is where it all begins.")
    time.sleep(2)
    print("But first, you must know why I brought you here.")
    time.sleep(2)
    print("A long time ago when the second Star was created, a dark force hidden at the core of The Forge unleashed itself...")
    time.sleep(2)
    print("It was darkness at it's purest form...unstoppable, dense, evil.")
    time.sleep(2)
    print("After eons we thought that the darkness had died out.")
    time.sleep(2)
    print("We were wrong.")
    time.sleep(2)
    print("We formed a group of Star contenders called The Guardians to hunt it down.")
    time.sleep(2)
    print("Sadly...we failed.")
    time.sleep(2)
    print("Now, I've decided to recruit you to destroy the darkness.")
    time.sleep(2)
    print("You are officially a Guardian now.")
    time.sleep(2)
    print("You must be ready to face whatever comes ahead of you.")
    time.sleep(2)
    print("Some enemies have deceptive rating. Don't judge an enemy by their rating.")
    time.sleep(2)
    print("Godspeed, Guardian.")
    time.sleep(2)
    os.system('cls')

print("-------------------------Campaign\n")
    
while True:
    
    cursor.execute(f"select c_id,name,rating from memchars where m_id=\"{mid}\"")

    print("-------------------------Character list\n")

    li=[]
    cout=0
    
    for x in cursor:
        li.append(x[0])
        cout+=1
        print(f"{x[0]} {x[1]}[{x[2]}]")

    print("\n-------------------------\n")

    if cout<3:
        print("\nYou need atleast 3 contenders to play.\n")
        time.sleep(3)
        os.system('cls')
        quit()

    if cq==1:
        print("Pick 3 contenders to get into the fight.\n")

    n=0
    li2=[]

    liname=[]
    liatt=[]
    lihlt=[]
    lirate=[]
    liplvl=[]

    while n<3:

        chars=input("Enter intended Contender ID (Type '000' to exit campaign ![Progress will not be saved]!) : C_")
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
    print(f"\nEntering Quest {cq}...\n")
    time.sleep(2)
    os.system('cls')
    
    print(f"-------------------------Quest {cq}\n")

    if cq==1:
        print("This is your first quest.")
        time.sleep(2)
        print("Not to worry, I'll help you through this one.")
        time.sleep(2)
        print("Here are the basics.")
        time.sleep(2)
        print("In one quest there are 3 rounds.")
        time.sleep(2)
        print("You will face one person each round using one of your contenders.")
        time.sleep(2)
        print("Now, this a turn-based duel. You'll go first.")
        time.sleep(2)
        print("You have 4 abilities.")
        time.sleep(2)
        print("Enter the corresponding number to use the ability.")
        time.sleep(2)
        print("Strike : Deals basic damage on the opponent.")
        time.sleep(2)
        print("Charge : You will gain +1 charge.")
        time.sleep(2)
        print("Critical strike : Multiplies basic damage with number of charges and deals a heavy blow.\tIf you have zero charges, well...")
        time.sleep(2)
        print("Heal : Gain 20 health using 5 charges.")
        time.sleep(2)
        print("When an attack uses charges, the charges get reduced to zero.")
        time.sleep(2)
        print("If your contender is power level 3, there's another ability.")
        time.sleep(2)
        print("That's about it...good luck.\n")
        time.sleep(2)

    den=0
    dch=0
    ddch=0
    roundno=0

    while True:

        time.sleep(2)
        os.system('cls')

        if roundno==3:
            break
        
        if dch==3:
            print("\nAll of your contenders lost.")
            time.sleep(2)
            print("Going to main menu...")
            time.sleep(3)
            os.system('cls')
            quit()
            
        print(f"-------------------------Round {roundno+1}\n")
        for j in range(0,3):
            print(f"{li2[j]} {liname[j]}[{lirate[j]}]     Health : {lihlt[j]}")

        print()

        fightch=input("Enter intended Contender ID for the fight(Type '000' to exit campaign ![Progress will not be saved]!) : C_")
        fightch=fightch.strip()

        roundch="C_"+fightch
        roundch=roundch.strip()

        if fightch=='000':
            os.system('cls')
            quit()

        if roundch not in li2:
            print("\nInvalid ID.\n")
            roundno-1
            continue
        else:
            statno=li2.index(roundch)
            ratech=lirate[statno]
            attch=liatt[statno]
            hltch=lihlt[statno]
            if hltch==0:
                print("\nLow health.\n")
                roundno-1
                continue
            namech=liname[statno]
            lvlch=liplvl[statno]
            hltin=hltch

        if ddch==0:
            inenemyhlt=300+(roundno*10)+(cq*10)
        elif ddch==1:
            ddch=0
            inenemyhlt=enemyhlt
            
        enemyatt=15+(roundno*cq)
        enemyrate=100

        if cq>=20:
            enemyatt=100+(roundno*cq)
            enemyrate=150

        if cq>=30:
            enemyatt=200+(roundno*cq)
            enemyrate=250

        if cq>=40:
            enemyatt=500+(roundno*cq)
            enemyrate=550
            
        enemyhlt=inenemyhlt

        charge=0

        print("--------------------\n")

        print(f"\n{namech}[{ratech}] Health : {hltch}  -vs- Dark Soldier[{enemyrate+((roundno+1)*cq)}] Health : {enemyhlt}")

        print()

        while True:
            
            time.sleep(3)
            os.system('cls')

            while True:

                print("--------------------\n")
                if lvlch<3:
                    turn=input("1.Strike\n2.Charge\n3.Crit. Strike\n4.Heal\n\nYour choice (Type '0' to quit the fight) : ")
                elif lvlch>=3:
                    turn=input("1.Strike\n2.Charge\n3.Crit. Strike\n4.Heal\n5.Rage (Uses 15 charges. Atk +2)\n\nYour choice : ")

                print()
                if turn=='0':
                    dch+=1
                    ddch=1
                    lihlt[statno]=0
                    print("You quit the fight.\n")
                    print("--------------------\n")
                    break
                elif turn=='1':
                    chatt=random.randint(attch,attch+5)
                    enemyhlt=enemyhlt-chatt
                    print(f"{namech} : Strike [{chatt}]")
                    if enemyhlt<=0:
                        print("--------------------\n")
                        print("You won!")
                        roundno+=1
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
                        roundno+=1
                        den=1
                        break
                    charge=0
                    break
                elif turn=='4':
                    if charge<5:
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
                if enmove==1:
                    enchatt=random.randint(enemyatt,enemyatt+5)
                    hltch=hltch-enchatt
                    print(f"Dark Soldier : Strike [{enchatt}]\n")
                    print("--------------------\n")
                    if hltch<=0:
                        hltch=0
                        print("You lost!")
                        ddch+=1
                        dch+=1
                        break
                    print(f"{namech} health : {hltch}  Charges : {charge}\nDark Soldier health : {enemyhlt}\n")
                    break
                elif enmove==2:
                    enchatt=random.randint(0,roundno+1)
                    hltch=hltch-enchatt
                    print(f"Dark Soldier : Stun [{enchatt}]")
                    if hltch<=0:
                        hltch=0
                        print("--------------------\n")
                        print("You lost!")
                        ddch+=1
                        dch+=1
                        break
                    continue
                elif enmove==3:
                    enrage=random.randint(0,roundno+1)
                    enemyatt=enemyatt+enrage
                    print(f"Dark Soldier : Rage [Atk +{enrage}]\n")
                    print("--------------------\n")
                    print(f"{namech} health : {hltch}  Charges : {charge}\nDark Soldier health : {enemyhlt}\n")
                    break

            if ddch==1:
                lihlt[statno]=hltch
                break
                    

    print(f"\nYou finished Quest {cq}!")
    cq+=1
    cr=random.randint(100,400)
    creds=creds+cr
    print(f"You earnt {cr} credits!")
    
    luck1=random.randint(1,5)
    if luck1==2:
        st+=5
        print("You earnt 5 star points!")
        cursor.execute(f"update mem set stars={st} where m_id=\"{mid}\"")
        
    luck2=random.randint(1,10)
    if luck2==3:
        power+=2
        print("You earnt 2 power points!")
        cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
        
    cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
    cursor.execute(f"update mem set curr_quest={cq} where m_id=\"{mid}\"")
    mydb.commit()
    
    if cq==2:
        print("\nYou got some resources.")
        time.sleep(2)
        print("Let's use these resources to make your contenders stronger.")
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        os.system(f"{path}\\DUEL_new\\Menu\\characters.py")
    while True:
        nexq=input("Proceed to next quest? (y/n) : ")
        if nexq.lower().strip()=="y":
            if cq==50:
                os.system('cls')
                time.sleep(2)
                os.system(f"{path}\\DUEL_new\\Menu\\final_quest.py")
            os.system('cls')
            break
        elif nexq.lower().strip()=="n":
            filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
            filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
            filee.write(f"cursor.execute('update mem set curr_quest={cq} where m_id=\"{mid}\"')\n")
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
        
            
                
                
                
        

                
                
            
        
        
        
        
            
    
            
