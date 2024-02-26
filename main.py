from replit import db
import datetime, os, time ,random

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break

def createUser():
  userName = input("Username: ")
  Password = input("Password: ")
  salt = random.randint(1000,9999)
  hashPass = f"{Password}{salt}"
  hashPass = hash(hashPass)
  db[userName] = {"password":hashPass, "salt": salt}
  print("User Added")

if len(db.keys()) == 0:
    print("It's the first time let's Sign Up")
    createUser()

else:
  userName = input("Username: ")
  Password = input("Password: ")
  salt = db[userName]["salt"]
  hashPass = f"{Password}{salt}"
  hashPass = hash(hashPass)
  if hashPass == db[userName]["password"]:
    print("Login Successful")
  else:
    print("Incorrect")
    exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()