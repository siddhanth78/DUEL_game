import github
import os
import os.path
import time
import sys

path = "C:\\Users\\manju\\Desktop\\Coding\\PythonPrograms"


while True:
    sys.stdout.write("\rUpdating game info  [          ]")
    sys.stdout.flush()
    try:
        g = github.Github("siddhanth78","sid1!Teju")
        repo = g.get_user().get_repo("DUEL_game")
    except:
        sys.stdout.write("\rConnect to the internet to play.")
        sys.stdout.flush()
        time.sleep(3)
        continue
    else:
        file=repo.get_contents("/DUEL_new/Menu/installinfo.py")
        repo.delete_file(file.path,"player_info_deleted",file.sha)
        sys.stdout.write("\rUpdating game info  [......    ]")
        sys.stdout.flush()
        infofile=open(f"{path}\\DUEL_new\\Menu\\installinfo.py",'r')
        pinfo=infofile.read()
        infofile.close()
        repo.create_file("DUEL_new/Menu/installinfo.py","new_player_info_added",pinfo)
        sys.stdout.write("\rUpdating game info  [..........]")
        sys.stdout.flush()
        time.sleep(2)
        os.system('cls')
        quit()
