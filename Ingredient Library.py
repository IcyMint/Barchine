#Import/Modify/Store info for all ingredients

library = []

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
        'Wine',
    ]
    def getBaseTypes():
        return self.base

class Ingredient:
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

#Add ingredient to library
def addIngredient(new_ingredient):
    library.append(new_ingredient)

#Commit library to storage
def storeLibrary():
    file = open("IngredientRepo.txt","w")
    for ingredient in library:
        file.write(ingredient.__str__)
    file.close()

#Restore library from storage
def restoreLibrary():
    file.open("IngredientRepo.txt","w")
    for line in file:
        elements = line.split(',')
        createIngredient(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5])
    
#Delete ingredient from library
def deleteIngredient(name):
    marked = null
    for element in library:
        if element.name == name:
            marked = element
    library.remove(element)
