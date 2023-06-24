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
    'money':0,
    'health pad':0,
    'treasure':{
        'code':0,
        'point':0
    }
}

def readTown(filename):
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
        'money':0,
        'health pad':0,
        'treasure':{
            'code':0,
            'point':0
        }
    }
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
        if list[i][:10] == '# Treasure':
            town['treasure']['code'] = int(list[i+1].split(',')[0].strip())
            town['treasure']['point'] = int(list[i+1].split(',')[1].strip())
        if list[i][:7] == '# Money':
            town['money'] = int(list[i+1].strip())
        if list[i][:12] == '# Healingpad':
            town['health'] = int(list[i+1].strip())
    return town


def goTown(roomNum):
    if roomNum == 1:
        townInfo = readTown("Room1.txt")
    if roomNum == 2:
        townInfo = readTown("Room2.txt")
    if roomNum == 3:
        townInfo = readTown("Room3.txt")
    if roomNum == 4:
        townInfo = readTown("Room4.txt")
    print(townInfo)


goTown(1)
goTown(2)