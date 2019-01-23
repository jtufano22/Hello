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

        self.polarbear_bttn = Button(self, text="Polar Bear\nCost: " + str(self.polar()[1]) + "\nLevel: "
                                     + str(self.polar()[0]), command=self.polar, relief=RAISED)
        self.polarbear_bttn.grid(row=0, column=2, rowspan=1, sticky=E+N)

        self.christmastree_bttn = Button(self, text="Christmas tree\nCost: " + str(self.christmas()[1])
                                        + "\nLevel: " + str(self.christmas()[0]), command=self.christmas, relief=RAISED)
        self.christmastree_bttn.grid(row=0, column=3, rowspan=1, sticky=E+N)

        self.presmac_bttn = Button(self, text="Present Machine\nCost: " + str(self.present()[1])
                                            + "\nLevel: " + str(self.present()[0]), command=self.present, relief=RAISED)
        self.presmac_bttn.grid(row=0, column=4, rowspan=1, sticky=E+N)

        self.candyfor_bttn = Button(self, text="Candy Forest\nCost: " + str(self.candy()[1])
                                    + "\nLevel: " + str(self.candy()[0]), command=self.candy, relief=RAISED)
        self.candyfor_bttn.grid(row=0, column=5, rowspan=1, sticky=E+N)

        self.eskimo_bttn = Button(self, text="Eskimo\nCost: " + str(self.eskimo()[1])
                                  + "\nLevel: " + str(self.eskimo()[0]), command=self.eskimo, relief=RAISED)
        self.eskimo_bttn.grid(row=0, column=6, rowspan=1, sticky=E+N)

        self.igloo_bttn = Button(self, text="Igloo\nCost: " + str(self.igloo()[1])
                                  + "\nLevel: " + str(self.igloo()[0]), command=self.igloo, relief=RAISED)
        self.igloo_bttn.grid(row=0, column=7, rowspan=1, sticky=E+N)

        self.northpole_bttn = Button(self, text="North Pole\nCost: " + str(self.north()[1])
                                  + "\nLevel: " + str(self.north()[0]), command=self.north, relief=RAISED)
        self.northpole_bttn.grid(row=0, column=8, rowspan=1, sticky=E+N)

        self.iceage_bttn = Button(self, text="Ice Age\nCost: " + str(self.ice()[1])
                                  + "\nLevel: " + str(self.ice()[0]), command=self.ice, relief=RAISED)
        self.iceage_bttn.grid(row=0, column=9, rowspan=1, sticky=E+N)

        self.pluto_bttn = Button(self, text="Pluto\nCost: " + str(self.pluto()[1])
                                  + "\nLevel: " + str(self.pluto()[0]), command=self.pluto, relief=RAISED)
        self.pluto_bttn.grid(row=0, column=10, rowspan=1, sticky=E+N)

        self.peppermint = Button(self, image=self.photo, command=self.update_count)
        self.peppermint.grid(row=0, column=0, rowspan=10, sticky=W+E+N+S)

        self.count.grid()
        self.redo.grid()

    def penguin(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

    def polar(self):
        self.polcost = 800 + self.po_up ** 4
        self.po_up += 1
        self.pol_list = [self.po_up, self.polcost]
        return self.pol_list

    def christmas(self):
        self.christcost = 6000 + self.ch_up ** 5
        self.ch_up += 1
        self.christ_list = [self.ch_up, self.christcost]
        return self.christ_list

    def present(self):
        self.prescost = 45000 + self.pres_up ** 6
        self.pres_up += 1
        self.pres_list = [self.pres_up, self.prescost]
        return self.pres_list

    def candy(self):
        self.cancost = 300000 + self.can_up ** 7
        self.can_up += 1
        self.can_list = [self.can_up, self.cancost]
        return self.can_list

    def eskimo(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

    def igloo(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

    def north(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

    def ice(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

    def pluto(self):
        self.pcost = 50 + self.p_up ** 3
        self.p_up += 1
        self.p_list = [self.p_up, self.pcost]
        return self.p_list

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






