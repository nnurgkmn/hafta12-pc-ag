import socket

remote_host = socket.gethostname()
remote_port = 8881

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', remote_port))
sock.listen(5)

try:
    while True:
        newSocket, address = sock.accept()
        print("Connected from", address)

        try:
            while True:
                receivedData = newSocket.recv(1024)
                if not receivedData:
                    break
                newSocket.send(receivedData)
        except Exception as e:
            print("Hata:", e)
        finally:
            newSocket.close()
            print("Disconnected from", address)
finally:
    sock.close()
