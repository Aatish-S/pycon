from base64 import decode
from tkinter.filedialog import askopenfilename
import socket
import sys
import time

def necon():
   global FORMAT,SIZE,PORT
   IP = socket.gethostbyname(socket.gethostname())
   PORT = 4455
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   SIZE = 1024
   FORMAT = "utf-8"
   s.bind((IP,PORT))
   s.listen(10)                              #accepts atleast 10 connections
   while True:
      listen_frame(s)

def file_send(self,filename):
   f = open(filename,'rb')
   l = f.read(1024)
   while(l):
      self.send(l.encode("utf-8"))
      l = f.read(1024)
   f.close()

def listen_frame(self):
    sc, address = self.accept()
    print(f"[SERVER]CONNECTION FROM {address} HAS BEEN ESTABLISHED")
    sc.send(bytes("WELCOME","utf-8")) 
    a = sc.recv(SIZE)
    print(a.decode("utf-8"))

if __name__ == "__main__":
   necon()