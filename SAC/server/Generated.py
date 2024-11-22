import os
import random

abc = "абвгдеёжзийклмнопрстуфхцчщъыьэюя1234567890qwertyuiopasdfghjklzxcvbnmАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯQWERTYUIOPASDFGHJKLZXCVBNM!*/-+@#%$№ ."
abc_arr, new_arr = list(abc), list(abc)

def GenerateProv(ip, port, name):
    try:
        provile = open('..\client\Provile.txt', 'w')
        provile.write('')


        if ip == 'Адрес сервера...':
            ip = '127.0.0.1'

        if port == "Порт сервера...":
            port = 2024

        if name == 'Имя...':
            name = '__NoName__'

        if port != None or ip != None or name != None :
            provile.write(f'{ip}\n{port}\n{name}')
            provile.close()
        else:
            provile.close()
            return None

    except: return False
def GenerateKey():
    for i in new_arr * random.randint(5, 15):
        elemein_1 = int(random.randint(0, 136))
        elemein_2 = int(random.randint(0, 136))

        new_arr[elemein_1], new_arr[elemein_2] = new_arr[elemein_2], new_arr[elemein_1]
    key = ""

    for i in new_arr:
        key = f'{key}{i}'

    try:
        data = open('SAC\server\Key.txt', 'w')
        data.write('')
        data.write(key)
        data.close()
    except:

        return None

def ServerDataStartedWrite(ip, port):
    try:
        data = open('SAC\server\Data.txt', 'w')

        data.write('')
        if port == None:
            data.write(f'{ip}\n{ServerDataStartedReed(2, True)}')
            data.close()
        elif ip == None:
            data.write(f'{ServerDataStartedReed(1, True)}\n{port}')
            data.close()

        elif port != None or ip != None:
            data.write(f'{ip}\n{port}')
            data.close()
        else:
            data.close()
            return None

    except: return False

def ServerDataStartedReed(oper=0, folder=False):
    if folder == True:
        folder = 'Data.txt'
    elif oper == 3:
        folder = "Provile.txt"
    else:
        folder = ''
    data = open(f'{folder}', 'r')
    file = data.readlines()
    data.close()
    try:


        if oper != 0:
            if oper == 1:
                ip = file[0].split('\n')[0]
                return ip
            elif oper == 2:
                port = str(file[1])
                return port

            elif oper == 3:
                ip, port, name = file[0], file[1], file[2]
                return ip, port, name

        else:
            ip = file[0]
            port = int(file[1])

            return ip, port

    except:
        return False, False, print("ERROR")
