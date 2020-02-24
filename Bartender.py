import * from Ingredient_Library
import * from Drink_Library
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
    for drink in DrinkLibrary:
        if drink == name:
            order = Order(drink, StatusTypes.getStatusTypes()[0])
            #Send order onwards to logging system and arduino processing
