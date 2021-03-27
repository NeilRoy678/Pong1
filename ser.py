import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostname()
port = 5555

try:
    server.bind((ip,port))
except:
    print(str(socket.error))

server.listen()
print("WAITING FOR CONNECTION ")


def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                conn.send(str.encode("BYE"))
                break
            else:
                #conn.send(str.encode(data))
                conn.sendall(str.encode(reply))
        except:
           break 
    print("CLOSED")
    conn.close()


while True:
    conn,addr = server.accept()
    print("CONNECTED TO",addr)
    thread1 = threading.Thread(target= threaded_client(conn,))
    thread1.start()