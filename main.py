import gui
import psycopg2
import threading
import netcon
import platform

def sys_check():
    system_info = platform.system()
    if system_info == "Linux":
        return 1
        
    elif system_info =="Windows":
        return 2


def main():
    sys = sys_check()
    if sys == 1:
        reciever_thread = threading.Thread(target=netcon.reciever)
        reciever_thread.start()
        sender_thread = threading.Thread(target=netcon.sender_all)
        sender_thread.start()
        sender_thread.join()
        reciever_thread.join()
        print("[SERVER] Server Ready")
    elif sys == 2:
        graphic_run = threading.Thread(target=gui.main())
        graphic_run.start()
        graphic_run.join()
        print("[APP] Client Ready")
    
    

if __name__ == "__main__":
    main()

