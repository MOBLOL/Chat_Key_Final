

import requests

from getpass import getuser

from rich import print as rprint

from rich.panel import Panel
from server.server import _IpPort
import threading

from rich.layout import Layout
from server.Generated import ServerDataStartedReed

from datetime import datetime
ip, port = ServerDataStartedReed(0, True)

def wifi_test():
    try:
        requests.head("http://www.google.com/", timeout=1)
        style_wifi = "green"
        text_wifi = "Подключено"
        return style_wifi, text_wifi
    except:
        style_wifi = "red"
        text_wifi = "Отключено"
        return style_wifi, text_wifi

layout = Layout(name="main")

layout["main"].split_row(
    Layout(name="Info"),
    Layout(name="Users"),
)

layout["Info"].split(
    Layout(name="WiFi"),
    Layout(name="Version Server"),
    Layout(name="Data")
)

style_wifi, text_wifi = wifi_test()


layout["WiFi"].split(
    Layout(Panel(f"                  [uu bold]Информация о WiFI[/]\n\nWi-Fi соединение: \n[{style_wifi}]{text_wifi}[/{style_wifi}] \n"
                 f"IP сети: {ServerDataStartedReed(1, True)} \n"
                 f"PORT сети: {ServerDataStartedReed(2, True)}\n"
                 f"В дальнейшем тут будет больше информации.")),
)

layout["Version Server"].split(
    Layout(Panel("              [uu bold]Дополнительная информация[/] \nВерсия сервера: Development-pre-release: 0.2v\n"
                 "Дата создания версии: 00:00:0000\n"
                 f"Пользователь сервера: \"{getuser()}\"\n"
                 f"В дальнейшем тут будет больше информации."))


)

layout["Data"].split(
    Layout(Panel(f"        Данные сервера: \n"
                 f"Время запуска: {datetime.now()}\n\n"
                 f"В дальнейшем тут будет больше информации."))
)

rprint(layout)


s = threading.Thread(target=_IpPort, args=(ip, int(port)))
s.start()


