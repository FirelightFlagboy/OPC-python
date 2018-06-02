from tkinter import Label, Frame, Button, Checkbutton, Radiobutton, Listbox,\
	Tk, StringVar, IntVar, Entry, END, X, BOTH

#create a window
window = Tk()

# create a label (text line)
text_label = Label(window, text="hello tkinter !")
# display the label in the windows
text_label.pack()

# create a text zone
var_text = StringVar()
line_text = Entry(window, textvariable=var_text, width=30)
line_text.pack()

# create a check zone
var_case = IntVar()
case = Checkbutton(window, text="don't ask this question",
	variable=var_case)
case.pack()

# create a radio button
var_choice = StringVar()

red_choice = Radiobutton(window, text="red", variable=var_choice,
	value="red")
blue_choice = Radiobutton(window, text="blue", variable=var_choice,
	value="blue")
green_choice = Radiobutton(window, text="green", variable=var_choice,
	value="green")

red_choice.pack()
blue_choice.pack()
green_choice.pack()

# create a listbox
liste = Listbox(window)

liste.insert(END, "hy")
liste.insert(END, "i'm")
liste.insert(END, "rock")
liste.insert(END, "baby")

liste.pack()

# create a frame
frame = Frame(window, width=768, height=576, borderwidth=1)
frame.pack(fill=BOTH)

msg = Label(frame, text="our window")
msg.pack(side="top", fill=X)

# create a button to quit the window
exit_button = Button(window, text="exit", command=window.quit)
exit_button.pack()

# begin the loop Tkinter
window.mainloop()
