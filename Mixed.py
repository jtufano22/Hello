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
        self.penguin()
        self.a = 1
        # self.p_list = []


    def create_window(self):

        p = self.penguin()
        po = self.polar()
        ch = self.christmas()
        pres = self.present()
        can = self.candy()
        esk = self.eskimo()
        ig = self.igloo()
        nor = self.north()
        ice = self.ice()
        pluto = self.pluto()

        self.photo = PhotoImage(file="peppermint11.png")

        self.count = Button(self, text="Peppermints: 0", relief=RAISED)

        self.redo = Button(self, text="Reset", command=self.reset, relief=RAISED)

        self.penguin_bttn = Button(self, text="Penguin\nCost: " + str(p[1]) + "\nLevel: "
                                              + str(p[0]), command = self.penguin, relief=RAISED)
        self.penguin_bttn.grid(row=0, column=1, sticky=W)

        self.polarbear_bttn = Button(self, text="Polar Bear\nCost: " + str(po[1]) + "\nLevel: "
                                     + str(po[0]), command=self.polar, relief=RAISED)
        self.polarbear_bttn.grid(row=1, column=1, sticky=W)

        self.christmastree_bttn = Button(self, text="Christmas tree\nCost: " + str(ch[1])
                                        + "\nLevel: " + str(ch[0]), command=self.christmas, relief=RAISED)
        self.christmastree_bttn.grid(row=2, column=1, sticky=W)

        self.presmac_bttn = Button(self, text="Present Machine\nCost: " + str(pres[1])
                                            + "\nLevel: " + str(pres[0]), command=self.present, relief=RAISED)
        self.presmac_bttn.grid(row=3, column=1, sticky=W)

        self.candyfor_bttn = Button(self, text="Candy Forest\nCost: " + str(can[1])
                                    + "\nLevel: " + str(can[0]), command=self.candy, relief=RAISED)
        self.candyfor_bttn.grid(row=4, column=1, sticky=W)

        self.eskimo_bttn = Button(self, text="Eskimo\nCost: " + str(esk[1])
                                  + "\nLevel: " + str(esk[0]), command=self.eskimo, relief=RAISED)
        self.eskimo_bttn.grid(row=5, column=1, sticky=W)

        self.igloo_bttn = Button(self, text="Igloo\nCost: " + str(ig[1])
                                  + "\nLevel: " + str(ig[0]), command=self.igloo, relief=RAISED)
        self.igloo_bttn.grid(row=6, column=1, sticky=W)

        self.northpole_bttn = Button(self, text="North Pole\nCost: " + str(nor[1])
                                  + "\nLevel: " + str(nor[0]), command=self.north, relief=RAISED)
        self.northpole_bttn.grid(row=7, column=1, sticky=W)

        self.iceage_bttn = Button(self, text="Ice Age\nCost: " + str(ice[1])
                                  + "\nLevel: " + str(ice[0]), command=self.ice, relief=RAISED)
        self.iceage_bttn.grid(row=8, column=1, sticky=W)

        self.pluto_bttn = Button(self, text="Pluto\nCost: " + str(pluto[1])
                                  + "\nLevel: " + str(pluto[0]), command=self.pluto, relief=RAISED)
        self.pluto_bttn.grid(row=9, column=1, sticky=W)

        self.peppermint = Button(self, image=self.photo, command=self.update_count)
        self.peppermint.grid(row=0, column=0, rowspan=10, sticky=W+E+N+S)

        self.count.grid()
        self.redo.grid()

    def penguin(self):

        self.pcost = 50 + self.p_up ** 3

        if self.bttn_clicks >= self.pcost:
            self.p_up += 1
            self.bttn_clicks -= self.pcost
            self.p_list = [self.p_up, self.pcost]
            self.penguin_bttn["text"] = "Penguin\nCost: " + str(self.p_list[1]) + "\nLevel: " + str(self.p_list[0])
            self.peppermint["command"] = self.penguincount()

    def polar(self):
        self.polcost = 800 + self.po_up ** 4

        if self.bttn_clicks >= self.polcost:
            self.po_up += 1
            self.pol_list = [self.po_up, self.polcost]
            self.bttn_clicks -= self.pcost
            self.polarbear_bttn["text"] ="Polar Bear\nCost: " + str(self.pol_list[1]) + "\nLevel: " + str(self.pol_list[0])

    def christmas(self):
        self.christcost = 6000 + self.ch_up ** 5

        if self.bttn_clicks >= self.christcost:
            self.ch_up += 1
            self.christ_list = [self.ch_up, self.christcost]
            self.bttn_clicks -= self.christcost
            self.christmastree_bttn["text"] = "Christmas tree\nCost: " + str(self.christ_list[1]) + "\nLevel: " + str(self.christ_list[0])

    def present(self):
        self.prescost = 45000 + self.pres_up ** 6

        if self.bttn_clicks >= self.prescost:
            self.pres_up += 1
            self.pres_list = [self.pres_up, self.prescost]
            self.bttn_clicks -= self.prescost
            self.presmac_bttn["text"] = "Present Machine\nCost: " + str(self.pres_list[1]) + "\nLevel: " + str(self.pres_list[0])

    def candy(self):
        self.cancost = 300000 + self.can_up ** 7

        if self.bttn_clicks >= self.cancost:
            self.can_up += 1
            self.can_list = [self.can_up, self.cancost]
            self.bttn_clicks -= self.cancost
            self.candyfor_bttn["text"] = "Candy Forest\nCost: " + str(self.can_list[1]) + "\nLevel: " + str(self.can_list[0])

    def eskimo(self):
        self.ecost = 5000000 + self.esk_up ** 8

        if self.bttn_clicks >= self.ecost:
            self.esk_up += 1
            self.bttn_clicks -= self.ecost
            self.esk_list = [self.esk_up, self.ecost]
            self.eskimo_bttn["text"] = "Eskimo\nCost: " + str(self.esk_list[1]) + "\nLevel: " + str(self.esk_list[0])

    def igloo(self):
        self.igcost = 375000000 + self.ig_up ** 9

        if self.bttn_clicks >= self.igcost:
            self.ig_up += 1
            self.bttn_clicks -= self.igcost
            self.ig_list = [self.ig_up, self.igcost]
            self. igloo_bttn["text"] = "Igloo\nCost: " + str(self.ig_list[1]) + "\nLevel: " + str(self.ig_list[0])

    def north(self):
        self.norcost = 6000000000 + self.nor_up ** 10

        if self.bttn_clicks >= self.norcost:
            self.nor_up += 1
            self.bttn_clicks -= self.norcost
            self.nor_list = [self.nor_up, self.norcost]
            self.northpole_bttn["text"] = "North Pole\nCost: " + str(self.nor_list[1]) + "\nLevel: " + str(self.nor_list[0])

    def ice(self):
        self.icecost = 210000000000 + self.ice_up ** 12

        if self.bttn_clicks >= self.icecost:
            self.ice_up += 1
            self.bttn_clicks -= self.icecost
            self.ice_list = [self.ice_up, self.icecost]
            self.iceage_bttn["text"] = "Ice Age\nCost: " + str(self.ice_list[1]) + "\nLevel: " + str(self.ice_list[0])

    def pluto(self):
        self.plutocost = 1000000000000 + self.pluto_up ** 14

        if self.bttn_clicks >= self.plutocost:
            self.pluto_up += 1
            self.bttn_clicks -= self.plutocost
            self.pluto_list = [self.pluto_up, self.plutocost]
            self.pluto_bttn["text"] = "Pluto\nCost: " + str(self.pluto_list[1]) + "\nLevel: " + str(self.pluto_list[0])

    def update_count(self):

        self.bttn_clicks += 1

        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

    def penguincount(self):

        self.a += 3

        self.bttn_clicks += self.a

        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)



    def reset(self):
        self.bttn_clicks = 0
        self.count["text"] = "Peppermints: " + str(self.bttn_clicks)

root = Tk()
root.geometry("900x600")
root.title("Peppermint Presser")
app = Peppermint(root)
root.mainloop()

