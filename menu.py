import random
import time

item1 = {'name':'Old Short Sword',
        'strength value': 2,
        'dexterity value': 0,
        'intel value': 0,
        'health value':0}



item2 = {'name':'old sheild',
        'strength value': 1,
        'dexterity value': -2,
        'intel value': 0,
        'health value':7}



item3 = {'name':'old long sword',
        'strength value': 5,
        'dexterity value': 0,
        'intel value': 0,
        'health value':0}


item4 = {'name':'old staff',
        'strength value': 1,
        'dexterity value': 3,
        'intel value': 5,
        'health value':0}

item5 = {'name':'old amplifying tome',
        'strength value': -2,
        'dexterity value': 3,
        'intel value': 5,
        'health value':0}

item6 = {'name':'Old Dagger',
        'strength value': 1,
        'dexterity value': 4,
        'intel value': 2,
        'health value':-1}

item7 = {'name':'Old Leather Armor',
        'strength value': 1,
        'dexterity value': 2,
        'intel value': 3,
        'health value':10}

item8 = {'name':'Old Leather Guise',
        'strength value': 0,
        'dexterity value': 1,
        'intel value': 2,
        'health value': 7}

item9 = {'name':'Old Mage Robes',
        'strength value': 0,
        'dexterity value': 2,
        'intel value': 10,
        'health value':5}

item10 = {'name':'Old Mage Hood',
        'strength value': -1,
        'dexterity value': 3,
        'intel value': 7,
        'health value':3}

item11 = {'name':'Old Plate Armor',
        'strength value': 2,
        'dexterity value': 3,
        'intel value': 4,
        'health value': 11}

item12 = {'name':'Old Plate Helmet',
        'strength value': 0,
        'dexterity value': 2,
        'intel value': 3,
        'health value': 8}

char = {'name':'Hero',
        'lvl': 1,
        'xp': 0,
        'lvlNext': 25,
        'turn':True,
        'potions':{'health': 2,
                   'strength': 3},
        'stats':{'stre': 1,
                 'maxStre':1,
                 'dex': 1,
                 'int': 1,
                 'maxhp': 20,
                 'hp': 20,}}
openInv = ""
itembought = ""
slot1 =""
slot2 =""
slot3 =""
slot4 =""
slot5 =""
print("would you like to buy "+ item1['name'] +" for 5G \n(1 to buy)")
itembought = input()
print("you bought the "+ item1['name']+".")
print("would you like to open inventory?")
openInv = input()

def menu(player):
    print()
    print("---Charecter Info---")
    print('\nname: {}'.format(char['name']))
    print('lvl: {}'.format(char['lvl']))
    print('xp: {}'.format(char['xp']))
    print('xp to next lvl: {}'.format(char['lvl']))
    time.sleep(1)
    print()
    print("---Equiped Items---")
    print('head item:')
    print('torso item:')
    print('1 handed item:')
    print('2 handed item:')
    print('off-hand item:')
    time.sleep(1)
def inventory(player, item):
    print()
    print("---Inventory---")
    print('slot 1:{}'.format(item['name']))
    print('slot 2:')
    print('slot 3:')
    print('slot 4:')
    print('slot 5:')
if openInv == "yes":
    menu(char)
    inventory(char,item1)
    if itembought == 1:
        inventory(char,item1)
