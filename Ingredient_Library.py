#Import/Modify/Store info for all ingredients

IngredientLibrary = []

class FamilyTypes():
    family = ['Alcohol','Mixer']
    def getFamilyTypes():
        return self.family

class BaseTypes():
    base = [
        'Benedictine',
        'Brandy',
        'Cachaca',
        'Campari',
        'Cointreau',
        'Drambuie',
        'Gin',
        'Jagermeister',
        'Liqeueur',
        'Rum',
        'Schnapps',
        'Tequila',
        'Vermouth',
        'Vodka',
        'Whiskey',
        'Wine'
    ]
    def getBaseTypes():
        return self.base

class Ingredient:
    name = None
    base = None
    family = None
    startVol = None
    endVol = None
    active = None
    def __init__(self, name, base, family, startVol, endVol, active):
        self.name = name
        self.base = base
        self.family = family
        self.startVol = startVol
        self.endVol = endVol
        self.active = active

    #String representation for storage
    def __str__(self):
        return self.name+','+self.base+','+self.family+','+self.startVol+','+self.endVol+','+self.active

#Create an ingredient
def createIngredient(name,base,family,startVol, endVol, active):
    ingredient = Ingredient(name, base, family, startVol, startVol, active)
    addIngredient(ingredient)

#Add ingredient to IngredientLibrary
def addIngredient(new_ingredient):
    IngredientLibrary.append(new_ingredient)

#Commit IngredientLibrary to storage
def storeIngredientLibrary():
    file = open("IngredientRepo.txt","w")
    for ingredient in IngredientLibrary:
        file.write(ingredient.__str__)
    file.close()

#Restore IngredientLibrary from storage
def restoreIngredientLibrary():
    file.open("IngredientRepo.txt","w")
    for line in file:
        elements = line.split(',')
        createIngredient(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5])
    
#Delete ingredient from IngredientLibrary
def deleteIngredient(name):
    marked = None
    for element in IngredientLibrary:
        if element.name == name:
            marked = element
    IngredientLibrary.remove(element)
