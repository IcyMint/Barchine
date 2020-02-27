import PySimpleGUI as sg
from Ingredient_Library import restoreIngredientLibrary, storeIngredientLibrary, listIngredients, getFamilyTypes, getBaseTypes, deleteIngredient, createIngredient
from Drink_Library import restoreDrinkLibrary, storeDrinkLibrary, listDrinks, deleteDrink, getIceTypes, getGlassTypes, createDrink
import Bartender
import sys
import os

#Initialize display properties
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sg.theme('DarkAmber')

#Load library information
restoreIngredientLibrary()
restoreDrinkLibrary()

columnInfo = [
                [sg.Text('-DRINK_NAME-',key='-DRINK_NAME-',font=('Helvetica', 15),size=(30,1))],
                [sg.Text('-ICE_NAME-',key='-ICE_NAME-',size=(12,1))],
                [sg.Text('-GLASS_NAME-',key='-GLASS_NAME-',size=(30,1))],
                [sg.Text('-GARNISH_NAME-',key='-GARNISH_NAME-')],
                [sg.Text('-EXTRAS_NAME-',key='-EXTRAS_NAME-')],
                [sg.Text('Ingredients:',font=('Helvetica', 15))],
                [sg.Listbox(['-DRINK_COMPONENTS-'],size=(20,4),key='Menu_DrinkIngredients')]
            ]

layout = [
            [sg.Text(text='Barchine',size=(8,1),font=('Helvetica', 30))],
            [sg.Button('Home',font=('Helvetica', 15)),sg.Button('Library',font=('Helvetica', 15)),sg.Button('Ingredients',font=('Helvetica', 15)),sg.Button('Stations',font=('Helvetica', 15)),sg.Button('Stats',font=('Helvetica', 15)),sg.Button('Settings',font=('Helvetica', 15))],
            [sg.Listbox(Bartender.showDrinkMenu(True),font=('Helvetica', 20),size=(25,8),key='Menu_List',enable_events=True),sg.Column(columnInfo)],
            [sg.Input(key='-IN-')]
        ]

window = sg.Window('Barchine', layout).Finalize()
#window.Maximize()

while True:  # Event Loop
    event, values = window.read()
    print(event, values)

    #When drink menu item is selected
    if event == 'Menu_List':
        for drink in Bartender.showDrinkMenu(False):
            if(drink.getName() == values['Menu_List'][0]):
                window['-DRINK_NAME-'].update(drink.getName())
                window['-ICE_NAME-'].update('Ice: '+drink.getIce())
                window['-GLASS_NAME-'].update('Glass: '+drink.getGlass())
                window['-GARNISH_NAME-'].update('Garnish: '+drink.getGarnish())
                window['-EXTRAS_NAME-'].update('Extras: '+drink.getExtras())
                #Retrieve list of ingredients formatted
                display = []
                for key, value in drink.getIngredients().items():
                    display.append(str(key)+str(value).rjust(20, ' '))

                window['Menu_DrinkIngredients'].update(display)
        
    if event in  (None, 'Exit'):
        break
    if event == 'Show':
        # Update the 'output' text element to be the value of 'input' element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()