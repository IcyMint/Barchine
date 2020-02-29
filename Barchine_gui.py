import PySimpleGUI as sg
from Ingredient_Library import restoreIngredientLibrary, storeIngredientLibrary, listIngredients, getFamilyTypes, getBaseTypes, deleteIngredient, createIngredient
from Drink_Library import restoreDrinkLibrary, storeDrinkLibrary, listDrinks, deleteDrink, getIceTypes, getGlassTypes, createDrink
import Bartender
import sys
import os

MENU = 'Home'

#Initialize display properties
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sg.theme('DarkAmber')

#Load library information
restoreIngredientLibrary()
restoreDrinkLibrary()

def HomeGUI():

    drinkInfo_home = [
                [sg.Text('-DRINK_NAME-',key='DRINK_NAME_home',font=('Helvetica', 15),size=(30,1))],
                [sg.Text('-ICE_NAME-',key='ICE_NAME_home',size=(12,1))],
                [sg.Text('-GLASS_NAME-',key='GLASS_NAME_home',size=(30,1))],
                [sg.Text('-GARNISH_NAME-',key='GARNISH_NAME_home')],
                [sg.Text('-EXTRAS_NAME-',key='EXTRAS_NAME_home')],
                [sg.Text('Ingredients:',font=('Helvetica', 15))],
                [sg.Listbox(['-DRINK_COMPONENTS-'],size=(20,4),key='DrinkIngredients_home')]
            ]

    layout_home = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_home')],
                [sg.Button('Home',font=('Helvetica', 15),key='Home_home'),
                sg.Button('Library',font=('Helvetica', 15),key='Library_home'),
                sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_home'),
                sg.Button('Stations',font=('Helvetica', 15),key='Stations_home'),
                sg.Button('Stats',font=('Helvetica', 15),key='Stats_home'),
                sg.Button('Settings',font=('Helvetica', 15),key='Settings_home')],
                [sg.Listbox(Bartender.showDrinkMenu(True),font=('Helvetica', 20),size=(25,8),key='Menu_List',enable_events=True),sg.Column(drinkInfo_home)],
                [sg.Button('Order',font=('Helvetica', 20),size=(25,1))]
            ]

    window_home = sg.Window('Barchine', layout_home).Finalize()
    #window_home.Maximize()
    
    while True:  # Event Loop
        event, values = window_home.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Library_home'):
            window_home.close()
            LibraryGUI()

        #When drink menu item is selected
        if event == 'Menu_List':
            for drink in Bartender.showDrinkMenu(False):
                if(drink.getName() == values['Menu_List'][0]):
                    window_home['DRINK_NAME_home'].update(drink.getName())
                    window_home['ICE_NAME_home'].update('Ice: '+drink.getIce())
                    window_home['GLASS_NAME_home'].update('Glass: '+drink.getGlass())
                    window_home['GARNISH_NAME_home'].update('Garnish: '+drink.getGarnish())
                    window_home['EXTRAS_NAME_home'].update('Extras: '+drink.getExtras())
                    #Retrieve list of ingredients formatted
                    display = []
                    for key, value in drink.getIngredients().items():
                        display.append(str(key)+str(value).rjust(20, ' '))

                    window_home['DrinkIngredients_home'].update(display)
            
        if event in  (None, 'Exit'):
            break


def LibraryGUI():

    #Format list of drink names
    drinks_pretty = []
    for drink in listDrinks():
        drinks_pretty.append(drink.getName())

    drinkInfo_library = [
                [sg.Text('-DRINK_NAME-',key='DRINK_NAME_library',font=('Helvetica', 15),size=(30,1))],
                [sg.Text('-ICE_NAME-',key='ICE_NAME_library',size=(12,1))],
                [sg.Text('-GLASS_NAME-',key='GLASS_NAME_library',size=(30,1))],
                [sg.Text('-GARNISH_NAME-',key='GARNISH_NAME_library')],
                [sg.Text('-EXTRAS_NAME-',key='EXTRAS_NAME_library')],
                [sg.Text('Ingredients:',font=('Helvetica', 15))],
                [sg.Listbox(['-DRINK_COMPONENTS-'],size=(20,4),key='DrinkIngredients_library')]
            ]

    layout_library = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_library')],
            [sg.Button('Home',font=('Helvetica', 15),key='Home_library'),
            sg.Button('Library',font=('Helvetica', 15),key='Library_library'),
            sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_library'),
            sg.Button('Stations',font=('Helvetica', 15),key='Stations_library'),
            sg.Button('Stats',font=('Helvetica', 15),key='Stats_library'),
            sg.Button('Settings',font=('Helvetica', 15),key='Settings_library')],
            [sg.Listbox(drinks_pretty,font=('Helvetica', 20),size=(25,8),key='Library_List',enable_events=True),sg.Column(drinkInfo_library)],
            [sg.Button('Add',font=('Helvetica', 15),size=(15,1),key='Add_library'),
            sg.Button('Edit',font=('Helvetica', 15),size=(15,1),key='Edit_library'),
            sg.Button('Delete',font=('Helvetica', 15),size=(15,1),key='Delete_library')]
            ]

    window_library = sg.Window('Barchine', layout_library).Finalize()
    #window_library.Maximize()

    chosen = None

    while True:  # Event Loop
        event, values = window_library.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Home_library'):
            window_library.close()
            HomeGUI()

         #When drink item is selected
        if event == 'Library_List':
            for drink in listDrinks():
                if(drink.getName() == values['Library_List'][0]):
                    chosen = drink
                    window_library['DRINK_NAME_library'].update(drink.getName())
                    window_library['ICE_NAME_library'].update('Ice: '+drink.getIce())
                    window_library['GLASS_NAME_library'].update('Glass: '+drink.getGlass())
                    window_library['GARNISH_NAME_library'].update('Garnish: '+drink.getGarnish())
                    window_library['EXTRAS_NAME_library'].update('Extras: '+drink.getExtras())
                    #Retrieve list of ingredients formatted
                    display = []
                    for key, value in drink.getIngredients().items():
                        display.append(str(key)+str(value).rjust(20, ' '))

                    window_library['DrinkIngredients_library'].update(display)

        if(event == 'Add_library'):
            print(chosen)
            pass

        if(event == 'Edit_library'):
            print(chosen)
            pass

        if(event == 'Delete_library'):
            print(chosen)
            pass

        if event in  (None, 'Exit'):
                break

    #Close remaining window
    window_library.close()


#Launch default home menu
HomeGUI()