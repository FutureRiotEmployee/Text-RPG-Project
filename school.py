from random import randint
from time import sleep
#Set a variable for attack, times it by your attack stat then randint it for its total attack

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


imp = {'name': 'Imp',
       'lvl': 1,
       'xp': 0,
       'lvlNext': 25,
       'reward': 9999,
       'stats':{'strE': 1,
                'dexE': 1,
                'intE': 1,
                'hpE': 15,
                'maxhpE':15,
                'atkE':[5,8]}}


def level(char,stats):
    nStre, nDex, nInt, nMaxStre = 0, 0, 0, 0
    while char['xp'] >= char['lvlNext']:
        char['lvl'] += 1
        char['xp'] = char['xp'] - char['lvlNext']
        char['lvlNext'] = round(char['lvlNext'] * 1.5)
        nMaxStre += 1
        nStre += 1
        nDex += 1
        nInt += 1

    print('level:', char['lvl'])
    print('STR {} +{} DEX {} +{} INT {} +{}'.format(char['stats']['stre'], nStre,
                                                    char['stats']['dex'], nDex,
                                                    char['stats']['int'], nInt))
    char['stats']['maxStre'] += nMaxStre
    char['stats']['stre'] += nStre
    char['stats']['dex'] += nDex
    char['stats']['int'] += nInt


def takeDmg(attacker, defender):
    if char['turn'] == True:
        dmg = randint(1,3) * char['stats']['stre']
        defender['stats']['hpE'] = defender['stats']['hpE'] - dmg
        if defender['stats']['hpE'] <= 0:
            print('{} has been slain'.format(defender['name']))
            char['stats']['stre'] = char['stats']['maxStre']
            char['xp'] += defender['reward'] 
            level(char,['stats'])
            input('Press any key to end battle.')#Perhaps remove??
        else:
            print('{} takes {} damage!'.format(defender['name'], dmg))
            print(defender['stats']['hpE'],"/",defender['stats']['maxhpE'])
            char['turn'] = False
    elif char['turn'] == False:
        dmgE = randint(1,2) * attacker['stats']['stre']
        attacker['stats']['hp'] = attacker['stats']['hp'] - dmgE
        if attacker['stats']['hp'] <= 0:
            print('Your vision starts to fade to darkness as the {} overpowers you...'.format(defender['name']))
        else:
            print('{} takes {} damage!'.format(attacker['name'], dmgE))
            print(attacker['stats']['hp'],"/",attacker['stats']['maxhp'])
            char['turn'] = True

def commands(player, enemy):
    while True:
        breakk = False
        breake = False
        if enemy['stats']['hpE'] <= 0:
            break
        print('------------------')
        if char['turn'] == False:
            print('It\'s {}\'s turn!'.format(enemy['name']))
            sleep(1)
            takeDmg(player, enemy)
            #Perhaps add dexterity use here?
        cmd = input('Do you want to attack(yes) or do something else(no)?: ').lower()
        if 'yes' in cmd:
            takeDmg(player, enemy)
        elif 'no' in cmd:
            while True:
                print('Do you want to use a potion? or Flee?: potion/flee/back')
                dec = input('').lower()
                ##print('{} takes the opportunity to attack!'.format(enemy['name']))
                if dec == 'potion':
                    while True:
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
                            
                            else:
                                print('Error with potion amount values line 80')
                        elif pot == 'strength':
                            if char['potions']['strength'] > 0:
                                print('You feel your muscles tighten past their usual limit')
                                char['potions']['strength'] = char['potions']['strength'] - 1
                                char['stats']['stre'] = char['stats']['stre'] + 2
                                break
                                print('Your strength is now',char['stats']['stre'] - char['stats']['maxStre'], 'past it\'s normal limit!')
                            elif char['potions']['health'] <= 0:
                                print('You don\'t have any health potions!')
                                break
                        break
                elif dec == 'flee':
                    if randint(1,100) < 36:
                        print('You successfully break away from battle!')
                        breakk = True
                        break
                    elif randint(1,100) > 36:
                        print('Your attack attempt fails and gives the {} time to attack!'.format(enemy['name']))
                        char['turn'] = False
                        breake = True
                        break
                elif dec == 'back':
                    break
                elif breakk == True:
                    break
                elif breake == True:
                    break
                else:
                    pass
        if breakk == True:
            break
        if breake == True:
            continue
        
        else:
            pass

#char['xp'] += 25
#level(char, char['stats'])

#char['xp'] += 500
#level(char, ['stats'])

commands(char,imp)
