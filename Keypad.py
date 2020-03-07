import PySimpleGUI as sg

def Keypad():
    layout = [
            [sg.Text(size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],
            [sg.Input(size=(10, 1), justification='right', key='input',visible=False)],
            [sg.Button('1'), sg.Button('2'), sg.Button('3')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9')],
            [sg.Button('Clear'), sg.Button('0'), sg.Button('Submit')]
    ]

    window = sg.Window('Keypad',layout,default_button_element_size=(5,2),keep_on_top=True,no_titlebar=True,auto_size_buttons=False).Finalize()
    window.BringToFront()

    keys_entered = ''
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == 'Clear':
            keys_entered = ''
            window['out'].update(keys_entered)
        elif event in '1234567890':
            keys_entered = values['input']
            keys_entered += event
            window['out'].update(keys_entered)
        elif event == 'Submit':
            window.close()
            return(values['input'])

        window['input'].update(keys_entered)
    window.close()