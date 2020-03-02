import random
entershop = " "
gold = 100
item = ""
itemprice = " "


def itemshop():
    print("you walk into a dark and musty room.\nInfront of you stands an old man behind a bar filled with mysterious goods.")
    print("the man says hello!my name is tim the shopkeeper would you like to buy from my shop? \n(y or n)")
    entershop = input()
    if entershop == "y":
          print("great here is a selection of my items!")
          print("...........")
          print("wich item would you like?(1-9)")
          item = input()
          return item
          if item == 1:
              itemprice = 50
              if gold >= itemprice:
                  gold = gold - itemprice
                  print("you bought a sword! your gold is:"+gold+"")
              
              
    elif entershop == "n":
        print("farewell then")

itemshop()
