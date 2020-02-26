import PySimpleGUI as sg
import sys
import os

#Initialize display properties
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sg.theme('DarkAmber')

layout = [[sg.Button('Order'),sg.Button('Library'),sg.Button('Ingredients'),sg.Button('Settings')],
          [sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Barchine', layout).Finalize()
window.Maximize()

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == 'Order':
        window['-OUTPUT-'].update('Main Search')
    if event == 'Library':
        window['-OUTPUT-'].update('Library')
    if event == 'Ingredients':
        window['-OUTPUT-'].update('Ingredients')
    if event == 'Settings':
        window['-OUTPUT-'].update('Settings')
        
    if event in  (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()