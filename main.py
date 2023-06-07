import tkinter
import random

player = {
    'name': '',
    'money': 0,
    'health': 100,
    'points': 0,
    'inventory': {
        'weapons': [],
        'keys': [],
        'armour': [],
    }
}

player['money'] = random.randrange(50, 310, 1)

window = tkinter.Tk()

window.geometry("300x200")

frame1 = tkinter.Frame(window)

label = tkinter.Label(window, text = "Please enter your username:", font="Calibri, 12")

input = tkinter.Entry(frame1)

def open_info():
    if len(input.get()) > 0:
        for object in window.winfo_children():
            object.pack_forget()
        window.geometry("1000x600")
        player['name'] = input.get()
        frame3 = tkinter.Frame(window)
        username = tkinter.Label(frame3, text = "Username: " + player['name'], font="Calibri, 12")
        money = tkinter.Label(frame3, text="Money: "+str(player['money']), font="Calibri, 12")
        health = tkinter.Label(frame3, text="Health: "+str(player['health']), font="Calibri, 12")
        frame2 = tkinter.Frame(window)
        btn_town1 = tkinter.Button(frame2, text="Town1", font="Calibri, 12")
        btn_town2 = tkinter.Button(frame2, text="Town2", font="Calibri, 12")
        btn_town3 = tkinter.Button(frame2, text="Town3", font="Calibri, 12")
        btn_town4 = tkinter.Button(frame2, text="Town4", font="Calibri, 12")
        btn_shop = tkinter.Button(frame2, text="Shop", font="Calibri, 12")
        frame3.pack(side=tkinter.TOP, pady=20)
        frame2.pack(side=tkinter.BOTTOM, pady=20)
        username.grid(row=0, column=0, padx=100)
        money.grid(row = 0, column=1, padx=100)
        health.grid(row = 0, column=2, padx=100)
        btn_town1.grid(row = 0, column=0, padx=50)
        btn_town2.grid(row = 0, column=1, padx=50)
        btn_town3.grid(row = 0, column=2, padx=50)
        btn_town4.grid(row = 0, column=3, padx=50)
        btn_shop.grid(row = 0, column=4, padx=50)

    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "Please enter a username!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()


button = tkinter.Button(frame1, text="Log in", bg="green", fg="white", font="Calibri, 12", command=open_info)

label.pack(pady=20)

frame1.pack()

input.grid(row = 1, column=0, padx=5, pady=5)

button.grid(row=1, column=1, padx=5, pady=5)

window.title("Best Game Ever")

window.mainloop()