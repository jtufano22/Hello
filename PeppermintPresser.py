from tkinter import *
import time

class Peppermint(Frame):
    def __init__(self, master):
        super(Peppermint, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.p_up = 0
        self.po_up = 0
        self.ch_up = 0
        self.pres_up = 0
        self.can_up = 0
        self.esk_up = 0
        self.ig_up = 0
        self.nor_up = 0
        self.ice_up = 0
        self.pluto_up = 0
        self.create_window()


    def create_window(self):

        self.photo = PhotoImage(file="peppermint11.png")

        self.count = Button(self, text="Peppermints: 0", relief=RAISED)

        self.redo = Button(self, text="Reset", command=self.reset, relief=RAISED)

        self.penguin_bttn = Button(self, text="Penguin\nCost: " + str(self.penguin()[1]) + "\nLevel: " + str(self.penguin()[0]),
                              command=self.penguin, relief=RAISED)
        self.penguin_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.polarbear_bttn = Button(self, text="Polar Bear", relief=RAISED)
        self.polarbear_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.christmastree_bttn = Button(self, text="Christmas tree", relief=RAISED)
        self.christmastree_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.presmac_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.presmac_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.candyfor_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.candyfor_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.eskimo_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.eskimo_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.igloo_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.igloo_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.northpole_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.northpole_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.iceage_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.iceage_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.pluto_bttn = Button(self, borderwidth=2, relief=RAISED)
        self.pluto_bttn.grid(row=0, column=1, rowspan=1, sticky=E+N)

        self.peppermint = Button(self, image=self.photo, command=self.update_count)
        self.peppermint.grid(row=0, column=0, rowspan=10, sticky=W+E+N+S)

        self.count.grid()
        self.redo.grid()

    def penguin(self):
        if
            self.p_up += 0
            self.pcost = 50 + self.p_up ** 3
            self.p_list = [self.p_up, self.pcost]
            return self.p_list

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn_clicks += self.penguin()[0] * 3

        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

    def reset(self):
        self.bttn_clicks = 0
        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

root = Tk()
root.geometry("900x600")
root.title("Peppermint Presser")
app = Peppermint(root)
root.mainloop()






