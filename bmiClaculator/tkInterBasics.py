import tkinter as tk

window = tk.Tk()
# greetings = tk.Label(text='GUI APP')
# greetings.pack()
# window.mainloop()

# widgets in tkinter
# 1. Label-displays text on a screen
# 2. Button-button containing text and can perform an action when clicked
# 3. Entry-a text entry, allows a single line of text
# 4. Text-text entry allowing multiple lines
# 5. Frame-rectangular region used to group related widgets or provide padding

label = tk.Label(
    text='learning to TK',
    foreground='gray',
    background='white'
)

window.mainloop()