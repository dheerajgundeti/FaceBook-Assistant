import tkinter as tk
from tkinter import font  as tkfont
from helpers import *
import threading


class FaceBookAssistant(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, MessagePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="FaceBook Assistant", font=controller.title_font)
        label.pack(pady=20)

        l1=tk.Label(self,text="UserName : ")
        l1.pack()
        self.email = tk.Entry(self, width=30)
        self.email.pack(pady=10)
        l2 = tk.Label(self, text="Password : ")
        l2.pack()
        self.password = tk.Entry(self, width=30)
        self.password.pack(pady=10)
        login = tk.Button(self, text="Login", command=self.login_fb)
        login.pack()

    def login_fb(self):
        username=self.email.get()
        passwrd=self.password.get()
        self.controller.show_frame("MessagePage")
        login_facebook(username,passwrd)

class MessagePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.welcomeMessage = tk.Label(self, text="Hi.. use text/voice", font=controller.title_font)
        self.welcomeMessage.pack(side="top", fill="x", pady=20)
        l1 = tk.Label(self, text="Command : ")
        l1.pack()
        self.command = tk.Entry(self, width=30)
        self.command.pack()
        button = tk.Button(self, text="Show",command=self.process_command)
        button.pack(pady=10)
        speech = tk.Button(self, text="-Command By Voice-", command=self.process_voicecommand)
        speech.pack()
        self.MessageBox = tk.Text(self, height=10, width=30)
        self.MessageBox.pack(pady=10)

    def process_command(self):
        process(self.command.get(),self.MessageBox)

    def process_voicecommand(self):
        command=voice()
        process(command,self.MessageBox)




def startApplication():
    application = FaceBookAssistant()
    application.geometry('600x400')
    application.mainloop()

if __name__ == "__main__":
    startApplication()