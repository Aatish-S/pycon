import socket
from psd_tools import  PSDImage
from tkinter.filedialog import askopenfile

def necon():
    global FORMAT ,PORT ,SIZE
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 4455
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SIZE = 1024
    FORMAT = "utf-8"
    s.bind(IP,PORT)
    s.listen()
    while True:
        listen_frame(s)

def listen_frame(self):
    sc, address = self.accept()
    print(f"[SERVER]CONNECTION FROM {address} HAS BEEN ESTABLISHED")
    sc.send(bytes("WELCOME","utf-8"))    
    
def send_frame(self,select):
    opt = ['[SERVER]','[APPLIC]','[DATABS]','[IMAGES]','[]']
    sc , address = self.accept()
    sc.send(bytes(opt[select],FORMAT))


def receiver():
    IP = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((IP,PORT))
    s.listen()
    while True:
        clsocket, address = s.accept()
        print(f"[SERVER]CONNECTION FROM {address} HAS BEEN ESTABLISHED")
        clsocket.send(bytes("WELCOME","utf-8"))

def file_send(self):
    file_dir = askopenfile()
    f = open(file_dir,'wb')
    i = i+1
    sc, address = self.accept()
    while True:
        l = sc.recv(1024)
        while(l):
            f.write(l)
            l = sc.recv(1024)
    f.close()
    sc.close()
    
def file_recv(self):
    f = open("") 

def psd_thumbnail():
    #PSDImage.open(psdfile).thumbnail().save(new_file_name)
    print("")

def tiff_thumbnail():
    print("")

def file_transfer(psdfile):
    print("FILE TRANSFER ",psdfile)
    print("")


if __name__ == "__main__":
    necon()