import PySimpleGUI as sg

sg.theme('DarkAmber')

def CBtn(button_text):
    return sg.Button(button_text,button_color=('white', 'Navy'), size=(3,1)) # use the function to declear multiple button in layout 

layout = [ [sg.Text("Py Simple calculator")],
           [sg.InputText(size=(17,2), font=('Helvetica', 14), text_color='red', key='input')],
           [CBtn('7'), CBtn('8'), CBtn('9'), CBtn('-'), CBtn('x')],
           [CBtn('4'), CBtn('5'), CBtn('6'), CBtn('+'), CBtn('/')],
           [CBtn('1'), CBtn('2'), CBtn('3'), CBtn('C'), CBtn('=')],
           [sg.Button('0', button_color=('white', 'Navy'), size=(23,1))]
         ]

form = sg.FlexForm('pysimplecalc', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout) 


var = " "

while True:
    event, values = form.read()
    
    try:
        if event is '=':
            var = values['input']
            sum = eval(var)
            form.FindElement('input').Update(sum)
    except ZeroDivisionError:
        form.FindElement('input').Update('Error')
    except SyntaxError:
        form.FindElement('input').Update('Error')
    if event is None: # exit button on the top right 
        break
    if event is 'C': #clearing a text area
        form.FindElement('input').Update('')
        
    if event in '*/-+1234567890':
        var = values['input'] # get what's been entered so far  
        var += event # add the new digit  
    # output the final string  
        form.FindElement('input').Update(var) # change the form to reflect current key string  
