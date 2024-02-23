import tkinter

win = tkinter.Tk()
win.title("korean")
win.minsize(500,500)

#label
label = tkinter.Label(text="I am a label",font=("Times New Roman",24,"bold"))
label.place(x=10,y=10)
# label.pack()

def onClick():
    label.config(text=t.get())
    print(inp.get("1.0",tkinter.END))

# button
b = tkinter.Button(text="Click me",command=onClick)
b.pack(side="left")

# text field
t = tkinter.Entry(width=10)
t.insert(tkinter.END, "Text Box")
t.pack()

# text area
inp = tkinter.Text(width=30,height=3)
inp.focus()
inp.pack()

# spin box
def spinbox_used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

# slider/scale
def scale_used(value):
    print(scale.get())
scale = tkinter.Scale(from_=0,to=100,command=scale_used)
scale.pack()

# check box
def check_button_used():
    print(check_var.get())
check_var = tkinter.IntVar()
check_button = tkinter.Checkbutton(variable=check_var,command=check_button_used,text="Item")
check_button.pack()

# radio button
def radio_used():
    print(radio_var.get())
radio_var = tkinter.IntVar()
radio = [tkinter.Radiobutton(variable=radio_var,command=radio_used,text="1 st button",value=1),
 tkinter.Radiobutton(variable=radio_var,command=radio_used,text="2nd button",value=2),
 tkinter.Radiobutton(variable=radio_var,command=radio_used,text="3rd button",value=3),
 tkinter.Radiobutton(variable=radio_var,command=radio_used,text="4th button",value=4)
]
for i in radio:
    i.pack()

# List Box
def list_box_used(event):
    print(lbox.get(lbox.curselection()))
lbox = tkinter.Listbox(height=4)
for i in range(4):
    lbox.insert(i,f'fruit {i}')
lbox.bind("<<ListboxSelect>>", list_box_used)
lbox.pack()
win.mainloop()