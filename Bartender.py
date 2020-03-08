import Ingredient_Library
import Drink_Library
import time, datetime

MAX_POSITIONS = 8

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

def createOrder(name):
    order = None
    for drink in Drink_Library.DrinkLibrary:
        if drink == name:
            order = Order(drink, StatusTypes.getStatusTypes()[0])
            #Send order onwards to logging system and arduino processing

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
    shelf = [None]*MAX_POSITIONS
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
    return MAX_POSITIONS