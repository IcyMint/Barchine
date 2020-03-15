import json

#Import/Modify/Store info for all ingredients

IngredientLibrary = []

FAMILIES = ['Alcohol','Mixer']

BASES = []


class Ingredient:
    name = None
    base = None
    family = None
    startVol = None
    endVol = None
    active = None
    position = None
    def __init__(self, name, base, family, startVol, endVol, active, position):
        self.name = name
        self.base = base
        self.family = family
        self.startVol = startVol
        self.endVol = endVol
        self.active = active
        self.position = position

    #String representation for storage
    def __str__(self):
        return self.name+','+self.base+','+self.family+','+str(self.startVol)+','+str(self.endVol)+','+str(self.active)+','+str(self.position)

    def isActive(self):
        return self.active

    def getName(self):
        return self.name

    def setName(self,new_name):
        self.name = new_name
    
    def getBase(self):
        return self.base

    def setBase(self,new_base):
        self.base = new_base

    def getFamily(self):
        return self.family

    def setFamily(self,new_family):
        self.family = new_family

    def getStartVol(self):
        return self.startVol

    def setStartVol(self,new_startVol):
        self.startVol = new_startVol

    def getEndVol(self):
        return self.endVol

    def setEndVol(self, new_endVol):
        self.endVol = new_endVol

    def setActive(self, new_active):
        self.active = new_active
    
    def getPosition(self):
        return self.position

    def setPosition(self, new_position):
        self.position = new_position

        
#Create an ingredient
def createIngredient(name,base,family,startVol, endVol, active, position):
    test = str(active)
    if(test == 'True'):
        active = True
    else:
        active = False
    ingredient = Ingredient(name, base, family, int(startVol), int(endVol), bool(active), int(position))
    addIngredient(ingredient)

#Add ingredient to IngredientLibrary
def addIngredient(new_ingredient):
    IngredientLibrary.append(new_ingredient)

#Save IngredientLibrary to storage
def storeIngredientLibrary():
    file = open("IngredientRepo.txt","w")
    for ingredient in IngredientLibrary:
        file.write(json.dumps(ingredient.__dict__)+'\n')
    file.close()

#Restore IngredientLibrary from storage
def restoreIngredientLibrary():
    file = open("IngredientRepo.txt","r")
    for line in file:
        ingredient = json.loads(line[:len(line)-1])
        createIngredient(ingredient['name'],ingredient['base'],ingredient['family'],ingredient['startVol'],ingredient['endVol'],ingredient['active'],ingredient['position'])

#Build bases library from file
def restoreBases():
    #TODO: Remove this after ingestion
    BASES.clear()
    file = open("BasesRepo.txt","r")
    for line in file:
        BASES.append(line.strip('\n'))
    
#Delete ingredient from IngredientLibrary
def deleteIngredient(name):
    marked = None
    for element in IngredientLibrary:
        if(element.getName() == name):
            marked = element
    IngredientLibrary.remove(marked)

def listIngredients():
    return IngredientLibrary

def getFamilyTypes():
    return FAMILIES

def getBaseTypes():
    return BASES