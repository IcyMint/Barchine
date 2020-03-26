import Ingredient_Library
import Drink_Library
import time, datetime

#First 9 positions are alcohol, next 5 are mixers
ALCOHOL_POSITION_COUNT = 9
MIXER_POSITION_COUNT = 5

class Order():
    drink_ref = None
    status = None
    time = None
    def __init__(self,drink_ref,status):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.drink_ref = drink_ref
        self.time = st
        self.status = status
    
    def __str__():
        return self.drink_ref+','+self.time+','+self.status

class StatusTypes():
    status = [
        'Active',
        'Paused',
        'Delivered',
        'Cancelled'
    ]
    def getStatusTypes():
        return self.status

def createOrder(name,force):

    shelfPositions = []
    for item in getShelf():
        if(item is not None):
            shelfPositions.append(item.getBase())
        else:
            shelfPositions.append(None)

    recipe = {}
    order = None
    for drink in Drink_Library.DrinkLibrary:
        if drink.getName() == name:
            order = drink
            break

    if(force):
        shelf = {}
        #Get a dict of shelf names
        for element in getShelf():
            if(element is not None):
                shelf[element.getBase()] = ''

            #Get recipe together for arduino
        for key, value in order.getIngredients().items():
            if(key in shelf):
                recipe[shelfPositions.index(str(key))] = int(value)
        #Pass on to arduino
        print('RECIPE: '+str(recipe))
    else:
        #Get recipe together for arduino
        for key, value in order.getIngredients().items():
            try:
                recipe[shelfPositions.index(str(key))] = int(value)
            except ValueError:
                print('Didnt find: '+str(key))
        #Pass on to arduino
        print(recipe)

def showDrinkMenu(pretty):
    drinkmenu = []
    for drink in Drink_Library.DrinkLibrary:
        total = len(drink.getIngredients())
        count = 0
        for name, amount in drink.getIngredients().items():
            for element in getShelf():
                if(element != None):
                    if(element.getBase() == name):
                        count+=1
        if(total==count):
            if(pretty):
                drinkmenu.append(drink.getName())
                #Organise list alphabetically
                drinkmenu.sort(key=str.lower) 
            else:
                drinkmenu.append(drink)
    return drinkmenu

def getShelf():
    shelf = [None]*getMaxPos()
    for ingredient in Ingredient_Library.IngredientLibrary:
        if ingredient.isActive():
            shelf[ingredient.getPosition()] = ingredient
    return shelf

def removeShelfItem(name):
    for ingredient in Ingredient_Library.IngredientLibrary:
        if(name == ingredient.getName()):
            ingredient.setActive(False)
            ingredient.setPosition(-1)

def addShelfItem(name, position):
    for ingredient in Ingredient_Library.IngredientLibrary:
        if(name == ingredient.getName()):
            ingredient.setActive(True)
            ingredient.setPosition(position)
    
def getMaxPos():
    return ALCOHOL_POSITION_COUNT + MIXER_POSITION_COUNT

def getAlcCount():
    return ALCOHOL_POSITION_COUNT

def getMixCount():
    return MIXER_POSITION_COUNT