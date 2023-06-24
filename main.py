import tkinter
import random


#for fight inventory
fightmode = {
    'armour':{
        'ID':-1,
        'durability':1,
        'price':0
    },
    'weapon':{
        'ID':-1,
        'name':None,
        'damage':0,
        'price':0
    }
}


#player initialization
player = {
    'name': '',
    'money': 0,
    'health': 100,
    'points': 0,
    'inventory': {
        'weapons': [],
        'keys': [],
        'armours': [],
        'health pad': {
            'point': 0,
            'price': 0,
            'quantity':0
        },
        'treasure':[]
    }
}


#money initialization
player['money'] = random.randrange(50, 310, 1)
shopInfo = {
    'weapons':[],
    'armours':[],
    'health pad': {
        'point': 0,
        'price': 0,
        'quantity':0
    },
    'keys':[]
}

#returning all content from chosen file
def readFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


#updating file
def updateFile(lines, filename):
    with open(filename, 'w') as f:
        f.writelines(lines)

#reading the shop txt file and adding all content to dictionary
def readShop(): 
    readShop = open("Shop.txt", "r")

    list = readShop.read().split("\n")
    for element in list:
        if element == '':
            list.remove(element)

    for element in list:
        if element.split(':')[0][:6] == 'weapon':
            counter1 = 0
            weaponName = element.split(':')[1].split(',')[0].strip()
            weaponDamage = int(element.split(':')[1].split(',')[1].strip())
            weaponPrice = int(element.split(':')[1].split(',')[2].strip())
            weapon = {'ID': counter1, 'name':weaponName, 'damage':weaponDamage, 'price':weaponPrice}
            shopInfo['weapons'].append(weapon)
            counter1+=1
        elif element.split(':')[0][:3] == 'key':
            keyCode = int(element.split(':')[1].split(',')[0].strip())
            keyPrice = int(element.split(':')[1].split(',')[1].strip())
            key = {'code':keyCode, 'price':keyPrice}
            shopInfo['keys'].append(key)
        elif element.split(':')[0][:6] == 'armour':
            counter2 = 0
            armourDurability = int(element.split(':')[1].split(',')[0].strip())
            armourPrice = int(element.split(':')[1].split(',')[1].strip())
            armour = {'ID':counter2, 'durability':armourDurability, 'price':armourPrice}
            shopInfo['armours'].append(armour)
            counter2+=1
        elif (element != list[0]) & (element[0] != '#'):
            healthPadQuantity = int(element[0].strip())
            shopInfo['health pad']['quantity'] = healthPadQuantity
        elif element.split(':')[0] == '# HealingPad description':
            healthPadPrice = int(element.split(':')[1].split(',')[1].strip()[5:])
            healthPadPoints = int(element.split(':')[1].split(',')[0].strip()[6:])
            shopInfo['health pad']['price'] = healthPadPrice
            shopInfo['health pad']['point'] = healthPadPoints

    readShop.close()
    return shopInfo

#importing shop
shopInfo = readShop()

#for town information collection
townInfo = {
    'label':[],
    'enemy':{
        'name':'',
        'damage':0,
        'health':0
    },
    'point':0,
    'weapon':{
        'name':'',
        'damage':0,
        'price':0
    },
    'armour':{
        'durability':1,
        'price':0,
    },
    'key':{
        'code':-1,
        'price':0
    },
    'money':0,
    'health pad':0,
    'treasure':{
        'code':0,
        'point':0
    }
}


#reading the given town file
def readTown(roomNum):
    town = {
        'label':[],
        'enemy':{
            'name':'',
            'damage':0,
            'health':0
        },
        'point':0,
        'weapon':{
            'name':'',
            'damage':0,
            'price':0
        },
        'armour':{
            'durability':1,
            'price':0,
        },
        'key':{
            'code':-1,
            'price':0
        },
        'money':0,
        'health pad':0,
        'treasure':{
            'code':None,
            'point':0
        }
    }
    filename = f"Room{roomNum}.txt"
    readTown = open(filename, "r")
    list = readTown.read().split("\n")
    for element in list:
        if element == '':
            list.remove(element)
    for i in range(0, len(list)):
        if list[i][:7] == 'Welcome':
            town['label'].append(list[i])
            town['label'].append(list[i+1])
        if list[i][:7] == '# Enemy':
            town['enemy']['name'] = list[i+1].split(',')[0].strip()
            town['enemy']['damage'] = int(list[i+1].split(',')[1].strip())
            town['enemy']['health'] = int(list[i+1].split(',')[2].strip())
        if list[i][:7] == '# Point':
            town['point'] = int(list[i+1].strip())
        if list[i][:8] == '# Weapon':
            town['weapon']['name'] = list[i+1].split(',')[0].strip()
            town['weapon']['damage'] = int(list[i+1].split(',')[1].strip())
            town['weapon']['price'] = int(list[i+1].split(',')[2].strip())
        if list[i][:8] == '# Armour':
            town['armour']['durability'] = list[i+1].split(',')[0].strip()
            town['armour']['price'] = int(list[i+1].split(',')[1].strip())
        if list[i][:10] == '# Treasure':
            town['treasure']['code'] = int(list[i+1].split(',')[0].strip())
            town['treasure']['point'] = int(list[i+1].split(',')[1].strip())
        if list[i][:7] == '# Key':
            town['key']['code'] = int(list[i+1].split(',')[0].strip())
            town['key']['price'] = int(list[i+1].split(',')[1].strip())
        if list[i][:7] == '# Money':
            town['money'] = int(list[i+1].strip())
        if list[i][:12] == '# Healingpad':
            town['health'] = int(list[i+1].strip())
    return town

#starting the GUI window
window = tkinter.Tk()


#main page after log in
def open_info():
    if len(input.get()) > 0:
        for object in window.winfo_children():
            object.pack_forget()
        if player['points'] >= 0 & player['points'] <= 9:
            window.geometry("1000x600")
            player['name'] = input.get()
            frame2 = tkinter.Frame(window)
            username = tkinter.Label(frame2, text = "Username: " + player['name'], font="Calibri, 12")
            money = tkinter.Label(frame2, text="Money: "+str(player['money']), font="Calibri, 12")
            health = tkinter.Label(frame2, text="Health: "+str(round(player['health'], 1)), font="Calibri, 12")
            point = tkinter.Label(frame2, text = "Point: "+str(player['points']), font='Calibri, 12')
            frame3 = tkinter.Frame(window)
            btn_town1 = tkinter.Button(frame3, text="Town1", font="Calibri, 12", command=lambda: goTown(1))
            btn_town2 = tkinter.Button(frame3, text="Town2", font="Calibri, 12", command=lambda: goTown(2))
            btn_town3 = tkinter.Button(frame3, text="Town3", font="Calibri, 12", command=lambda: goTown(3))
            btn_town4 = tkinter.Button(frame3, text="Town4", font="Calibri, 12", command=lambda: goTown(4))
            btn_inventory = tkinter.Button(frame3, text="Inventory", font="Calibri, 12", command=showInventory)
            btn_shop = tkinter.Button(frame3, text="Shop", font="Calibri, 12", command=showShop)
            frame3.pack(side=tkinter.BOTTOM, pady=20)
            frame2.pack(side=tkinter.TOP, pady=20)
            username.grid(row=0, column=0, padx=80)
            money.grid(row = 0, column=1, padx=80)
            health.grid(row = 0, column=2, padx=80)
            point.grid(row= 0, column = 3, padx = 80)
            btn_town1.grid(row = 0, column=0, padx=40)
            btn_town2.grid(row = 0, column=1, padx=40)
            btn_town3.grid(row = 0, column=2, padx=40)
            btn_town4.grid(row = 0, column=3, padx=40)
            btn_shop.grid(row = 0, column=4, padx=40)
            btn_inventory.grid(row = 0, column=5, padx=40)
        if player['points'] >= 10:
            win = tkinter.Tk()
            win.geometry("500x100")
            win.title('Won')
            winLabel = tkinter.Label(win, text='Your point reached 10. You won the game. Try again with another player')
            winLabel.pack()
        if player['points'] < 0:
            lose = tkinter.Tk()
            lose.geometry("500x100")
            lose.title('Lost')
            loseLabel = tkinter.Label(lose, text='Your point is below 0. You lost the game. Try again with another Player')
            loseLabel.pack()
    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "Please enter a username!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()

#adding items into invewntory which are bought in shop
def buyInventory(element, type):
    if player['money']>= element['price']:
        if type == 'weapon':
            list = player['inventory']
            list['weapons'].append(element)
            shopInfo['weapons'].remove(element)
            loadShop(shopInfo)
        if type == 'armour':
            list = player['inventory']
            list['armours'].append(element)
            shopInfo['armours'].remove(element)
            loadShop(shopInfo)
        if type == 'key':
            list = player['inventory']
            list['keys'].append(element)
            shopInfo['keys'].remove(element)
            loadShop(shopInfo)

        player['money'] -= element['price']
    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "You don't have enough money!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()


#buying health pads differs in some aspects from other utilities so I created new function for it
def buyHealth(info, label):
    if player['money']>= info['health pad']['price']:
        if info['health pad']['quantity'] > 0:
            info['health pad']['quantity'] -= 1
            player['inventory']['health pad']['quantity'] += 1
            player['inventory']['health pad']['price'] = info['health pad']['price']
            player['inventory']['health pad']['point'] = info['health pad']['price']
            label.config(text="Quantity: "+str(info['health pad']['quantity'])+"\nPrice: "+str(info['health pad']['price'])+"\nPoints: "+str(info['health pad']['point']))
            player['money'] -= info['health pad']['price']
        else:
            warning = tkinter.Tk()
            warning.title("Warning")
            warning.geometry("350x100")
            label_warning = tkinter.Label(warning, text = "Health pad not available in the shop.", font="Calibri, 12", pady=30)
            label_warning.pack()
            warning.mainloop()
    else:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "You don't have enough money!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()

#showing the shop information on GUI
def loadShop(shopInfo):
    for object in window.winfo_children():
            object.pack_forget()
    window.geometry("1500x900")
    shopLabel = tkinter.Label(window, text="Welcome to the Shop", font="Calibri, 12")
    utilityFrame = tkinter.Frame(window)
    buttonFrame = tkinter.Frame(window)

    weaponFrame = tkinter.Frame(utilityFrame)
    armourFrame = tkinter.Frame(utilityFrame)
    keyFrame = tkinter.Frame(utilityFrame)
    healthFrame = tkinter.Frame(utilityFrame)
    
    weaponLabel = tkinter.Label(weaponFrame, text="Weapons", font="Calibri, 12")
    armourLabel = tkinter.Label(armourFrame, text="Armours", font="Calibri, 12")
    keyLabel = tkinter.Label(keyFrame, text="Keys", font="Calibri, 12")
    healthLabel = tkinter.Label(healthFrame, text="Health Pad", font="Calibri, 12")

    btn_inventory = tkinter.Button(buttonFrame, text="Inventory", font="Calibri, 12", command=showInventory)
    btn_back = tkinter.Button(buttonFrame, text="Go back", font="Calibri, 12", command=open_info)
    
    shopLabel.pack(side = tkinter.TOP, pady=20)
    utilityFrame.pack(pady=20)
    buttonFrame.pack(side = tkinter.BOTTOM, pady=20)
    weaponFrame.grid(row =0, column=0, padx=20)
    armourFrame.grid(row =0, column=1, padx = 20)
    keyFrame.grid(row =0, column=2, padx = 20)
    healthFrame.grid(row =0, column=3, padx = 20)
    weaponLabel.grid(row = 0, column = 0)
    armourLabel.grid(row = 0, column = 0)
    keyLabel.grid(row = 0, column = 0)
    healthLabel.grid(row = 0, column = 0)

    for element in shopInfo['weapons']:
         s = "Name: "+ element['name']+", "+"Damage: "+str(element['damage'])+", Price: "+str(element['price'])
         weaponInfo = tkinter.Label(weaponFrame, text=s, font="Calibri, 12")
         buyButton = tkinter.Button(weaponFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='weapon': buyInventory(e, t))
         weaponInfo.grid(row = shopInfo['weapons'].index(element) +1, column =0 ,pady=15, padx=10)
         buyButton.grid(row = shopInfo['weapons'].index(element) +1, column =1 ,pady=15, padx=10)
    for element in shopInfo['armours']:
        s = "Durability: "+str(element['durability'])+", Price: "+str(element['price'])
        ArmourInfo = tkinter.Label(armourFrame, text=s, font="Calibri, 12")
        buyButton = tkinter.Button(armourFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='armour': buyInventory(e, t))
        ArmourInfo.grid(row = shopInfo['armours'].index(element) +1, column =0 ,pady=15, padx=10)
        buyButton.grid(row = shopInfo['armours'].index(element) +1, column =1 ,pady=15, padx=10)
    for element in shopInfo['keys']:
        s = "Code: "+str(element['code'])+", Price: "+str(element['price'])
        keyInfo = tkinter.Label(keyFrame, text=s, font="Calibri, 12")
        buyButton = tkinter.Button(keyFrame, text="Buy", font="Calibri, 12", command=lambda e=element, t='key': buyInventory(e, t))
        keyInfo.grid(row = shopInfo['keys'].index(element) +1, column =0 ,pady=15, padx=10)
        buyButton.grid(row = shopInfo['keys'].index(element) +1, column =1 ,pady=15, padx=10)
    
    s = "Quantity: "+str(shopInfo['health pad']['quantity'])+"\nPrice: "+str(shopInfo['health pad']['price'])+"\nPoints: "+str(shopInfo['health pad']['point'])
    healthInfo = tkinter.Label(healthFrame, text = s, font="Calibri, 12")
    buyButton = tkinter.Button(healthFrame, text="Buy", font="Calibri, 12", command = lambda: buyHealth(shopInfo, healthInfo))
    healthInfo.grid(row = 1, column =0 ,pady=15, padx=10)
    buyButton.grid(row = 1, column =1 ,pady=15, padx=10)


    btn_inventory.grid(row = 0, column=0, padx= 100)
    btn_back.grid(row = 0, column=1, padx=100)


#Showing the information of inventory on GUI
def showInventory():
    for object in window.winfo_children():
            object.pack_forget()
    window.geometry("1500x900")
    shopLabel = tkinter.Label(window, text="Welcome to the Shop", font="Calibri, 12")
    utilityFrame = tkinter.Frame(window)
    buttonFrame = tkinter.Frame(window)

    weaponFrame = tkinter.Frame(utilityFrame)
    armourFrame = tkinter.Frame(utilityFrame)
    keyFrame = tkinter.Frame(utilityFrame)
    healthFrame = tkinter.Frame(utilityFrame)
    treasureFrame = tkinter.Frame(utilityFrame)
    
    weaponLabel = tkinter.Label(weaponFrame, text="Weapons", font="Calibri, 12")
    armourLabel = tkinter.Label(armourFrame, text="Armours", font="Calibri, 12")
    keyLabel = tkinter.Label(keyFrame, text="Keys", font="Calibri, 12")
    treasureLabel = tkinter.Label(treasureFrame, text="Treasure Boxes", font='Calibri, 12')
    healthLabel = tkinter.Label(healthFrame, text="Health Pad", font="Calibri, 12")

    btn_back_shop = tkinter.Button(buttonFrame, text="Go back to shop", font="Calibri, 12", command=showShop)
    btn_back_home = tkinter.Button(buttonFrame, text='Go back to home', font='Calibri 12', command=open_info)
    
    shopLabel.pack(side = tkinter.TOP, pady=20)
    utilityFrame.pack(pady=20)
    buttonFrame.pack(side = tkinter.BOTTOM, pady=20)
    weaponFrame.grid(row =0, column=0, padx=40)
    armourFrame.grid(row =0, column=1, padx = 40)
    keyFrame.grid(row =0, column=2, padx = 40)
    treasureFrame.grid(row = 0, column=3, padx= 40)
    healthFrame.grid(row =0, column=4, padx = 40)
    weaponLabel.grid(row = 0, column = 0)
    armourLabel.grid(row = 0, column = 0)
    keyLabel.grid(row = 0, column = 0)
    treasureLabel.grid(row = 0, column = 0)
    healthLabel.grid(row = 0, column = 0)

    for element in player['inventory']['weapons']:
         s = "Name: "+ element['name']+", "+"Damage: "+str(element['damage'])+", Price: "+str(element['price'])
         weaponInfo = tkinter.Label(weaponFrame, text=s, font="Calibri, 12")
         weaponInfo.grid(row = player['inventory']['weapons'].index(element) +1, column =0 ,pady=15, padx=10)
         if len(player['inventory']['weapons']) > 0:
            use_btn = tkinter.Button(weaponFrame, text='Use', font="Calibri, 12", command=lambda e=element, t='weapon': useUtil(t, e))
            sell_btn = tkinter.Button(weaponFrame, text='Sell', font="Calibri, 12", command=lambda e=element, t='weapon': sellUtil(t, e))
            use_btn.grid(row = player['inventory']['weapons'].index(element) +1, column =1 ,pady=15, padx=10)
            sell_btn.grid(row = player['inventory']['weapons'].index(element) +1, column =2 ,pady=15, padx=10)
    for element in player['inventory']['armours']:
        if element['price']!= 0 & element['durability'] != 1:
            s = "Durability: "+str(element['durability'])+", Price: "+str(element['price'])
            ArmourInfo = tkinter.Label(armourFrame, text=s, font="Calibri, 12")
            ArmourInfo.grid(row = player['inventory']['armours'].index(element) +1, column =0 ,pady=15, padx=10)
            if len(player['inventory']['armours']) > 0:
                use_btn = tkinter.Button(armourFrame, text='Use', font="Calibri, 12", command=lambda e=element, t='armour': useUtil(t, e))
                sell_btn = tkinter.Button(armourFrame, text='Sell', font="Calibri, 12", command=lambda e=element, t='armour': sellUtil(t, e))
                use_btn.grid(row = player['inventory']['armours'].index(element) +1, column =1 ,pady=15, padx=10)
                sell_btn.grid(row = player['inventory']['armours'].index(element) +1, column =2 ,pady=15, padx=10)
    for element in player['inventory']['keys']:
        if element['code'] != -1:
            s = "Code: "+str(element['code'])+", Price: "+str(element['price'])
            keyInfo = tkinter.Label(keyFrame, text=s, font="Calibri, 12")
            keyInfo.grid(row = player['inventory']['keys'].index(element) +1, column =0 ,pady=15, padx=10)
    for element in player['inventory']['treasure']:
        s = 'Code: '+str(element['code']) + ', Points: ' + str(element['point'])
        treasureInfo = tkinter.Label(treasureFrame, text = s, font='Calibri, 12')
        treasureInfo.grid(row = player['inventory']['treasure'].index(element) +1, column = 0, pady=15, padx=10)
        if len(player['inventory']['treasure']) > 0:
            open_btn = tkinter.Button(treasureFrame, text='Open', font='Calibri, 12', command=lambda e = element : openTreasure(e))
            open_btn.grid(row = player['inventory']['treasure'].index(element) +1, column = 1, pady=15, padx=10)
    
    s = "Quantity: "+str(player['inventory']['health pad']['quantity'])
    healthInfo = tkinter.Label(healthFrame, text = s, font="Calibri, 12")
    healthInfo.grid(row = 1, column =0 ,pady=15, padx=10)
    if player['inventory']['health pad']['quantity'] > 0:
        use_btn = tkinter.Button(healthFrame, text='Use', font="Calibri, 12", command=lambda e=player['inventory']['health pad'], t='health pad': useUtil(t, e))
        sell_btn = tkinter.Button(healthFrame, text='Sell', font="Calibri, 12", command=lambda e=player['inventory']['health pad'], t='health pad': sellUtil(t, e))
        use_btn.grid(row = 1, column =1 ,pady=15, padx=10)
        sell_btn.grid(row = 1, column =2 ,pady=15, padx=10)

    btn_back_shop.grid(row = 0, column=1, padx=100)
    btn_back_home.grid(row = 0, column = 2, padx = 100)

#checking if user has the key for treasure box
def openTreasure(element):
    check = True
    success = tkinter.Tk()
    success.geometry('350x100')
    successLabel = tkinter.Label(success, text='')
    for key in player['inventory']['keys']:
        if key['code'] == element['code']:
            player['points'] += element['point']
            successLabel = tkinter.Label(success, text='You opened the box. Point is added to your account.')
            check = False
            player['inventory']['keys'].remove(key)
            player['inventory']['treasure'].remove(element)
            showInventory()
            break
    if check:
        successLabel = tkinter.Label(success, text='You don\'t have the key to open box. Try to find key in either shop or towns.')
    successLabel.pack(pady=20)
    success.mainloop()


def showShop():
    loadShop(shopInfo)

#using utility for fight
def useUtil(utilType, element):
    if utilType == 'weapon':
        fightmode['weapon']['ID'] = element['ID']
        fightmode['weapon']['name'] = element['name']
        fightmode['weapon']['damage'] = element['damage']
        fightmode['weapon']['price'] = element['price']
    if utilType == 'armour':
        fightmode['armour']['ID'] = element['ID']
        fightmode['armour']['durability'] = element['durability']
        fightmode['armour']['price'] = element['price']
    if utilType == 'health pad':
        player['inventory']['health pad']['quantity'] -=1
        if (player['health'] + element['point']) < 100:
            player['health'] += element['point']
        else:
            player['health'] = 100
    showInventory()

#selling utility which is already in inventory
def sellUtil(utilType, element):
    if utilType == 'weapon':
        player['inventory']['weapons'].remove(element)
        player['money']+= element['price']
    if utilType == 'armour':
        player['inventory']['armours'].remove(element)
        player['money']+= element['price']
    if utilType == 'health pad':
        player['inventory']['health pad']['quantity'] -=1
        player['money'] += player['inventory']['health pad']['price']
    showInventory()

#showing the information of town on GUI
def loadTown(info, filename):
    for object in window.winfo_children():
            object.pack_forget()
    window.geometry("1500x900")
    buttonFrame = tkinter.Frame(window)
    s = info['label'][0]
    townLabel1 = tkinter.Label(window, text=s, font="Calibri, 12")
    s= info['label'][1]
    townLabel2 = tkinter.Label(window, text=s, font="Calibri, 12")
    infoFrame = tkinter.Frame(window)
    townLabel1.pack(pady=20)
    townLabel2.pack(pady=5)
    buttonFrame.pack(side=tkinter.BOTTOM)
    if info['enemy']['health'] != 0:
        s = "Enemy:\n"+"Name: "+info['enemy']['name']+", Damage: "+str(info['enemy']['damage'])+", Health: "+str(info['enemy']['health'])
        enemyInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        s = "Points:\n"+str(info['point'])
        pointInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        s = "Weapon:\n"+"Name: "+info['weapon']['name']+", Damage: "+str(info['weapon']['damage'])+", Price: "+str(info['weapon']['price'])
        weaponInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        s = "Money:\n"+str(info['money'])
        moneyInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        s = "Health Pad:\n"+str(info['health pad'])
        healthInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        s = "Treasure:\n"+"Code: "+str(info['treasure']['code']) +", Point: "+str(info['treasure']['point'])
        if info['treasure']['code'] == None:
            s = "Treasure:\nNone"
        treasureInfo = tkinter.Label(infoFrame, text=s,font="Calibri, 12")
        inventory_btn = tkinter.Button(buttonFrame, text = 'Inventory', font= 'Calibri, 12', command=showInventory)
        fight_btn = tkinter.Button(buttonFrame, text ='Fight', font = 'Calibri, 12', command=lambda: fight_enemy(info, filename))
        enemyInfo.pack(pady=15)
        pointInfo.pack(pady=15)
        weaponInfo.pack(pady=15)
        moneyInfo.pack(pady=15)
        healthInfo.pack(pady=15)
        treasureInfo.pack(pady=15)
        
        infoFrame.pack(pady=20)
        inventory_btn.grid(row = 0, column = 0, pady=20, padx = 15)
        fight_btn.grid(row = 0, column = 1, pady = 20, padx = 15)
        btn_back = tkinter.Button(buttonFrame, text="Go back", font="Calibri, 12", command=open_info)
        btn_back.grid(row = 0, column=2, pady=20, padx = 15)
    else:
        fightLabel = tkinter.Label(window, text='You have already take everything in this town. Please go other towns.', font='Calibri, 12')
        fightLabel.pack()
        btn_back = tkinter.Button(buttonFrame, text="Go back", font="Calibri, 12", command=open_info)
        btn_back.grid(row = 0, column=0, pady=20, padx = 15)

#updating the health of enemy after fight
def updateHealth(lines, health):
    for line in lines:
        if line == '# Enemy description: name, damage, health\n':
            lines[lines.index(line)+1] = str(lines[lines.index(line)+1].split(',')[0].strip()) + ','+ str(lines[lines.index(line)+1].split(',')[1].strip()) + ',' + str(health)+'\n\n'
    return lines

#fighting with enemy of the chosen town
def fight_enemy(info, filename):
    lines = None
    if player['health'] == 0:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "You don't have enough health to fight!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()
    if player['points'] < 0:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("250x100")
        label_warning = tkinter.Label(warning, text = "You lost the game!", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()
    if fightmode['weapon']['name'] == None:
        warning = tkinter.Tk()
        warning.title("Warning")
        warning.geometry("500x100")
        label_warning = tkinter.Label(warning, text = "You don't have any weapon to fight!\n Go back and equip weapon from inventory or buy from shop.", font="Calibri, 12", pady=30)
        label_warning.pack()
        warning.mainloop()
    else:
        success = True
        fight_scene = tkinter.Tk()
        fight_scene.title('Fighting scene')
        fight_scene.geometry('350x200')
        successLabel = tkinter.Label(fight_scene, font='Calibri, 12')
        while True:
            info['enemy']['health'] = info['enemy']['health'] - fightmode['weapon']['damage']
            if info['enemy']['health'] <= 0:
                successLabel = tkinter.Label(fight_scene, text='You won the fight! All city inventory is yours.', font='Calibri, 12')
                break
            player['health'] = player['health'] - (info['enemy']['damage']/fightmode['armour']['durability'])
            if player['health'] <= 0:
                player['health'] = 0
                success = False
                successLabel = tkinter.Label(fight_scene, text='You lost the fight!', font='Calibri, 12')
                player['points'] -= 2
                lines = readFile(filename)
                lines = updateHealth(lines, info['enemy']['health'])
                updateFile(lines, filename)
                loadTown(info, filename)
                break
        if success:
            player['money']+= info['money']
            player['points'] += info['point']
            counter1 = len(player['inventory']['armours'])
            counter2 = len(player['inventory']['armours'])
            weapon = {'ID': counter1, 'name': info['weapon']['name'], 'damage': info['weapon']['damage'], 'price': info['weapon']['price']}
            player['inventory']['weapons'].append(weapon)
            armour = {'ID': counter2, 'durability': info['armour']['durability'], 'price': info['armour']['price']}
            player['inventory']['armours'].append(armour)
            player['inventory']['health pad']['quantity'] += info['health pad']
            player['inventory']['keys'].append(info['key'])
            player['inventory']['treasure'].append(info['treasure'])
            lines = readFile(filename)
            updateHealth(lines, 0)
            updateFile([lines[0], lines[1]], filename)
        player['inventory']['weapons'].remove(fightmode['weapon'])
        if fightmode['armour'] in player['inventory']['armours']:
            player['inventory']['armours'].remove(fightmode['armour'])
        fightmode['armour'] = {
        'ID':-1,
        'durability':1,
        'price':0
        }
        fightmode['weapon'] = {
        'ID':-1,
        'name':None,
        'damage':0,
        'price':0
        }
        successLabel.grid(row =0, column=0, padx=50, pady=50)
        fight_scene.mainloop()

    
#function helps to choose which town should be shown    
def goTown(roomNum):
    if roomNum == 1:
        townInfo = readTown(1)
    if roomNum == 2:
        townInfo = readTown(2)
    if roomNum == 3:
        townInfo = readTown(3)
    if roomNum == 4:
        townInfo = readTown(4)
    filename = f"Room{roomNum}.txt"
    loadTown(townInfo, filename)

window.geometry("300x200")

frame1 = tkinter.Frame(window)

label = tkinter.Label(window, text = "Please enter your username:", font="Calibri, 12")

input = tkinter.Entry(frame1)

button = tkinter.Button(frame1, text="Log in", bg="green", fg="white", font="Calibri, 12", command=open_info)

#opening login page
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