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

def shop1():
    print('-----------------')
    
def town1(player):
    print('You walk into Vallengards safe walls..')
    while True:
        choice = input('What would you like to do(use \"help\" if needed)?: ').lower()#Perhaps move before while loop
        if choice == 'help':
            print('To look around use(examine),To walk to the quests board use(quests),To check your inventory use(inventory),')
            print('to check your stats use(stats) or to enter the main shop use(shop)')
            print('-----------------')
        elif choice == 'examine':##Make this dependent on if a certain variable is true or not
            print('-----------------')
            print('placeholder')
        elif choice == 'quests':
            print('-----------------')
            print('placeholder')
        elif choice == 'inventory':
            print('-----------------')
            print('placeholder')
        elif choice == 'stats':
            print('-----------------')
            print('Name:',char['name'],'Health:',char['stats']['hp'],'/',char['stats']['maxhp'],'Strength:',char['stats']['stre'])
        elif choice == 'shop':
            print('-----------------')
            print('You walk into the shop, the Shop owner calls out to you')
            print('Hey {}, glad to see you here! Come take a look around!'.format(player['name']))
        else:
            print('Error, please Re-Enter your command, if needed you can use \"Help\"!')
            print('-----------------')
            
town1(char)
