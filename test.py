readShop = open("Shop.txt", "r")

list = readShop.read().split("\n")



shopInfo = {
    'weapons':[],
    'armours':[],
    'health pad': {},
    'key':{}
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
        shopInfo['key'] = {'Code':keyCode, 'Price':keyPrice}
    elif element.split(':')[0][:6] == 'armour':
        armourDurability = element.split(':')[1].split(',')[0].strip()
        armourPrice = element.split(':')[1].split(',')[1].strip()
        armour = {'Durability':armourDurability, 'Price':armourPrice}
        shopInfo['armours'].append(armour)
    elif (element != list[0]) & (element[0] != '#'):
        healthPadQuantity = int(element[0])
        shopInfo['health pad'] = {'Quantity':healthPadQuantity}