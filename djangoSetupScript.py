import os
import time
VENV_ACTIVATE = "source venv/bin/activate"



def main():
    path = input("Path> ")
    os.chdir(f"{path}")
    createFolder()
    createVirtualEnv()
    startDjangoProject()
    startDjangoApp()
    createFirstTemplate()
    startVsCode()
    

def createFolder():
    folder_name = input("project DIR name> ")
    os.system(f"mkdir {folder_name}")
    os.chdir(f"./{folder_name}")    

def createVirtualEnv():
    os.system("python3 -m venv venv")

def startDjangoProject():
    os.system(f"{VENV_ACTIVATE}; pip3 install django")
    os.system(f"{VENV_ACTIVATE}; django-admin startproject core")

    project_name = input("django project name> ")
    os.system(f"mv core {project_name}")
    time.sleep(3)
    os.chdir(f"./{project_name}")
    os.system(f"mkdir apps")

def startDjangoApp():
    app_name = input("app name> ")
    os.system(f"mkdir apps")
    os.chdir("./apps")
    os.system(f"touch __init__.py")
    os.system(f"django-admin startapp {app_name}")


def createFirstTemplate():
    os.chdir("..")
    os.system(f"mkdir templates")
    os.chdir("./templates")
    os.system(f"touch index.html")

def startVsCode():
    os.chdir("..")
    os.chdir("..")
    os.system('code .')


main()