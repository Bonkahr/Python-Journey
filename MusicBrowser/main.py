import sqlite3
import tkinter

conn = sqlite3.connect("music.db")

mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1366x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(3, weight=2)
mainWindow.columnconfigure(4, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# labels

tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Artist Listbox

artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL,
                                 command=artistList.yview())
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['vscrollcommand'] = artistScroll.set

# Albums Listbox

albumLV = tkinter.Variable(mainWindow)
albumLV.set('Choose an artist',)
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# Songs Listbox

songLv = tkinter.Variable(mainWindow)
songLv.set('Choose an album')
songList = tkinter.Listbox(mainWindow, listvariable=songLv)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# mainloop

mainWindow.mainloop()
albumLV.set((1, 2, 3, 4, 5))
print('Closing database connection')
conn.close()
