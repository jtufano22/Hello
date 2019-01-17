from tkinter import *
import time

class Peppermint(Frame):
    def __init__(self, master):
        super(Peppermint, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_window()


    def create_window(self):

        photo = PhotoImage(file="peppermint11.png")

        self.count = Button(self, text="Peppermints: 0", relief=RAISED)

        self.redo = Button(self, text="Reset", command=self.reset, relief=RAISED)

        left = Frame(root, borderwidth=2, relief=RAISED)
        right = Frame(root, borderwidth=2, relief=RAISED)
        penguin = Frame(right, borderwidth=2, relief=RAISED)
        polar_bear = Frame(right, borderwidth=2, relief=RAISED)
        christmas_tree = Frame(right, borderwidth=2, relief=RAISED)
        pres_mac = Frame(right, borderwidth=2, relief=RAISED)
        candy_for = Frame(right, borderwidth=2, relief=RAISED)
        eskimo = Frame(right, borderwidth=2, relief=RAISED)
        igloo = Frame(right, borderwidth=2, relief=RAISED)
        north_pole = Frame(right, borderwidth=2, relief=RAISED)
        ice_age = Frame(right, borderwidth=2, relief=RAISED)
        pluto = Frame(right, borderwidth=2, relief=RAISED)

        self.peppermint = Button(left, image=photo, command=self.update_count)
        '''
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
        '''


        self.count.pack()
        self.redo.pack()
        '''
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
        '''
    def update_count(self):
        self.bttn_clicks += 1
        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

    def reset(self):
        self.bttn_clicks = 0
        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

root = Tk()
root.geometry("900x600")
root.title("Peppermint Presser")
app = Peppermint(root)
root.mainloop()






