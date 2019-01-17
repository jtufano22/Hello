from tkinter import *
import time

class Application(Frame):
    def __init__(self,master):

        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
        self.create_widgets2()
        self.create_widgets3()
        self.create_widgets4()


    def create_widget(self):
        photo = PhotoImage(file="peppermint11.png")
        self.bttn = Button(self, image=photo)
        self.photo = photo
        self.bttn.place(x=90, y=20)
        self.bttn.grid(row=0, column=0)
        self.bttn["command"] = self.update_count


    def create_widgets2(self):
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Peppermints: 0"

        self.bttn2.place(x=40, y=40)
        self.bttn2.grid(row=8, column=90)

    def create_widgets3(self):
        self.bttn3 = Button(self)
        self.bttn3["text"] = "Redo"
        self.bttn3.grid(row=20, column= 90)
        self.bttn3.place(x=40, y=60)
        self.bttn3["command"] = self.reset

    def create_widgets4(self):
        self.bttn4 = Button(self)
        self.bttn4["text"] = "Add"
        self.bttn4.grid(row = 50, column = 90)
        self.bttn4.place(x=60, y=79)
        self.bttn4["command"] = self.add_cookies



    def update_count(self):
        self.bttn_clicks += 1
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)

    def reset(self):
        self.bttn_clicks = 0

    def add_cookies(self):
        self.bttn_clicks += 50


    # def callback():
    #     print
    #     "click!"

    # def peppermint(master):
    #     photo = PhotoImage(file="peppermint11.png")
    #     b = Button(master, image=photo, text="Click!!", height=50, width=150, compound=LEFT)
    #     b.place(x=20, y=20)

def callback(self):
    print("click!")

root = Tk()
root.title("Peppermint Clicker")
root.geometry("999x990")
app = Application(root)
root.mainloop()