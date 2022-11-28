import socket

PORT = 4455
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()
print("[LISTENING] Server is listening.")
print(IP)
while True:
        conn, addr = s.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        file.close()
        conn.send("File received".encode(FORMAT))
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

