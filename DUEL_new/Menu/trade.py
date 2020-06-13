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

cursor.execute(f"select m_id from mem where user=\"{user}\"")

for mm in cursor:
    mid=mm[0]

print("--------------------Trading centre\n")

ver=input("Enter Player ID : ")
ver=ver.strip()

if ver==mid:
    print("\nValid ID.")
    print("Trade resources.\n")
    time.sleep(2)
    pass
else:
    print("\nInvalid ID. You will have to leave for security purposes.\n")
    time.sleep(2)
    os.system('cls')
    quit()

while True:
    
    cursor.execute(f"select credits,power_points,stars from mem where m_id=\"{mid}\"")

    for x in cursor:
        creds,power,st=x
        
    print("1 star point : 200 credits")
    print("1 power point : 1500 credits\n")

    print(f"Your resources :\n\nCredits : {creds}\nStar points : {st}\nPower points : {power}\n")

    trade=input("1.Credits\n2.Star points\n3.Power points\n4.Exit\n\nYour choice : ")

    if trade=='1':
        print("\nWARNING :\n")
        print("Some credits may get wasted during conversion. To avoid this, trade the exact amount.\n")
        while True:
            try:
                amt=int(input("Enter number of credits : "))
            except:
                print("\nInvalid.\n")
            else:
                if amt>creds:
                    print("\nInsufficient resources.\n")
                    time.sleep(2)
                    os.system('cls')
                    break
                conv=input("\nConvert to :\n1.Star points\n2.Power points\n\nYour choice : ")
                creds=creds-amt
                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                if conv=='1':
                    ast=int(amt/200)
                    print(f"\nYou got {ast} star point(s).\n")
                    st=st+ast
                    cursor.execute(f"update mem set stars={st} where m_id=\"{mid}\"")
                    mydb.commit()
                    filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
                    filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
                    filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
                    filee.write("mydb.commit()\n")
                    filee.write("c+=1\n")
                    filee.write("load()\n")
                    filee.close()
                elif conv=='2':
                    apow=int(amt/1500)
                    print(f"\nYou got {apow} power point(s).\n")
                    power=power+apow
                    cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                    mydb.commit()
                    filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
                    filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
                    filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
                    filee.write("mydb.commit()\n")
                    filee.write("c+=1\n")
                    filee.write("load()\n")
                    filee.close()
                else:
                    print("\nInvalid choice.\n")
                    continue
                time.sleep(2)
                os.system('cls')
                break
            
    elif trade=='2':
        while True:
            try:
                amt=int(input("Enter number of star points : "))
            except:
                print("\nInvalid.\n")
            else:
                if amt>st:
                    print("\nInsufficient resources.\n")
                    time.sleep(2)
                    os.system('cls')
                    break
                acr=int(amt*200)
                print(f"\nYou got {acr} credits.")
                creds=creds+acr
                st=st-amt
                cursor.execute(f"update mem set stars={st} where m_id=\"{mid}\"")
                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                mydb.commit()
                filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
                filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
                filee.write(f"cursor.execute('update mem set stars={st} where m_id=\"{mid}\"')\n")
                filee.write("mydb.commit()\n")
                filee.write("c+=1\n")
                filee.write("load()\n")
                filee.close()
                time.sleep(2)
                os.system('cls')
                break

    elif trade=='3':
        while True:
            try:
                amt=int(input("Enter number of power points : "))
            except:
                print("\nInvalid.\n")
            else:
                if amt>power:
                    print("\nInsufficient resources.\n")
                    time.sleep(2)
                    os.system('cls')
                    break
                acr=int(amt*1500)
                print(f"\nYou got {acr} credits.")
                creds=creds+acr
                power=power-amt
                cursor.execute(f"update mem set power_points={power} where m_id=\"{mid}\"")
                cursor.execute(f"update mem set credits={creds} where m_id=\"{mid}\"")
                mydb.commit()
                filee=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'a')
                filee.write(f"cursor.execute('update mem set credits={creds} where m_id=\"{mid}\"')\n")
                filee.write(f"cursor.execute('update mem set power_points={power} where m_id=\"{mid}\"')\n")
                filee.write("mydb.commit()\n")
                filee.write("c+=1\n")
                filee.write("load()\n")
                filee.close()
                time.sleep(2)
                os.system('cls')
                break

    elif trade=='4':
        time.sleep(2)
        os.system('cls')
        os.system(f"{path}\\DUEL_new\\Menu\\transfer.py")
        quit()

    else:
        print("\nInvalid choice.\n")
        os.system('cls')
        break
                    
                    
