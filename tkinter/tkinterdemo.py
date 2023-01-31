import tkinter

main_window = tkinter.Tk()
main_window.title('My First GUI program')
main_window.geometry('640x480+8+400')

label = tkinter.Label(main_window, text="ooh my")
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(main_window, relief='raised', borderwidth=3)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure columns
main_window.columnconfigure(0, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')

button3.config(relief='sunken')
right_frame.columnconfigure(0, weight=1)

main_window.mainloop()
