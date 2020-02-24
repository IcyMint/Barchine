#Import/Modify/Store info for all drinks
DrinkLibrary = []


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
        return self.name+','+self.ice+','+self.glass+','+self.garnish+','+self.extras+','+self.ingredients+','+self.image

class IceTypes():
    ice = [
        'Cubes',
        'Crushed',
        'Any',
        'None'
    ]
    def getIceTypes():
        return self.ice

class GlassTypes():
    glasses = [
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
    def getGlassTypes():
        return self.glasses

def createDrink(name, ice, glass, garnish, extras, ingredients, image):
    drink = Drink(name, ice, glass, garnish, extras, ingredients, image)
    addDrink(drink)

def addDrink(new_drink):
    DrinkLibrary.append(new_drink)

def storeDrinkLibrary():
    file = open("DrinkRepo.txt","w")
    for drink in DrinkLibrary:
        file.write(drink.__str__)
    file.close()

def restoreDrinkLibrary():
    file.open("DrinkRepo.txt","w")
    for line in file:
        elements = line.split(',')
        createDrink(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6])
        
