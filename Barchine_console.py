from Ingredient_Library import restoreIngredientLibrary, storeIngredientLibrary, listIngredients, getFamilyTypes, getBaseTypes, deleteIngredient, createIngredient
from Drink_Library import restoreDrinkLibrary, storeDrinkLibrary, listDrinks, deleteDrink, getIceTypes, getGlassTypes, createDrink
import Bartender
import sys

print('Barchine::Made by Diego Bonilla, 2020')
print('type "help" to list all commands')

user = ''

#Main console loop

while(user!='exit'):

    user = input('----Main Menu----\n')

    #Load libraries
    if(user == 'load'):
        restoreIngredientLibrary()
        restoreDrinkLibrary()
    
    #Save libraries
    if(user == 'save'):
        storeDrinkLibrary()
        storeIngredientLibrary()
    
    #list elements (debugging)
    if(user == 'list'):
        for drink in listDrinks():
            print(drink)
        print('--------------------------')
        for ingredient in listIngredients():
            print(ingredient)

    #Add a new ingredient to the library
    if(user == 'addIngredient'):
        #Get ingredient name from user
        name = input('Enter name of ingredient: ')
        #Retrieve base type from user
        i=0
        for element in getBaseTypes():
            print(str(i)+' - '+element)
            i+=1
        base = input('------------Select base with number---------------\n')
        base = getBaseTypes()[int(base)]
        i=0
        for element in getFamilyTypes():
            print(str(i)+' - '+element)
            i+=1
        family = input('------------Select family with number---------------\n')
        family = getFamilyTypes()[int(family)]
        startVol = input('Enter starting volume: ')
        #Generate drink and add to library
        createIngredient(name,base,family,startVol,startVol,False,0)

    if(user == 'editIngredient'):
        i = 0
        for element in listIngredients():
            print(str(i)+' - '+element.getName())
            i+=1
        target = input('------------Select drink number to edit---------------\n')
        #Get new name
        new_name = input('Enter new name of ingredient ('+listIngredients()[int(target)].getName()+'): ')
        #Retrieve base type from user
        i=0
        for element in getBaseTypes():
            print(str(i)+' - '+element)
            i+=1
        new_base = input('------------Select base with number ('+listIngredients()[int(target)].getBase()+')---------------\n')
        if(len(new_base)<1):
            new_base = listIngredients()[int(target)].getBase()
        else:
            new_base = getBaseTypes()[int(new_base)]
        #Retrieve family type from user
        i=0
        for element in getFamilyTypes():
            print(str(i)+' - '+element)
            i+=1
        new_family = input('------------Select family with number ('+listIngredients()[int(target)].getFamily()+')-------------\n')
        if(len(new_family)<1):
            new_family = listIngredients()[int(target)].getFamily()
        else:
            new_family = getFamilyTypes()[int(new_family)]
        new_startVol = input('Enter starting volume ('+str(listIngredients()[int(target)].getStartVol())+'): ')
        new_EndVol = input('Enter starting volume ('+str(listIngredients()[int(target)].getEndVol())+'): ')
        #Perform edits
        if(len(new_name)>0):
            listIngredients()[int(target)].setName(new_name)
        if(len(new_base)>0):
            listIngredients()[int(target)].setBase(new_base)
        if(len(new_family)>0):
            listIngredients()[int(target)].setFamily(new_family)
        if(len(new_startVol)>0):
            listIngredients()[int(target)].setStartVol(int(new_startVol))
        if(len(new_EndVol)>0):
            listIngredients()[int(target)].setEndVol(int(new_EndVol))


    if(user == 'showshelf'):
        for element in Bartender.getShelf():
            print(element)

    if(user == 'editshelf'):
        print('1 - remove from shelf')
        print('2 - add to shelf')
        print('3 - change position')
        user = input('\nWhat would you like to do: ')
        #Remove item from shelf
        if(user == '1'):
            i = 1
            for element in Bartender.getShelf():
                if(element!=None):
                    print(str(i)+' - '+element.getName())
                else:
                    print(str(i)+' - '+'EMPTY')
                i+=1
            item = input('------------Select shelf item---------------\n')
            Bartender.removeShelfItem(Bartender.getShelf()[int(item)-1].getName())

        #Add item to shelf
        if(user == '2'):
            if(None not in Bartender.getShelf()):
                print('Shelf currently full')
                continue
            #List innactive ingredients
            i = 0
            for element in listIngredients():
                if(not element.isActive()):
                    print(str(i)+' - '+element.getName())
                i+=1
            item = input('------------Select item to add to shelf---------------\n')
            #List empty shelf positions
            i = 0
            for element in Bartender.getShelf():
                if(element==None):
                    print(str(i)+' - EMPTY')
                i+=1
            position = input('------Enter position------\n')
            Bartender.addShelfItem(listIngredients()[int(item)].getName(),int(position))
            
        #Change item position
        if(user == '3'):
            i = 1
            for element in Bartender.getShelf():
                if(element!=None):
                    print(str(i)+' - '+element.getName())
                else:
                    print(str(i)+' - '+'EMPTY')
                i+=1
            item = input('------------Select shelf item---------------\n')
            item = Bartender.getShelf()[int(item)-1].getName()
            print(item)
            i = 0
            for element in Bartender.getShelf():
                if(element==None):
                    print(str(i)+' - EMPTY')
                i+=1
            position = input('------Enter position------\n')

            Bartender.addShelfItem(item,int(position))

    if(user == 'delIngredient'):
        i = 0
        for ingredient in listIngredients():
            print(str(i)+' - '+ingredient.getName())
            i+=1
        target = input('------Select ingredient to delete------')
        deleteIngredient(listIngredients()[int(target)].getName())

    if(user == 'menu'):
        for drink in Bartender.showDrinkMenu():
            print(drink)

    if(user == 'delDrink'):
        i = 0
        for drink in listDrinks():
            print(str(i)+' - '+drink.getName())
            i+=1
        target = input('-----Enter drink number to delete-----\n')
        deleteDrink(listDrinks()[int(target)].getName())

    if(user == 'addDrink'):
        new_name = input('Enter new name: ')
        #Display options for ice
        i = 0
        for ice in getIceTypes():
            print(str(i)+' - '+ice)
            i+=1
        new_ice = input('-----Enter ice type-----\n')
        new_ice = getIceTypes()[int(new_ice)]
        #Display options for glasses
        i = 0
        for glass in getGlassTypes():
            print(str(i)+' - '+glass)
            i+=1
        new_glass = input('-----Enter glass type------\n')
        new_glass = getGlassTypes()[int(new_glass)]
        #Ask for garnish
        new_garnish = input('Enter garnish: ')
        if(len(new_garnish)<1):
            new_garnish = None
        #Ask for extras
        new_extras = input('Enter extras: ')
        if(len(new_extras)<1):
            new_extras = None
        #Ask for ingredients
        print('Enter exit when finished adding ingredients')
        recipe = {}
        while(True):
            i = 0
            for ingredient in listIngredients():
                print(str(i)+' - '+ingredient.getName())
                i+=1
            new_ingr = input('-----Enter ingredient number-----\n')
            if(new_ingr == 'exit'):
                break
            new_amount = input('Enter amount (mL): ')
            recipe[listIngredients()[int(new_ingr)].getName()] = new_amount
        #Convert recipe into a string
        new_ingredients = ''
        for key, value in recipe.items():
            new_ingredients += str(key)+'@'+str(value)+'#'
        new_ingredients = new_ingredients[:-1]
        #Ask for image reference
        new_img = '0'

        #Create new drink
        createDrink(new_name,new_ice,new_glass,str(new_garnish),str(new_extras),new_ingredients,new_img)

    #print out list of commands with description

    if (user=='help'):

        print('load           - Load data for ingredients and drinks')
        print('save           - Save drinks menu and ingredients to a file')
        print('list           - List a full ingredients list and menu list with relevant data points')
        print('menu           - List all drinks which can be made with current ingredients')
        print('shelf          - List a full ingredients list and menu list with relevant data points')
        print('editshelf      - Swap out ingredients/swap positions')
        print('addIngredient  - Add new ingredient')
        print('editIngredient - Edit an ingredient')
        print('delIngredient  - Delete an Ingredient form the Library')
        print('addDrink       - Add new Drink')
        print('editDrink      - Edit a Drink')
        print('delDrink       - Delete a Drink form the Library')
        print('order          - Order a drink (Default, sending to Arduino via Serial)')
        print('help - List all console commands with description')
        print('exit - Exit and close program')

sys.exit