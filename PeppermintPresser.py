from tkinter import *

class Peppermint(Frame):
    def __init__(self, master):
        super(Peppermint, self).__init__(master)
        self.grid()
        self.create_window()

    def p_com(self):



    def create_window(self):
        root = Tk()
        root.geometry("600x400")

        left = Frame(root, borderwidth=2, relief="solid")
        right = Frame(root, borderwidth=2, relief="solid")
        penguin = Frame(right, borderwidth=2, relief="solid")
        polar_bear = Frame(right, borderwidth=2, relief="solid")
        christmas_tree = Frame(right, borderwidth=2, relief="solid")
        pres_mac = Frame(right, borderwidth=2, relief="solid")
        candy_for = Frame(right, borderwidth=2, relief="solid")
        eskimo = Frame(right, borderwidth=2, relief="solid")
        igloo = Frame(right, borderwidth=2, relief="solid")
        north_pole = Frame(right, borderwidth=2, relief="solid")
        ice_age= Frame(right, borderwidth=2, relief="solid")
        pluto = Frame(right, borderwidth=2, relief="solid")

        peppermint_area = Label(left, text="Peppermint Area")
        l1 = Button(penguin, command=self.p_com, text="I could be your image")
        l2 = Button(polar_bear, command=self.po_com, text="I could be your setup window")
        l3 = Button(christmas_tree, command=self.c_com, text="I could be your image")
        l4 = Button(pres_mac, command=self.pr_com, text="I could be your image")
        l5 = Button(candy_for, command=self.ca_com, text="I could be your image")
        l6 = Button(eskimo, command=self.e_com, text="I could be your image")
        l7 = Button(igloo, command=self.i_com, text="I could be your image")
        l8 = Button(north_pole, command=self.n_com, text="I could be your image")
        l9 = Button(ice_age, command=self.ice_com, text="I could be your image")
        l10 = Button(pluto, command=self.plu_com, text="I could be your image")

        left.pack(side="left", expand=True, fill="both")
        right.pack(side="right", expand=True, fill="both")

        peppermint_area.pack()
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        l7.pack()
        l8.pack()
        l9.pack()
        l10.pack()

        root.mainloop()


    '''
    def create_widgets(self):
        self.Penguin = Button(row=1, )
        self.polar_bears
        self.christmas_tree_forest
        self.present_machine
        self.candy_cane_factory
        self.Eskimo
        self.iogloo
        self.north_pole
        self.ice_age
        self.pluto
    '''



root.mainloop()



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



    def update_count(self):
        self.bttn_clicks += 1
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)

    def reset(self):
        self.bttn_clicks = 0
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)

    def add_cookies(self):
        self.bttn_clicks += 50
        self.bttn2["text"] = "Peppermints: " + str(self.bttn_clicks)



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
