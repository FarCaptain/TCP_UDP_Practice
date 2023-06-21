import socket
import threading
import random

host = "127.0.0.1" #localhost
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host, random.randint(8888, 9990))) #hopefully don't repeat
name = input("Nickname = ")

def receive():
    while True:
        try:
            message, _ =  client.recvfrom(1024)
            print(message.decode)
        except:
            pass

t = threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), (host, port))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), (host, port))