from mojang_api import Player

def accVerification():
    
    with open('C:\\Users\HomePC\Desktop\py\\Nueva carpeta\\accounts.txt', 'r') as myfile:
        data = myfile.readline()
        account = data.split(":")
        mail = str(account[0])
        pwd = str(account[1])
        print(mail)
        print(pwd)

    myUsername = ""
    player = Player(username=myUsername)
    auth = player.authenticate(mail, pwd)
    return auth

try:
    accVerification()
except Exception:
    pass

x = accVerification()

print(x)

if x[0] != False:
    print("acc")
else:
    print("no u")
