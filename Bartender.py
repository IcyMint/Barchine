import Ingredient_Library
import Drink_Library
import time, datetime

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

def showDrinkMenu():
    return Drink_Library.DrinkLibrary

def getShelf():
    shelf = []
    for ingredient in Ingredient_Library.IngredientLibrary:
        if ingredient.isActive():
            shelf.append(ingredient)
    return shelf

def editShelf():
    shelf = getShelf()
    