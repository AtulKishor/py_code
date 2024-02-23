import tkinter

win = tkinter.Tk()
win.title("A game Layout")
win.minsize(width=500,height=500)
win.config(padx=20,pady=20)

label = tkinter.Label(text="Button game")
label.grid(column=4,row=0)

for i in range(3,6):
    for j in range(3,6):
        b = tkinter.Button(text=f'Button {(i,j)}')
        b.grid(column=i,row=j)
        b.config(padx=10,pady=10)

win.mainloop()