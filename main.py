import tkinter

window = tkinter.Tk()

window.geometry("500x300")

label = tkinter.Label(window, text = "Please enter your username:", font="Arial, 20")

input = tkinter.Entry(window)

button = tkinter.Button(text="Log in", bg="green", fg="white")

label.pack()

input.pack()

button.pack()

window.title("Best Game Ever")

window.mainloop()