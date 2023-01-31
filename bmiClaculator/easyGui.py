import easygui as gui

fav_color = gui.buttonbox(
    msg='What is your favourite color?',
    title='Choose your favourite color',
    choices=['Red', 'Blue', 'Violet', 'Black'],
)  # Returns the value of the chosen item

colors = ['Red', 'Blue', 'Violet', 'Black']
fav_color_index = gui.indexbox(
    msg='What is your favourite color?',
    title='Choose your favourite color',
    choices=colors,
)  # return the index of the color chosen

gui.msgbox(msg=f'You chose: {fav_color}', title='Color chosen', ok_button='OK')

name = gui.enterbox(
    msg='Please enter your name',
    title='User Name'
)

gui.msgbox(msg=f'You entered name: {name}', title='Your Name', ok_button='OK')

# file selection from the system/directories
# Return the full path of the fle chosen

file = gui.fileopenbox(title='Select file')

# Returns the full path to save the file
file_save = gui.filesavebox(title='Save File')
