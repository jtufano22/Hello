from tkinter import *

class Peppermint(Frame):
    def __init__(self, master):
        super(Peppermint, self).__init__(master)
        self.grid()
        self.create_window()

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

        label2 = Label(left, text="Peppermint Area")
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

        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()

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


