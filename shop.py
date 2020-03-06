import random
entershop = "y"
item = ""



def itemshop():
    global gold
    gold = 100
    print("you walk into a dark and musty room.\nInfront of you stands an old man behind a bar filled with mysterious goods.")
    print("the man says hello!my name is tim the shopkeeper would you like to buy from my shop? \n(y or n)")
 
def goshop():
    
    entershop = input()
    if entershop == "y":
          print("great here is a selection of my items!")
          print("red cram 50G \nblue carm 50G\ncram sword 100 G ")
          print("wich item would you like?(1-9)")
          print("you have"+ str(gold) +"G")
    elif entershop == "n":
          print("farewell then")
def itemstuff():
    global gold
    gold = 100

    global itemprice
    itemprice = 0
    item = input()
    if item == "1":
        itemprice = 50
    
        if gold >= itemprice:
            gold = gold - itemprice
            print("you bought red cram! you now have: "+str(gold)+"G")
    if item == "2":
        itemprice = 50
    
        if gold >= itemprice:
            gold = gold - itemprice
            print("you bought blue cram! you now have: "+str(gold)+"G")
    if item == "3":
        itemprice = 100
    
        if gold >= itemprice:
            gold = gold - itemprice
            print("you bought a cram sword! you now have: "+str(gold)+"G")
def stopshop():
    print("would you like to buy another item?(y or n twice)")
    entershop = input()
    return entershop
   
itemshop()
while entershop == "y":
    goshop()
    itemstuff()
    entershop = stopshop()

