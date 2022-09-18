import tkinter as tk


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

    def saree_no(self,work_imp):
        option = work_imp.get()
        if option == "Saree":
            sar_tot = tk.Entry(self).place(x=300,y=300)
            sar_lab = tk.Label(self,text="No. of Sarees").place(x=300,y=300)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        option = ["Production","Sampling","Saree"]
        button = tk.Label(self,text="Fabric Entry")
        button.place(x=45,y=75)

        button2 = tk.Button(self, text="Design Upload",command=lambda: controller.show_frame(Design_upload))
        button2.place(x=135,y=70)

        button3 = tk.Button(self, text = "Print Queue", command=lambda: controller.show_frame(Print_queue))
        button3.place(x=255,y=70)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))

        button4.place(x=360,y=70)

        client_name = tk.Label(self,text="Client Name:").place(x=30,y=200)

        cl_name = tk.Entry(self).place(x = 110,y = 200)
        fb_title = tk.Label(self,text="Fabric Amount:").place(x=30,y=270)
        fb_amount = tk.Entry(self).place(x = 160,y = 270)


        work_tag = tk.Label(self,text="Work Role:").place(x=30,y=235)
        work_imp = tk.StringVar()
        work_imp.set(option[0])
        dpdown = tk.OptionMenu(self,work_imp,*option,command=Fabric_entry.saree_no(self,work_imp))
        dpdown.place(x=110,y=230)

        fb_entry_button = tk.Button(self,text="Submit")
        fb_entry_button.place(x=100,y=320)



        
        


class Design_upload(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2 = tk.Button(self, text="Fabric Entry",command=lambda: controller.show_frame(Fabric_entry))
        button2.pack(side=tk.LEFT)

        button3 = tk.Button(self, text = "Print Queue", command=lambda: controller.show_frame(Print_queue))
        button3.pack(side=tk.LEFT)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))
        
        button4.pack(side=tk.LEFT)


class Print_queue(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        button = tk.Button(self, text="Fabric Logging",command=lambda: controller.show_frame(Fabric_entry))
        button.pack(side=tk.LEFT)

        button3 = tk.Button(self, text = "Design Upload", command=lambda: controller.show_frame(Design_upload))
        button3.pack(side=tk.LEFT)

        button4 = tk.Button(self, text="Pending", command=lambda: controller.show_frame(Pending_page))
        
        button4.pack(side=tk.LEFT)
        
class Pending_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        button = tk.Button(self, text="Fabric Logging",command=lambda: controller.show_frame(Fabric_entry))
        button.pack(side=tk.LEFT)

        button3 = tk.Button(self, text = "Design Upload", command=lambda: controller.show_frame(Design_upload))
        button3.pack(side=tk.LEFT)

        button4 = tk.Button(self, text="Print Queue", command=lambda: controller.show_frame(Print_queue))
        
        button4.pack(side=tk.LEFT)

def main():
    app = pycon()
    app.geometry('800x600')
    app.title("PYCON")
    app.mainloop()   

if __name__ == "__main__":
    main()

