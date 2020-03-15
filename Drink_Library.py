import json

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
        self.ingredients = ingredients

    def getName(self):
        return self.name

    def setName(self,new_name):
        self.name = new_name

    def getIce(self):
        return self.ice

    def setIce(self,new_ice):
        self.ice = new_ice

    def getGlass(self):
        return self.glass

    def setGlass(self,new_glass):
        self.glass = new_glass

    def getGarnish(self):
        return self.garnish

    def setGarnish(self,new_garnish):
        self.garnish = new_garnish

    def getExtras(self):
        return self.extras

    def setExtras(self,new_extras):
        self.extras = new_extras
    
    def getImage(self):
        return self.image

    def setImage(self,new_image):
        self.image = new_image

def createDrink(name, ice, glass, garnish, extras, ingredients, image):
    drink = Drink(name, ice, glass, garnish, extras, ingredients, image)
    addDrink(drink)

def addDrink(new_drink):
    DrinkLibrary.append(new_drink)

def storeDrinkLibrary():
    file = open("DrinkRepo.txt","w")
    for drink in DrinkLibrary:
        file.write(json.dumps(drink.__dict__)+'\n')
    file.close()

def restoreDrinkLibrary():
    file = open("DrinkRepo.txt","r")
    for line in file:
        drink = json.loads(line[:len(line)-1])
        createDrink(drink['name'],drink['ice'],drink['glass'],drink['garnish'],drink['extras'],drink['ingredients'],drink['image'])

#Delete ingredient from IngredientLibrary
def deleteDrink(name):
    marked = None
    for element in DrinkLibrary:
        if(element.getName() == name):
            marked = element
    DrinkLibrary.remove(marked)
        
def listDrinks():
    return DrinkLibrary

def getIceTypes():
    return ICE

def getGlassTypes():
    return GLASSES