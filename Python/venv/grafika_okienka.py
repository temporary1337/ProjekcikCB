#biblioteka Tkinter jest wbudowana, toporna ale dziala
#biblioteka wxPython juz nie, open source
#biblioteka Jpython, port na Jave. Pozwala uzywac calej biblioteki Javy do okienek itp
import tkinter
import tkinter.messagebox

#tworzenie glownego okna
MainWindow = tkinter.Tk() #Tk to konstruktor okna

#GUZIOK
def klyk():
    print(MielenieWartosc.get())
    print(OproznianieWartosc.get()) #.get() zwraca wartosc variabla przed kropkom
def klek():
    tkinter.messagebox.showinfo('Warning', 'HeHe') #jest tez .showerror

def klok():
    import zadanie_maj

guziok1 = tkinter.Button(MainWindow, text = 'Hy hy', command = klyk)
guziok2 = tkinter.Button(MainWindow, text = 'He he', command = klek)
guziok3 = tkinter.Button(MainWindow, text = 'Włącz młyn', command = klok)

guziok1.grid(row = 0, column = 1)
guziok2.grid(row = 0, column = 2)
guziok3.grid(row = 0, column = 3)

#Check Button
MielenieWartosc = tkinter.BooleanVar()
OproznianieWartosc = tkinter.BooleanVar()
guziok4 = tkinter.Checkbutton(MainWindow, text = 'Mielenie', onvalue = True, offvalue = False, variable = MielenieWartosc)
guziok5 = tkinter.Checkbutton(MainWindow, text = 'Oproznianie', onvalue = True, offvalue = False, variable = OproznianieWartosc)

guziok4.grid(row = 1, column = 1)
guziok5.grid(row = 2, column = 1)

#Radio Button
RVar = tkinter.BooleanVar()
guziok6 = tkinter.Radiobutton(MainWindow, text='Opt1', variable = MielenieWartosc, value = True, command=klyk)
guziok7 = tkinter.Radiobutton(MainWindow, text='Opt2', variable = OproznianieWartosc, value = False, command=klyk)
guziok8 = tkinter.Radiobutton(MainWindow, text='Opt3', variable = MielenieWartosc, value = False, command=klyk)

guziok6.grid(row = 1, column = 3)
guziok7.grid(row = 2, column = 3)
guziok8.grid(row = 3, column = 3)

#Entry
def kluk():
    tkinter.messagebox.showerror('Ty jesteś młynarzem, wysłałeś list do siebie', E1.get())

guziok9 = tkinter.Button(MainWindow, text = 'Wyślij list', command = kluk)

L1 = tkinter.Label(MainWindow, text = 'List do młynarza')
E1 = tkinter.Entry(MainWindow)

guziok9.grid(row = 5, column = 2)
L1.grid(row = 6, column = 1)
E1.grid(row = 6, column = 2)

#Listbox
Lb1 = tkinter.Listbox(MainWindow, selectmode = 'multiple')
Lb1.insert(1, "C")
Lb1.insert(2, "C++")
Lb1.insert(3, "C#")
Lb1.insert(4, ".NET")

Lb1.grid(row = 7, column = 2)

#Canvas
C = tkinter.Canvas(MainWindow, width = 300, height = 250)

coord = 10,50,240,210
mlyn = PhotoImage(file = "mlyn.bmp")#C.create_arc(coord, start = 10, fill = "green")
image = canvas.create_image(250, 300, anchor=NE, image = mlyn)

C.grid(row = 7, column = 3)

#Grid
#glowna petla do startowania okna
MainWindow.mainloop()