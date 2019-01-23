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
        self.a = 0
        self.c = 1
        # autoclickers = 0
        # autoclickerspurchased = False
        self.comments()
        self.upgrader1 = 0
        self.autoclicker1()




    def create_widget(self):
        photo = PhotoImage(file="peppermint11.png")
        self.bttn = Button(self, image=photo)
        self.photo = photo
        # self.bttn.place(x=90, y=20)
        self.bttn.grid(row=0, column=0)
        self.bttn["command"] = self.update_count


    def create_widgets2(self):
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Peppermints: 0"

        # self.bttn2.place(x=40, y=40)
        self.bttn2.grid(row=1, column=0)

    def create_widgets3(self):
        self.bttn3 = Button(self)
        self.bttn3["text"] = "Redo"
        self.bttn3.grid(row=2, column= 0)
        # self.bttn3.place(x=40, y=60)
        self.bttn3["command"] = self.reset

    def create_widgets4(self):
        self.bttn4 = Button(self)
        self.bttn4["text"] = "Add"
        self.bttn4.grid(row = 3, column = 0)
        # self.bttn4.place(x=60, y=79)
        self.bttn4["command"] = self.add_cookies
    #
    def comments(self):
        self.bttn4 = Button(self)
        self.bttn4["text"] = "Comments"
        self.bttn4.grid(row=4, column=0)

    def autoclicker1(self):


        self.autobttn = Button(self)
        self.a = 50

        # self.autobttn["text"] = "Auto: Cost " + str(self.a)
        self.autobttn.grid(row = 5, column = 0)
        if self.upgrader1 != 7:
            self.autobttn["command"] = self.enough1
            self.autobttn["text"] = "Auto: Cost " + str(self.a)
        else:
           self.autobttn["text"] = "Done! No more upgrades!"


    def enough1(self):



        if self.upgrader1 == 0:
            self.a = 50
        elif self.upgrader1 >= 1:
            self.a *= 2
            # self.autobttn["text"] = "Auto: Cost " + str(self.a)



        if self.bttn_clicks < self.a:
            self.bttn4["text"] = "Sorry Not enough peppermints!"
            self.a /= 2
        if self.bttn_clicks >= self.a:
            self.bttn4["text"] = "Purchased!"
            self.bttn_clicks -= self.a
            self.upgrader1 += 1
            self.autobttn["text"] = "Auto: Cost " + str(self.a*2)

        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)
        # self.autobttn["text"] = "Auto: Cost " + str(self.a)





    def update_count(self):

        if self.upgrader1 == 0:
            self.bttn_clicks += self.c

        if self.upgrader1 == 1:
            self.bttn_clicks += 3

        if self.upgrader1 == 2:
            self.bttn_clicks += 6

        if self.upgrader1 == 3:
            self.bttn_clicks += 9

        if self.upgrader1 == 4:
            self.bttn_clicks += 12

        if self.upgrader1 == 5:
            self.bttn_clicks += 15

        if self.upgrader1 == 6:
            self.bttn_clicks += 3

        # self.bttn_clicks += 1
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)



    def reset(self):
        self.bttn_clicks = 0
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)

    def add_cookies(self):
        self.bttn_clicks += 50
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)


    # def autoclick(self):
    #     global master
    #     global click
    #     global autoclickers
    #     click += autoclickers  # get clicks from autoclickers
    #     master.after(1000, autoclick)  # do this again 1 second later
    #


    # def callback():
    #     print
    #     "click!"

    # def peppermint(master):
    #     photo = PhotoImage(file="peppermint11.png")
    #     b = Button(master, image=photo, text="Click!!", height=50, width=150, compound=LEFT)
#     #     b.place(x=20, y=20)
#
# def callback(self):
#     print("click!")

root = Tk()
root.title("Peppermint Clicker")
root.geometry("999x990")
app = Application(root)
app.mainloop()
