# from tkinter import *
# #
# # class Application(Frame):
# #     def __init__(self,master):
# #
# #         super(Application, self).__init__(master)
# #         self.grid()
# #         self.bttn_clicks = 0
# #         self.create_widget()
# #
# #         def create_widget(self):
# #         self.bttn = Button(self)
# #         self.bttn["text"] = "Total Clicks: 0"
# #         self.bttn["command"] = self.update_count
# #         self.bttn.grid()
# #
# #     def update_count(self):
# #         self.bttn_clicks += 1
# #         self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
# #
# #
# # root = Tk()
# # root.title("Click Counter")
# # root.geometry("200x50")
# # app = Application(root)
# # root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title ('iMedic')
canvas = Canvas(root, width = 1600, height = 250)


canvas.pack(fill = BOTH, expand = True)
photo = PhotoImage(file = './logo.gif')
canvas.create_image(55, 55, image=photo)
canvas.create_text(600, 155, text = 'Welcome', font = ('Helvetica', 72, 'bold'), justify = 'center', fill='blue')
canvas.update

# Make panewindow child of root
panewindow = ttk.Panedwindow(root, orient = VERTICAL)
panewindow.pack(fill = BOTH, expand = True)

# paitents_frame with Labels in it
paitents_frame = ttk.Frame(panewindow, width = 1600, height = 400, relief = RAISED)
paitents_label1 = Label(paitents_frame, text="Name Label")
paitents_label1.pack()
paitents_label2 = Label(paitents_frame, text="Name Label")
paitents_label2.pack()

# prescription_frame with Labels in it
prescription_frame = ttk.Frame(panewindow, width = 1600, height = 300, relief = RAISED)
prescription_label1 = Label(prescription_frame, text="Prescription Text")
prescription_label1.pack()
prescription_label2 = Label(prescription_frame, text="Prescription Text")
prescription_label2.pack()

# Add the frames to panewindow
panewindow.add(paitents_frame, weight = 1)
panewindow.add(prescription_frame, weight = 1)

root.mainloop()