
#Set a variable for attack, times it by your attack stat then randint it for its total attack

char = {'name':'Hero',
        'lvl': 1,
        'xp': 0,
        'lvlNext': 25,
        'potions':{'health': 2,
                   'strength': 3},
        'stats':{'stre': 1,
                 'dex': 1,
                 'int': 1,
                 'maxhp': 30,
                 'hp': 10,
                 'atk':[5,12]}}

imp = {'name': 'Imp',
       'lvl': 1,
       'xp': 0,
       'lvlNext': 25,
       'reward': 25,
       'stats':{'stre': 1,
                 'dex': 1,
                 'int': 1,
                 'hp': 30,
                 'atk':[5,12]}}


def level(char,stats):
    nStre, nDex, nInt = 0, 0, 0
    while char['xp'] >= char['lvlNext']:
        char['lvl'] += 1
        char['xp'] = char['xp'] - char['lvlNext']
        char['lvlNext'] = round(char['lvlNext'] * 1.5)
        nStre += 1
        nDex += 1
        nInt += 1

    print('level:', char['lvl']) #level
    # print('STR +{} DEX +{} INT +{}'.format(nStr, nDex, nInt)) #old stats +new stats
    # print()
    #The assignment as I gave it last lesson:
    print('STR {} +{} DEX {} +{} INT {} +{}'.format(char['stats']['stre'], nStre,
                                                    char['stats']['dex'], nDex,
                                                    char['stats']['int'], nInt))
    char['stats']['stre'] += nStre
    char['stats']['dex'] += nDex
    char['stats']['int'] += nInt

from random import randint

def takeDmg(attacker, defender):
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    if defender['stats']['hp'] <= 0:
        print('{} has been slain'.format(defender['name']))
        char['xp'] += imp['reward'] #Find a way to make this interchangable
        level(char,['stats'])
        input('Press any key to quit.')
    else:
        print('{} takes {} damage!'.format(defender['name'], dmg))

def commands(player, enemy):
    while True:
        if enemy['stats']['hp'] <= 0:
            break
        print('------------------')
        cmd = input('Do you want to swing? yes/no: ').lower()
        if 'yes' in cmd:
            takeDmg(player, enemy)
        elif 'no' in cmd:
            while True:
                print('Do you want to use a potion? or Flee?: potion/flee/back')
                dec = input('').lower()
                ##print('{} takes the opportunity to attack!'.format(enemy['name']))
                if dec == 'potion':
                    print('You have',char['potions']['health'], 'health potions and',char['potions']['strength'],'strength potions')
                    pot = input('Which would you like to use? health/strength: ').lower()
                    if pot == 'health':
                        if char['potions']['health'] > 0:
                            print('You drink a health potion and feel your wounds begin to close')
                            char['potions']['health'] = char['potions']['health'] - 1
                            hpAdd = char['stats']['int']
                            maxHp = char['stats']['maxhp']
                            hpTotal = hpAdd + 10
                            hp = char['stats']['hp']
                            if maxHp - hp > hpAdd + 10:
                                char['stats']['hp'] = hp + hpTotal
                            elif maxHp - hp < hpAdd + 10:
                                char['stats']['hp'] = maxHp
                                print('You feel yourself return to your peak state!(No more HP can be gained)')
                            #char['stats']['hp'] = hpAdd + 10
                            print(char['stats']['hp'])
                        elif char['potions']['health'] <= 0:
                            print('You don\'t have any health potions!')
                            break
                        else:
                            print('Error with potion amount values line 80')
                    elif pot == 'strength':
                        print('placeholder')
                    break
                elif dec == 'flee':
                    print('placeholder')
                    break
                elif dec == 'back':
                    break
                else:
                    pass
        else:
            pass

char['xp'] += 25
level(char, char['stats'])

char['xp'] += 500
level(char, ['stats'])

commands(char,imp)
