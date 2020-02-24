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
        'Gin','Gin'),
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
        

#Create an ingredient
def createIngredient():

#Add ingredient to library
def addIngredient():

#Commit library to storage
def storeLibrary():

#Restore library from storage
def restoreLibrary():
    
#Delete ingredient from library
def deleteIngredient():
