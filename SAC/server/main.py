import MenuCreator
from MenuCreator import CreateMenu
from os import system
from time import sleep
from server import _IpPort
from Generated import *



def ShowMenu():
    global is_stop_menu
    is_stop_menu = False
    Menu = CreateMenu(title="Меню серверв", elements=[
        'Запустить сервер',
        'Изменить IP',
        'Изменить Port',
        'Изменить ключ шифрации'
    ])

    Menu.load_menu()

    Menu.wait(is_stop_menu)

    if Menu.get_selected_item() == 0:
        print()
        system('cls')
        is_stop_menu = True
        ip, port = ServerDataStartedReed(0, True)
        MenuCreator.MenuCreator.is_stoped = True
        _IpPort(ip, port)

    elif Menu.get_selected_item() == 3:
        input()
        system('cls')
        is_key = input("Желаете изменить ключ? Y/n")
        if is_key == "Y" or "y":
            print()
            system('cls')
            GenerateKey()
            print("Новый пароль сгенерирован!")
            sleep(2)
            ShowMenu()
        else:
            system('cls')
            sleep(1)
            ShowMenu()

    elif Menu.get_selected_item() == 1:
        input()
        system('cls')
        ip = input("Введите новый IP: ")
        ServerDataStartedWrite(ip, None)
        sleep(1)
        ShowMenu()

    elif Menu.get_selected_item() == 2:
        input()
        system('cls')
        port = input("Введите новый Port: ")
        print(port)
        ServerDataStartedWrite(None, port)
        sleep(1)
        ShowMenu()



system('cls')
ShowMenu()
