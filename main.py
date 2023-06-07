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
        'armours': [],
        'health pad': 0
    }
}

player['money'] = random.randrange(50, 310, 1)

window = tkinter.Tk()

def open_info():
    if len(input.get()) > 0:
        for object in window.winfo_children():
            object.pack_forget()
        window.geometry("1000x600")
        player['name'] = input.get()
        frame2 = tkinter.Frame(window)
        username = tkinter.Label(frame2, text = "Username: " + player['name'], font="Calibri, 12")
        money = tkinter.Label(frame2, text="Money: "+str(player['money']), font="Calibri, 12")
        health = tkinter.Label(frame2, text="Health: "+str(player['health']), font="Calibri, 12")
        frame3 = tkinter.Frame(window)
        btn_town1 = tkinter.Button(frame3, text="Town1", font="Calibri, 12")
        btn_town2 = tkinter.Button(frame3, text="Town2", font="Calibri, 12")
        btn_town3 = tkinter.Button(frame3, text="Town3", font="Calibri, 12")
        btn_town4 = tkinter.Button(frame3, text="Town4", font="Calibri, 12")
        btn_shop = tkinter.Button(frame3, text="Shop", font="Calibri, 12", command=showShop)
        btn_back = tkinter.Button(frame3, text="Log out", font="Calibri, 12", command=openLogin)
        frame3.pack(side=tkinter.BOTTOM, pady=20)
        frame2.pack(side=tkinter.TOP, pady=20)
        username.grid(row=0, column=0, padx=100)
        money.grid(row = 0, column=1, padx=100)
        health.grid(row = 0, column=2, padx=100)
        btn_town1.grid(row = 0, column=0, padx=50)
        btn_town2.grid(row = 0, column=1, padx=50)
        btn_town3.grid(row = 0, column=2, padx=50)
        btn_town4.grid(row = 0, column=3, padx=50)
        btn_shop.grid(row = 0, column=4, padx=50)
        btn_back.grid(row = 0, column=5, padx=50)
    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "Please enter a username!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()

def buyInventory(element, type):
    if type == 'weapon':
        list = player['inventory']
        list['weapons'].append(element)
    if type == 'armour':
        list = player['inventory']
        list['armours'].append(element)
    if type == 'key':
        list = player['inventory']
        list['keys'].append(element)

def buyHealth(info, label):
    if info['health pad'] > 0:
        info['health pad'] -= 1
        player['inventory']['health pad'] += 1
        label.config(text="Quantity: " + str(info['health pad']))
    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("350x100")
        label_warning = tkinter.Label(warning, text = "Health pad not available in the shop.", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()

def showShop():
    readShop = open("Shop.txt", "r")

    list = readShop.read().split("\n")

    shopInfo = {
        'weapons':[],
        'armours':[],
        'health pad': 0,
        'keys':[]
    }

    for element in list:
        if element == '':
            list.remove(element)

    for element in list:
        if element.split(':')[0][:6] == 'weapon':
            weaponName = element.split(':')[1].split(',')[0].strip()
            weaponDamage = element.split(':')[1].split(',')[1].strip()
            weaponPrice = element.split(':')[1].split(',')[2].strip()
            weapon = {'Name':weaponName, 'Damage':weaponDamage, 'Price':weaponPrice}
            shopInfo['weapons'].append(weapon)
        elif element.split(':')[0][:3] == 'key':
            keyCode = element.split(':')[1].split(',')[0].strip()
            keyPrice = element.split(':')[1].split(',')[1].strip()
            key = {'Code':keyCode, 'Price':keyPrice}
            shopInfo['keys'].append(key)
        elif element.split(':')[0][:6] == 'armour':
            armourDurability = element.split(':')[1].split(',')[0].strip()
            armourPrice = element.split(':')[1].split(',')[1].strip()
            armour = {'Durability':armourDurability, 'Price':armourPrice}
            shopInfo['armours'].append(armour)
        elif (element != list[0]) & (element[0] != '#'):
            healthPadQuantity = int(element[0].strip())
            shopInfo['health pad'] = healthPadQuantity

    for object in window.winfo_children():
            object.pack_forget()
    window.geometry("1500x900")
    shopLabel = tkinter.Label(window, text="Welcome to the Shop", font="Calibri, 12")
    headFrame = tkinter.Frame(window)
    utilityFrame = tkinter.Frame(window)
    buttonFrame = tkinter.Frame(window)

    weaponFrame = tkinter.Frame(utilityFrame)
    armourFrame = tkinter.Frame(utilityFrame)
    keyFrame = tkinter.Frame(utilityFrame)
    healthFrame = tkinter.Frame(utilityFrame)
    
    weaponLabel = tkinter.Label(headFrame, text="Weapons", font="Calibri, 12")
    armourLabel = tkinter.Label(headFrame, text="Armours", font="Calibri, 12")
    keyLabel = tkinter.Label(headFrame, text="Keys", font="Calibri, 12")
    healthLabel = tkinter.Label(headFrame, text="Health Pad", font="Calibri, 12")

    btn_inventory = tkinter.Button(buttonFrame, text="Inventory", font="Calibri, 12")
    btn_back = tkinter.Button(buttonFrame, text="Go back", font="Calibri, 12", command=open_info)
    
    shopLabel.pack(side = tkinter.TOP, pady=20)
    headFrame.pack(pady=20)
    utilityFrame.pack(pady=20)
    buttonFrame.pack(side = tkinter.BOTTOM, pady=20)
    weaponFrame.grid(row =0, column=0, padx=50)
    armourFrame.grid(row =0, column=1, padx = 50)
    keyFrame.grid(row =0, column=2, padx = 50)
    healthFrame.grid(row =0, column=3, padx = 50)
    weaponLabel.grid(row = 0, column = 0, padx = 150)
    armourLabel.grid(row = 0, column = 1, padx = 150)
    keyLabel.grid(row = 0, column = 2, padx = 150)
    healthLabel.grid(row = 0, column = 3, padx = 150)

    for element in shopInfo['weapons']:
         s = "Name: "+ element['Name']+", "+"Damage: "+element['Damage']+", Price: "+element['Price']
         weaponInfo = tkinter.Label(weaponFrame, text=s, font="Calibri, 12")
         buyButton = tkinter.Button(weaponFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='weapon': buyInventory(e, t))
         weaponInfo.grid(row = shopInfo['weapons'].index(element) +1, column =0 ,pady=15, padx=10)
         buyButton.grid(row = shopInfo['weapons'].index(element)+1, column =1 ,pady=15, padx=10)
    for element in shopInfo['armours']:
        s = "Durability: "+element['Durability']+", Price: "+element['Price']
        ArmourInfo = tkinter.Label(armourFrame, text=s, font="Calibri, 12")
        buyButton = tkinter.Button(armourFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='armour': buyInventory(e, t))
        ArmourInfo.grid(row = shopInfo['armours'].index(element) +1, column =0 ,pady=15, padx=10)
        buyButton.grid(row = shopInfo['armours'].index(element)+1, column =1 ,pady=15, padx=10)
    for element in shopInfo['keys']:
        s = "Code: "+element['Code']+", Price: "+element['Price']
        keyInfo = tkinter.Label(keyFrame, text=s, font="Calibri, 12")
        buyButton = tkinter.Button(keyFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='key': buyInventory(e, t))
        keyInfo.grid(row = shopInfo['keys'].index(element) +1, column =0 ,pady=15, padx=10)
        buyButton.grid(row = shopInfo['keys'].index(element)+1, column =1 ,pady=15, padx=10)
    
    s = "Quantity: "+str(shopInfo['health pad'])
    healthInfo = tkinter.Label(healthFrame, text = s, font="Calibri, 12")
    buyButton = tkinter.Button(healthFrame, text="Buy", font="Calibri, 12", command = lambda: buyHealth(shopInfo, healthInfo))
    healthInfo.grid(row = 1, column =0 ,pady=15, padx=10)
    buyButton.grid(row = 1, column =1 ,pady=15, padx=10)


    btn_inventory.grid(row = 0, column=0, padx= 100)
    btn_back.grid(row = 0, column=1, padx=100)
    
         

window.geometry("300x200")

frame1 = tkinter.Frame(window)

label = tkinter.Label(window, text = "Please enter your username:", font="Calibri, 12")

input = tkinter.Entry(frame1)

button = tkinter.Button(frame1, text="Log in", bg="green", fg="white", font="Calibri, 12", command=open_info)

def openLogin():
    for object in window.winfo_children():
            object.pack_forget()

    label.pack(pady=20)

    frame1.pack()

    input.grid(row = 1, column=0, padx=5, pady=5)

    button.grid(row=1, column=1, padx=5, pady=5)



openLogin()

window.title("Best Game Ever")

window.mainloop()