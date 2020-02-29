import PySimpleGUI as sg
from Ingredient_Library import restoreIngredientLibrary, storeIngredientLibrary, listIngredients, getFamilyTypes, getBaseTypes, deleteIngredient, createIngredient
from Drink_Library import restoreDrinkLibrary, storeDrinkLibrary, listDrinks, deleteDrink, getIceTypes, getGlassTypes, createDrink
import Bartender
import sys
import os
from pathlib import Path

#Initialize display properties
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sg.theme('DarkAmber')

#Fullscreen selector
FULLSCREEN = False

#Load library information
restoreIngredientLibrary()
restoreDrinkLibrary()

def contextSwitcher(current, next, window):

    #Check for Home menu selection
    if(current == 'Home_home'):
        if(next == 'Library_home'):
            #window.hide()
            LibraryGUI(window)
            #window.close()
        
        if(next == 'Ingredients_home'):
            #window.hide()
            IngredientsGUI(window)
            #window.close()

        if(next == 'Stations_home'):
            #window.hide()
            StationsGUI(window)
            #window.close()

    #Check for Library menu selection
    if(current == 'Library_library'):
        if(next == 'Home_library'):
            #window.hide()
            HomeGUI(window)
            #window.close()

        if(next == 'Ingredients_library'):
            #window.hide()
            IngredientsGUI(window)
            #window.close()
        
        if(next == 'Stations_library'):
            #window.hide()
            StationsGUI(window)
            #window.close()

    #Check for Ingredients menu selection
    if(current == 'Ingredients_ingredients'):
        if(next == 'Home_ingredients'):
            #window.hide()
            HomeGUI(window)
            #window.close()

        if(next == 'Library_ingredients'):
            #window.hide()
            LibraryGUI(window)
            #window.close()

        if(next == 'Stations_ingredients'):
            #window.hide()
            StationsGUI(window)
            #window.close()

    #Check for Stations menu selection
    if(current == 'Stations_stations'):
        if(next == 'Home_stations'):
            #window.hide()
            HomeGUI(window)
            #window.close()

        if(next == 'Library_stations'):
            #window.hide()
            LibraryGUI(window)
            #window.close()

        if(next == 'Ingredients_stations'):
            #window.hide()
            IngredientsGUI(window)
            #window.close()


def HomeGUI(prev_window):

    drinkInfo_home = [
                [sg.Text('-DRINK_NAME-',key='DRINK_NAME_home',font=('Helvetica', 15),size=(15,1))],
                [sg.Text('-ICE_NAME-',key='ICE_NAME_home',size=(15,1))],
                [sg.Text('-GLASS_NAME-',key='GLASS_NAME_home',size=(15,1))],
                [sg.Text('-GARNISH_NAME-',key='GARNISH_NAME_home')],
                [sg.Text('-EXTRAS_NAME-',key='EXTRAS_NAME_home')],
                [sg.Text('Ingredients:',font=('Helvetica', 15))],
                [sg.Listbox(['-DRINK_COMPONENTS-'],size=(20,4),key='DrinkIngredients_home')]
            ]
    #Image translation
    placeholder = Path('Image_Library/placeholder.png')
        
    image_layout_home = [
                [sg.Image(filename=placeholder,key='image_home')]
            ]

    layout_home = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_home')],
                [sg.Button('Home',font=('Helvetica', 15),key='Home_home',border_width=5,button_color=(None,'#60b551')),
                sg.Button('Library',font=('Helvetica', 15),key='Library_home'),
                sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_home'),
                sg.Button('Stations',font=('Helvetica', 15),key='Stations_home'),
                sg.Button('Stats',font=('Helvetica', 15),key='Stats_home'),
                sg.Button('Settings',font=('Helvetica', 15),key='Settings_home')],
                [sg.Listbox(Bartender.showDrinkMenu(True),font=('Helvetica', 20),size=(25,8),
                key='Menu_List',enable_events=True),sg.Column(drinkInfo_home),sg.Column(image_layout_home)],
                [sg.Button('Order',font=('Helvetica', 20),size=(25,1))]
            ]

    #Launch Window
    window_home = sg.Window('Barchine', layout_home).Finalize()
    if(FULLSCREEN):
        window_home.Maximize()
    #Close Previous window
    if(prev_window is not None):
        prev_window.close()
    
    while True:  # Event Loop
        event, values = window_home.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Library_home'):
            contextSwitcher('Home_home','Library_home',window_home)
        
        if(event == 'Ingredients_home'):
            contextSwitcher('Home_home','Ingredients_home',window_home)

        if(event == 'Stations_home'):
            contextSwitcher('Home_home','Stations_home',window_home)


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
            window_home.close()
            break


def LibraryGUI(prev_window):

    #Format list of drink names
    drinks_pretty = []
    for drink in listDrinks():
        drinks_pretty.append(drink.getName())

    drinkInfo_library = [
                [sg.Text('-DRINK_NAME-',key='DRINK_NAME_library',font=('Helvetica', 15),size=(15,1))],
                [sg.Text('-ICE_NAME-',key='ICE_NAME_library',size=(15,1))],
                [sg.Text('-GLASS_NAME-',key='GLASS_NAME_library',size=(15,1))],
                [sg.Text('-GARNISH_NAME-',key='GARNISH_NAME_library')],
                [sg.Text('-EXTRAS_NAME-',key='EXTRAS_NAME_library')],
                [sg.Text('Ingredients:',font=('Helvetica', 15))],
                [sg.Listbox(['-DRINK_COMPONENTS-'],size=(20,4),key='DrinkIngredients_library')]
            ]

    #Image translation
    placeholder = Path('Image_Library/placeholder.png')

    image_layout_library = [
                [sg.Image(filename=placeholder,key='image_library')]
            ]

    layout_library = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_library')],
                [sg.Button('Home',font=('Helvetica', 15),key='Home_library'),
                sg.Button('Library',font=('Helvetica', 15),key='Library_library',border_width=5,button_color=(None,'#60b551')),
                sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_library'),
                sg.Button('Stations',font=('Helvetica', 15),key='Stations_library'),
                sg.Button('Stats',font=('Helvetica', 15),key='Stats_library'),
                sg.Button('Settings',font=('Helvetica', 15),key='Settings_library')],
                [sg.Listbox(drinks_pretty,font=('Helvetica', 20),size=(25,8),
                key='Library_List',enable_events=True),sg.Column(drinkInfo_library),sg.Column(image_layout_library)],
                [sg.Button('Add',font=('Helvetica', 15),size=(15,1),key='Add_library'),
                sg.Button('Edit',font=('Helvetica', 15),size=(15,1),key='Edit_library'),
                sg.Button('Delete',font=('Helvetica', 15),size=(15,1),key='Delete_library')]
            ]

    #Launch window
    window_library = sg.Window('Barchine', layout_library).Finalize()
    if(FULLSCREEN):
        window_library.Maximize()

    #Close Previous window
    if(prev_window is not None):
        prev_window.close()

    chosen = None

    while True:  # Event Loop
        event, values = window_library.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Home_library'):
            contextSwitcher('Library_library','Home_library',window_library)

        if(event == 'Ingredients_library'):
            contextSwitcher('Library_library','Ingredients_library',window_library)
        
        if(event == 'Stations_library'):
            contextSwitcher('Library_library','Stations_library',window_library)

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
            window_library.close()
            break

    #Close remaining window
    window_library.close()


def IngredientsGUI(prev_window):

    #Format list of ingredient names
    ingredients_pretty = []
    for ingredient in listIngredients():
        ingredients_pretty.append(ingredient.getName())

    ingredientInfo_ingredients = [
                [sg.Text('-INGREDIENT_NAME-',key='INGREDIENT_NAME_ingredients',font=('Helvetica', 15),size=(30,1))],
                [sg.Text('-FAMILY_NAME-',key='FAMILY_NAME_ingredients',size=(15,1))],
                [sg.Text('-BASE_NAME-',key='BASE_NAME_ingredients',size=(15,1))],
                [sg.Text('-STARTING_VOLUME-',key='STARTING_VOLUME_NAME_ingredients')],
                [sg.Text('-CURRENT_VOLUME-',key='CURRENT_VOLUME_NAME_ingredients')]
            ]

    layout_ingredients = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_ingredients')],
                [sg.Button('Home',font=('Helvetica', 15),key='Home_ingredients'),
                sg.Button('Library',font=('Helvetica', 15),key='Library_ingredients'),
                sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_ingredients',border_width=5,button_color=(None,'#60b551')),
                sg.Button('Stations',font=('Helvetica', 15),key='Stations_ingredients'),
                sg.Button('Stats',font=('Helvetica', 15),key='Stats_ingredients'),
                sg.Button('Settings',font=('Helvetica', 15),key='Settings_ingredients')],
                [sg.Listbox(ingredients_pretty,font=('Helvetica', 20),size=(25,8),
                key='Ingredients_List',enable_events=True),sg.Column(ingredientInfo_ingredients)],
                [sg.Button('Add',font=('Helvetica', 15),size=(15,1),key='Add_ingredients'),
                sg.Button('Edit',font=('Helvetica', 15),size=(15,1),key='Edit_ingredients'),
                sg.Button('Delete',font=('Helvetica', 15),size=(15,1),key='Delete_ingredients')]
            ]

    #Launch window
    window_ingredients = sg.Window('Barchine', layout_ingredients).Finalize()
    if(FULLSCREEN):
        window_ingredients.Maximize()

    #Close Previous window
    if(prev_window is not None):
        prev_window.close()

    chosen = None

    while True:  # Event Loop
        event, values = window_ingredients.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Home_ingredients'):
            contextSwitcher('Ingredients_ingredients','Home_ingredients',window_ingredients)

        if(event == 'Library_ingredients'):
            contextSwitcher('Ingredients_ingredients','Library_ingredients',window_ingredients)

        if(event == 'Stations_ingredients'):
            contextSwitcher('Ingredients_ingredients','Stations_ingredients',window_ingredients)

        #When ingredient item is selected
        if event == 'Ingredients_List':
            for ingredient in listIngredients():
                if(ingredient.getName() == values['Ingredients_List'][0]):
                    chosen = ingredient
                    window_ingredients['INGREDIENT_NAME_ingredients'].update(ingredient.getName())
                    window_ingredients['FAMILY_NAME_ingredients'].update('Family: '+ingredient.getFamily())
                    window_ingredients['BASE_NAME_ingredients'].update('Base: '+ingredient.getBase())
                    window_ingredients['STARTING_VOLUME_NAME_ingredients'].update('Starting Volume: '+str(ingredient.getStartVol())+' mL')
                    window_ingredients['CURRENT_VOLUME_NAME_ingredients'].update('Current Volume: '+str(ingredient.getEndVol())+' mL')
        
        if(event == 'Add_ingredients'):
            print(chosen)
            pass

        if(event == 'Edit_ingredients'):
            print(chosen)
            pass

        if(event == 'Delete_ingredients'):
            print(chosen)
            pass

        if event in  (None, 'Exit'):
            window_ingredients.close()
            break

    #Close remaining window
    window_ingredients.close()


def StationsGUI(prev_window):

     #Image translation
    measurebar = Path('Image_Library/measurementbar.png')

    layout_measure = [
                [sg.Text(text='100%',size=(5,1),font=('Helvetica', 8))],
                [sg.Image(filename=measurebar,key='image_library')],
                [sg.Text(text='0%',size=(3,1),font=('Helvetica', 12))],
            ]

    layout_bar1 = [
            [sg.Text(text='1',size=(2,1),font=('Helvetica', 12),key='bar1_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar1_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar1_name',enable_events=True)],
            ]
    layout_bar2 = [
            [sg.Text(text='2',size=(1,1),font=('Helvetica', 12),key='bar2_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar2_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar2_name',enable_events=True)],
            ]
    layout_bar3 = [
            [sg.Text(text='3',size=(1,1),font=('Helvetica', 12),key='bar3_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar3_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar3_name',enable_events=True)],
            ]
    layout_bar4 = [
            [sg.Text(text='4',size=(1,1),font=('Helvetica', 12),key='bar4_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar4_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar4_name',enable_events=True)],
            ]
    layout_bar5 = [
            [sg.Text(text='5',size=(1,1),font=('Helvetica', 12),key='bar5_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar5_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar5_name',enable_events=True)],
            ]

    layout_bar6 = [
            [sg.Text(text='6',size=(1,1),font=('Helvetica', 12),key='bar6_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar6_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar6_name',enable_events=True)],
            ]

    layout_bar7 = [
            [sg.Text(text='7',size=(1,1),font=('Helvetica', 12),key='bar7_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar7_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar7_name',enable_events=True)],
            ]

    layout_bar8 = [
            [sg.Text(text='8',size=(1,1),font=('Helvetica', 12),key='bar8_num')],
            [sg.ProgressBar(100, orientation='v', size=(10, 30), key='bar8_meter')],
            [sg.Text(text='INSERT NAME HERE',size=(5,4),font=('Helvetica', 8),key='bar8_name',enable_events=True)],
            ]

    layout_stations = [
                [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30),key='title_stations')],
                [sg.Button('Home',font=('Helvetica', 15),key='Home_stations'),
                sg.Button('Library',font=('Helvetica', 15),key='Library_stations'),
                sg.Button('Ingredients',font=('Helvetica', 15),key='Ingredients_stations'),
                sg.Button('Stations',font=('Helvetica', 15),key='Stations_stations',border_width=5,button_color=(None,'#60b551')),
                sg.Button('Stats',font=('Helvetica', 15),key='Stats_stations'),
                sg.Button('Settings',font=('Helvetica', 15),key='Settings_stations')],
                [sg.Text(text='Select Station to Edit',size=(17,1),font=('Helvetica', 20),key='subtitle_stations')],
                [sg.Column(layout_measure),sg.Column(layout_bar1),sg.Column(layout_bar2),
                sg.Column(layout_bar3),sg.Column(layout_bar4),sg.Column(layout_bar5),
                sg.Column(layout_bar6),sg.Column(layout_bar7),sg.Column(layout_bar8),sg.Text(text=' ',size=(10,1))]
            ]

    #Launch window
    window_stations = sg.Window('Barchine', layout_stations).Finalize()
    if(FULLSCREEN):
        window_stations.Maximize()


    #Close Previous window
    if(prev_window is not None):
        prev_window.close()

    #Load bars with shelf items
    i = 1
    for item in Bartender.getShelf():
        if(item!=None):
            window_stations['bar'+str(i)+'_name'].update(value=item.getName())
            window_stations['bar'+str(i)+'_meter'].update_bar(item.getEndVol(),item.getStartVol())
        else:
            window_stations['bar'+str(i)+'_name'].update(value='EMPTY')
            window_stations['bar'+str(i)+'_meter'].update_bar(0,100)
        i+=1

    chosen = None

    while True:  # Event Loop

        event, values = window_stations.read()
        print(event, values)

        #Check for menu selection
        if(event == 'Home_stations'):
            contextSwitcher('Stations_stations','Home_stations',window_stations)

        if(event == 'Library_stations'):
            contextSwitcher('Stations_stations','Library_stations',window_stations)

        if(event == 'Ingredients_stations'):
            contextSwitcher('Stations_stations','Ingredients_stations',window_stations)


        if event in  (None, 'Exit'):
            window_stations.close()
            break

    #Close remaining window
    window_stations.close()

#Launch default home menu
HomeGUI(None)