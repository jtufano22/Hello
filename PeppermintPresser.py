from tkinter import *
import time

class Application(Frame):
    def __init__(self,master):

        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.cursor_clicker()

    def cursor_clicker(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

    def penguin_clicker(self):
