from Ingredient_Library import restoreIngredientLibrary, storeIngredientLibrary, listIngredients
from Drink_Library import restoreDrinkLibrary, storeDrinkLibrary, listDrinks
import Bartender
import sys

print('Barchine::Made by Diego Bonilla, 2016')
print('type "help" to list all commands')

user = ''

#Main console loop

while(user!='exit'):

    user = input('')

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



    #print out list of commands with description

    if (user=='help'):

        print('load - Load data for ingredients and drinks')
        print('save - Save drinks menu and ingredients to a file')
        print('verify - Check for low stock and invalid drink recipes')
        print('list - List a full ingredients list and menu list with relevant data points')
        print('order - Order a drink (Default, sending to Arduino via Serial)')
        print('edit - Edit entries for both drinks and ingredients')
        print('add - Add a new drink or ingredient to the system')
        print('delete - Remove a drink or ingredient from the system')
        print('help - List all console commands with description')
        print('exit - Exit and close program')

sys.exit