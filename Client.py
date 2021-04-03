import socket
from _thread import *
import sys

server = "192.168.1.12"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def read(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(335,475),(335,480)]

def threaded_client(conn, player):
    conn.sendall(str.encode(make(pos[player])))
    reply = ""
    while True:
        try:
            data = read(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

cp = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, cp))
    cp += 1
