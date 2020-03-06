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
        return self.name+','+self.ice+','+self.glass+','+self.garnish+','+self.extras+','+self.ingredients+','+self.image
    
    def getIngredients(self):
        dict = {}
        elements = self.ingredients.split('#')
        for each in elements:
            dict[each[:each.index('@')]] = int(each[each.index('@')+1:])
        return dict

    def setIngredients(self,ingredients):
        string = ''
        for key, value in ingredients.items():
            string+=str(key)+'@'+str(value)+'#'
        self.ingredients = string[:-1]
        print('LIST = '+self.ingredients)

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
        file.write(str(drink)+'\n')
    file.close()

def restoreDrinkLibrary():
    file = open("DrinkRepo.txt","r")
    for line in file:
        elements = line.split(',')
        createDrink(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6].rstrip())

#Delete ingredient from IngredientLibrary
def deleteDrink(name):
    marked = None
    for element in DrinkLibrary:
        if(element.getName() == name):
            marked = element
    DrinkLibrary.remove(marked)
        
def listDrinks():
    for drink in DrinkLibrary:
        print(drink)
    return DrinkLibrary

def getIceTypes():
    return ICE

def getGlassTypes():
    return GLASSES