from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Tic Tac Toe")

# top.geometry("241x258")
turn = True


def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def click(b):
    global turn
    if b["text"] == " " and turn == True:
        b["text"] = "X"
        turn = False
        winner()

    elif b["text"] == " " and turn == False:
        b["text"] = "O"
        turn = True
        winner()

    else:
        messagebox.showinfo("Tic Tac Toe", "This is an invalid move \n Try Again")


def winner():
    global win
    win = False
    if b1["text"] == b2["text"] == b3["text"] == "X":
        b1.config(bg="pink")
        b2.config(bg="pink")
        b3.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b4["text"] == b5["text"] == b6["text"] == "X":
        b4.config(bg="pink")
        b5.config(bg="pink")
        b6.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b7["text"] == b8["text"] == b9["text"] == "X":
        b7.config(bg="pink")
        b8.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b1["text"] == b4["text"] == b7["text"] == "X":
        b1.config(bg="pink")
        b4.config(bg="pink")
        b7.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b2["text"] == b5["text"] == b8["text"] == "X":
        b2.config(bg="pink")
        b5.config(bg="pink")
        b8.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b3["text"] == b6["text"] == b9["text"] == "X":
        b3.config(bg="pink")
        b6.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
    elif b1["text"] == b5["text"] == b9["text"] == "X":
        b1.config(bg="pink")
        b5.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b3["text"] == b5["text"] == b7["text"] == "X":
        b3.config(bg="pink")
        b5.config(bg="pink")
        b7.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b1["text"] == b2["text"] == b3["text"] == "O":
        b1.config(bg="pink")
        b2.config(bg="pink")
        b3.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b4["text"] == b5["text"] == b6["text"] == "O":
        b4.config(bg="pink")
        b5.config(bg="pink")
        b6.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b7["text"] == b8["text"] == b9["text"] == "O":
        b7.config(bg="pink")
        b8.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b1["text"] == b4["text"] == b7["text"] == "O":
        b1.config(bg="pink")
        b4.config(bg="pink")
        b7.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b2["text"] == b5["text"] == b8["text"] == "O":
        b2.config(bg="pink")
        b5.config(bg="pink")
        b8.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b3["text"] == b6["text"] == b9["text"] == "O":
        b3.config(bg="pink")
        b6.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
    elif b1["text"] == b5["text"] == b9["text"] == "O":
        b1.config(bg="pink")
        b5.config(bg="pink")
        b9.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()
    elif b3["text"] == b5["text"] == b7["text"] == "O":
        b3.config(bg="pink")
        b5.config(bg="pink")
        b7.config(bg="pink")
        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation on your win")
        disable()


b1 = Button(top, height=7, width=15, text=" ", command=lambda: click(b1))
b2 = Button(top, height=7, width=15, text=" ", command=lambda: click(b2))
b3 = Button(top, height=7, width=15, text=" ", command=lambda: click(b3))
b4 = Button(top, height=7, width=15, text=" ", command=lambda: click(b4))
b5 = Button(top, height=7, width=15, text=" ", command=lambda: click(b5))
b6 = Button(top, height=7, width=15, text=" ", command=lambda: click(b6))
b7 = Button(top, height=7, width=15, text=" ", command=lambda: click(b7))
b8 = Button(top, height=7, width=15, text=" ", command=lambda: click(b8))
b9 = Button(top, height=7, width=15, text=" ", command=lambda: click(b9))
b1.grid(column=0, row=1)
b2.grid(column=1, row=1)
b3.grid(column=2, row=1)
b4.grid(column=0, row=2)
b5.grid(column=1, row=2)
b6.grid(column=2, row=2)
b7.grid(column=0, row=3)
b8.grid(column=1, row=3)
b9.grid(column=2, row=3)

top.mainloop()
