from tkinter import *
# import tkinter as tk
# from PIL import Image, ImageTk
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

    # --- functions ---

    # def on_click(event=None):
    #     # `command=` calls function without argument
    #     # `bind` calls function with one argument
    #     print("image clicked")

    # # --- main ---
    #
    # # init
    # root = tk.Tk()
    #
    # # load image
    # image = Image.open("Peppermint.png")
    # photo = ImageTk.PhotoImage(image)
    #
    # # label with image
    # l = tk.Label(root, image=photo)
    # l.pack()
    #
    # # bind click event to image
    # l.bind('<Button-1>', on_click)
    #
    # # button with image binded to the same function
    # b = tk.Button(root, image=photo, command=on_click)
    # b.pack()
    #
    # # button with text closing window
    # b = tk.Button(root, text="Close", command=root.destroy)
    # b.pack()
    #
    # # "start the engine"
    # root.mainloop()
    #
    # # def penguin_clicker(self):
  class fe:
    def __init__(self,master):
      self.b=Button(master,justify = LEFT)
      photo=PhotoImage(file="mine32.gif")
      self.b.config(image=photo,width="10",height="10")
      self.b.pack(side=LEFT)

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()


root = Tk()
root.title("PeppermintPresser")
root.geometry("1000x500")
app = Application(root)
root.mainloop()