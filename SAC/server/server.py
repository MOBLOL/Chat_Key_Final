import socket
import time
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_user = []
    
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(4)
        threading.Thread(target=self.ConnectHendler).start()
        print('Сервер запущен!')

    def ConnectHendler(self):
        while True:
            client, address = self.server.accept()
            if client not in self.all_user:
                self.all_user.append(client)
                threading.Thread(target=self.MassageHandler, args=(client,)).start()
                client.send("Вы подключены!".encode('utf-8'))
            time.sleep(2)

    def MassageHandler(self, client_socket):
        try:
            while True:
                message = client_socket.recv(1024)
                message = message.decode()
                for user in self.all_user:
                    if user != client_socket:
                        user.send(message.encode('utf-8'))
                time.sleep(1)
        except: pass



def _IpPort(ip, port):

    _ip = ip
    _port = port

    _ip = _ip.replace("\n", '')
    Server(_ip, int(_port))


#26.205.223.55