from tkinter import Tk, Frame, Label, Button, BOTH

class Interface(Frame):

	def __init__(self, window, **kwargs):
		Frame.__init__(self, window, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)
		self.nb_click = 0

		self.msg = Label(self, text="you don't presse the button")
		self.msg.pack()

		self.quit_button = Button(self, text="Exit", command=self.quit)
		self.quit_button.pack(side="left")

		self.click_button = Button(self, text="Click here", fg="red",
			command=self.clicking)
		self.click_button.pack(side="right")

	def clicking(self):
		self.nb_click += 1
		self.msg["text"] = "you clicked {} time".format(self.nb_click)

window = Tk()
interface = Interface(window)

interface.mainloop()
interface.destroy()
