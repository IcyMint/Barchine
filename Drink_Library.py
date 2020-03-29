import json
from Logging import log

#Import/Modify/Store info for all drinks
DrinkLibrary = []

ICE = [
    'None',
    'Cubes',
    'Crushed',
    'Any'
]

GLASSES = [
        'Any',
        'Cocktail Glass',
        'Flute Glass',
        'Highball Glass',
        'Hurricane Glass',
        'Irish Coffee Glass',
        'Lowball Glass',
        'Margarita Glass',
        'Martini Glass',
        'Red Wine Glass',
        'Rock',
        'Snifter Glass',
        'Glencairn Whiskey Glass',
        'White Wine Glass'
    ]

class Drink():
    name = None
    ice = None
    glass = None
    garnish = None
    extras = None
    ingredients = None
    image = None
    def __init__(self, name, ice, glass, garnish, extras, ingredients, image):
        self.name = name
        self.ice = ice
        self.glass = glass
        self.garnish = garnish
        self.extras = extras
        self.ingredients = ingredients
        self.image = image

    def __str__(self):
        return self.name+','+self.ice+','+self.glass+','+self.garnish+','+self.extras+','+str(self.ingredients)+','+self.image
    
    def getIngredients(self):
        return self.ingredients

    def setIngredients(self,ingredients):
        log('Drinks','[EDIT]'+'ingredients='+str(ingredients)+'|'+str(self))
        self.ingredients = ingredients

    def getName(self):
        return self.name

    def setName(self,new_name):
        log('Drinks','[EDIT]'+'name='+new_name+'|'+str(self))
        self.name = new_name

    def getIce(self):
        return self.ice

    def setIce(self,new_ice):
        log('Drinks','[EDIT]'+'ice='+new_ice+'|'+str(self))
        self.ice = new_ice

    def getGlass(self):
        return self.glass

    def setGlass(self,new_glass):
        log('Drinks','[EDIT]'+'glass='+new_glass+'|'+str(self))
        self.glass = new_glass

    def getGarnish(self):
        return self.garnish

    def setGarnish(self,new_garnish):
        log('Drinks','[EDIT]'+'garnish='+new_garnish+'|'+str(self))
        self.garnish = new_garnish

    def getExtras(self):
        return self.extras

    def setExtras(self,new_extras):
        log('Drinks','[EDIT]'+'extras='+new_extras+'|'+str(self))
        self.extras = new_extras
    
    def getImage(self):
        return self.image

    def setImage(self,new_image):
        log('Drinks','[EDIT]'+'image='+new_image+'|'+str(self))
        self.image = new_image

def createDrink(name, ice, glass, garnish, extras, ingredients, image,restore):
    drink = Drink(name, ice, glass, garnish, extras, ingredients, image)
    addDrink(drink)
    if(not restore):
        log('Drinks','[CREATE]'+str(drink))

def addDrink(new_drink):
    DrinkLibrary.append(new_drink)
    log('Drinks','[CREATE]'+str(new_drink))

def storeDrinkLibrary():
    file = open("DrinkRepo.txt","w")
    for drink in DrinkLibrary:
        file.write(json.dumps(drink.__dict__)+'\n')
    file.close()
    log('Info','Saved Drink Library')

def restoreDrinkLibrary():
    file = open("DrinkRepo.txt","r")
    for line in file:
        drink = json.loads(line[:len(line)-1])
        createDrink(drink['name'],drink['ice'],drink['glass'],drink['garnish'],drink['extras'],drink['ingredients'],drink['image'],True)

#Delete ingredient from IngredientLibrary
def deleteDrink(name):
    marked = None
    for element in DrinkLibrary:
        if(element.getName() == name):
            marked = element
    log('Drinks','[DELETE]'+str(marked))
    DrinkLibrary.remove(marked)
        
def listDrinks():
    return DrinkLibrary

def getIceTypes():
    return ICE

def getGlassTypes():
    return GLASSES