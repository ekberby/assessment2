import tkinter

window = tkinter.Tk()

window.geometry("300x200")

frame1 = tkinter.Frame(window)

label = tkinter.Label(window, text = "Please enter your username:", font="Arial, 12")

input = tkinter.Entry(frame1)

button = tkinter.Button(frame1, text="Log in", bg="green", fg="white")

label.pack(pady=20)

frame1.pack()

input.grid(row = 1, column=0, padx=5, pady=5)

button.grid(row=1, column=1, padx=5, pady=5)

window.title("Best Game Ever")

window.mainloop()