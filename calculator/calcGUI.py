import tkinter

main_window = tkinter.Tk()
main_window.title('Calculator')
main_window.geometry('400x300')

frame = tkinter.Frame(main_window)
frame.grid(column=1)

button_1 = tkinter.Button(frame, text='1')
button_1.grid(row=0, column=0)
button_2 = tkinter.Button(frame, text='2')
button_2.grid(row=0, column=1)
button_3 = tkinter.Button(frame, text='3')
button_3.grid(row=0, column=2)
button_4 = tkinter.Button(frame, text='4')
button_4.grid(row=1, column=0)
button_5 = tkinter.Button(frame, text='5')
button_5.grid(row=1, column=1)
button_6 = tkinter.Button(frame, text='6')
button_6.grid(row=1, column=2)
button_7 = tkinter.Button(frame, text='7')
button_7.grid(row=2, column=0)
button_8 = tkinter.Button(frame, text='8')
button_8.grid(row=2, column=1)
button_9 = tkinter.Button(frame, text='9')
button_9.grid(row=2, column=2)
button_0 = tkinter.Button(frame, text='0')
button_0.grid(row=2, column=3)


main_window.mainloop()
