import tkinter as tk
from tkinter.filedialog import askopenfilename
import netcon
from tkinter import messagebox
from pathlib import Path


LARGE_FONT= ("Verdana", 12)


class pycon(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Fabric_entry,Design_upload,Print_queue,Pending_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Fabric_entry)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class Fabric_entry(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        option = ["Production","Sampling","Saree"]
        client_name = tk.StringVar()
        fabric_amount = tk.StringVar()
        work_role = tk.StringVar()
        client_name.set("")
        fabric_amount.set("")
        button = tk.Label(self,text="Fabric Entry")
        button.place(x=45,y=75)

        button2 = tk.Button(self, text="Design Upload",command=lambda: controller.show_frame(Design_upload))
        button2.place(x=135,y=70)

        button3 = tk.Button(self, text = "Print Queue", command=lambda: controller.show_frame(Print_queue))
        button3.place(x=255,y=70)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))

        button4.place(x=360,y=70)

        client_nametag = tk.Label(self,text="Client Name:").place(x=30,y=200)
        cl_name = tk.Entry(self,textvariable=client_name).place(x = 110,y = 200)
        fb_title = tk.Label(self,text="Fabric Amount:").place(x=30,y=270)
        fb_amount = tk.Entry(self,textvariable=fabric_amount).place(x = 160,y = 270)
        work_tag = tk.Label(self,text="Work Role:").place(x=30,y=235)

        

        work_role.set(option[0])
        dpdown = tk.OptionMenu(self,work_role,*option)
        dpdown.place(x=110,y=230)

        fb_entry_button = tk.Button(self,text="Submit",command=lambda:Fabric_entry.get_val(client_name,fabric_amount,work_role))
        fb_entry_button.place(x=100,y=320)
    
    def get_val(client_name,fabric_amount,work_role):
        clientele = client_name.get()
        fb_amount = fabric_amount.get()
        role = work_role.get()
        print(client_name.get(),fabric_amount.get(),work_role.get())


class Design_upload(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2 = tk.Button(self, text="Fabric Entry",command=lambda: controller.show_frame(Fabric_entry))
        button2.place(x=35,y=70)

        des_lab = tk.Label(self,text = "Design Upload")
        des_lab.place(x=150,y=75)

        button3 = tk.Button(self, text = "Print Queue", command=lambda: controller.show_frame(Print_queue))
        button3.place(x=255,y=70)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))

        button4.place(x=360,y=70)

        file_select = tk.Button(self,text="Select File",command=lambda:Design_upload.file_send())
        file_select.place(x=110,y=230)

    def file_send():
        psdf = askopenfilename()
        psdfile = Path(psdf).stem
        if psdfile.endswith('.pdf'):
            netcon.file_transfer(psdfile)
        elif psdfile.endswith('.txt'):
            netcon.file_transfer(psdfile)
        else:
            messagebox.showerror("File Error!","Please select a PSD File.")
            print(psdfile)

class Print_queue(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        button2 = tk.Button(self, text="Fabric Entry",command=lambda: controller.show_frame(Fabric_entry))
        button2.place(x=35,y=70)

        des_lab = tk.Button(self,text = "Design Upload",command=lambda: controller.show_frame(Design_upload))
        des_lab.place(x=140,y=70)

        button3 = tk.Label(self, text = "Print Queue")
        button3.place(x=270,y=75)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))

        button4.place(x=360,y=70)
        
class Pending_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button2 = tk.Button(self, text="Fabric Entry",command=lambda: controller.show_frame(Fabric_entry))
        button2.place(x=35,y=70)

        des_lab = tk.Button(self,text = "Design Upload",command=lambda: controller.show_frame(Design_upload))
        des_lab.place(x=140,y=70)

        button3 = tk.Button(self, text = "Print Queue",command=lambda: controller.show_frame(Print_queue))
        button3.place(x=265,y=70)

        button4 = tk.Label(self, text="Pending")

        button4.place(x=370,y=75)


def main():
    app = pycon()
    app.geometry('600x600')
    app.title("PYCON")
    app.mainloop()   

if __name__ == "__main__":
    main()

