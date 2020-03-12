char = {'name':'Hero',
        'class':'Unassigned',
        'lvl': 1,
        'xp': 0,
        'lvlNext': 25,
        'turn':True,
        'gold':100,
        'potions':{'health': 2,
                   'strength': 3},
        'events':{'casinoTutorial':False,
                  'fillerTutorial':False},
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
            print('to check your stats use(stats), to enter the casino use(casino) or to enter the main shop use(shop)')
            print('-----------------')
        elif choice == 'examine':##Make this dependent on if a certain variable is true or not
            print('-----------------')
            print('placeholder')
        elif choice == 'quests':
            print('-----------------')
            print('You approach the quests board...')
            while True:
                print('placeholder')
        elif choice == 'inventory':
            print('-----------------')
            print('placeholder')
        elif choice == 'stats':
            print('-----------------')
            print('Name:',char['name'])
            print('Class:',char['class'])
            print('Health:',char['stats']['hp'],'/',char['stats']['maxhp'])
            print('Strength:',char['stats']['stre'])
            print('Intelligence:',char['stats']['int'])
            print('Dexterity:',char['stats']['dex'])
        elif choice == 'casino':
            print('You walk into the Casino...')
            while True:
                if char['events']['casinoTutorial'] == False:
                    while char['events']['casinoTutorial'] == False:##This is if never been in casino before
                        yes = input('Hello {}, would you like a tutorial?(yes) or (no): '.format(char['name'])).lower()
                        while char['events']['casinoTutorial'] == False:
                            if yes == 'yes':
                                print('Here at the Casino you must put in a bet prior')
                                print('If you win, your bet will always double')
                                print('But there\'s a catch!')
                                print('The Game Master will randomly decide what game you\'ll play!')
                                yes1 = input('Do you understand?: ')
                                if yes1 == 'yes':
                                    char['events']['casinoTutorial'] = True
                                else:
                                    print('*Ahem* let me explain again...')
                                    print('-----------------')
                                    pass
                            elif yes =='no':
                                print('Okay then suit yourself!')
                                char['events']['casinoTutorial'] = True
                else:
                    print('placeholder')
        elif choice == 'shop':
            print('-----------------')
            print('You walk into the shop, the Shop owner calls out to you')
            print('Hey {}, glad to see you here! Come take a look around!'.format(player['name']))
        else:
            print('Error, please Re-Enter your command, if needed you can use \"Help\"!')
            print('-----------------')
            
town1(char)
