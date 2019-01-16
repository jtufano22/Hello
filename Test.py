from tkinter import *


class Application(Frame):
    def __init__(self,master):

        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
        self.create_widgets2()


    def create_widget(self):
        photo = PhotoImage(file="peppermint11.png")
        self.bttn = Button(self, image=photo)
        self.photo = photo
        self.bttn.place(x=20, y=20)
        self.bttn.grid(row=0, column=0)
        self.bttn["command"] = self.update_count


    def create_widgets2(self):
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Total Clicks: 0"

        self.bttn2.place(x=40, y=40)
        self.bttn2.grid(row=0, column=3)



    def update_count(self):
        self.bttn_clicks += 1
        self.bttn2["text"] = "Total Clicks: " + str(self.bttn_clicks)

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
root.title("Click Counter")
root.geometry("600x400")
app = Application(root)
root.mainloop()