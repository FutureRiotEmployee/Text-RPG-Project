#Where stat points are allocated
skill = {'total': 0,
         }






char = {'name':'Hero',
        'lvl': 1,
        'xp': 0,
        'lvlNext': 25,
        'stats':{'str': 1,
                 'dex': 1,
                 'int': 1,
                 'hp': 30,
                 'atk':[5,12]}}

imp = {'name': 'Imp',
       'lvl': 1,
       'xp': 0,
       'lvlNext': 25,
       'reward': 25,
       'stats':{'str': 1,
                 'dex': 1,
                 'int': 1,
                 'hp': 30,
                 'atk':[5,12]}}


def level(char,stats):
    nStr, nDex, nInt = 0, 0, 0
    while char['xp'] >= char['lvlNext']:
        char['lvl'] += 1
        char['xp'] = char['xp'] - char['lvlNext']
        char['lvlNext'] = round(char['lvlNext'] * 1.5)
        nStr += 1
        nDex += 1
        nInt += 3

    print('level:', char['lvl']) #level
    # print('STR +{} DEX +{} INT +{}'.format(nStr, nDex, nInt)) #old stats +new stats
    # print()
    #The assignment as I gave it last lesson:
    print('STR {} +{} DEX {} +{} INT {} +{}'.format(char['stats']['str'], nStr,
                                                    char['stats']['dex'], nDex,
                                                    char['stats']['int'], nInt))
    char['stats']['str'] += nStr
    char['stats']['dex'] += nDex
    char['stats']['int'] += nInt

from random import randint

def takeDmg(attacker, defender):
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    if defender['stats']['hp'] <= 0:
        print('{} has been slain'.format(defender['name']))
        char['xp'] += imp['reward']
        level(char,char['stats'])
        input('Press any key to continue.')
    else:
        print('{} takes {} damage!'.format(defender['name'], dmg))

def commands(player, enemy):
    while True:
        if imp['stats']['hp'] <= 0:
              break
        print('------------------')
        cmd = input('Do you want to attack? yes/no: ').lower()
        if 'yes' in cmd:
            takeDmg(player, enemy)
        elif 'no' in cmd:
            print('{} takes the opportunity to attack!'.format(enemy['name']))
        else:
            pass

#char['xp'] += 25
#level(char, char['stats'])

commands(char,imp)

#char['xp'] += 100
#level(char, char['stats'])
