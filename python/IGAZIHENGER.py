import math

from tkinter import *

def terfogat():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a**2*math.pi*b
    fa = 0.66*c
    vas = 7.874*c
    mezo3.delete(0, END)
    mezo3.insert(0,str(round(c, 2))+" cm3")
    mezo4.delete(0, END)
    mezo4.insert(0,str(round(fa, 2))+" g")
    mezo5.delete(0, END)
    mezo5.insert(0,str(round(vas, 2))+" g")

foablak=Tk()
foablak.config()

gyoker = 'H:\\ikt project munka\\python\\képek\\'
icon = PhotoImage(file=gyoker+'log-cartoon-png-6.png')
foablak.iconphoto(True, icon)


cimke=Label(foablak, text="Sugár (cm):")
cimke.grid(row= 1, column=0, sticky='e')

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1)

cimke=Label(foablak, text="Magasság (cm):")
cimke.grid(row=2, column=0, sticky='e')

mezo2=Entry(foablak)
mezo2.grid(row=2, column=1)

gomb=Button(foablak, text="Kiszámít", command=terfogat , pady=3, padx=4,)
gomb.grid(row=3, column=1, sticky='e')

cimke=Label(foablak, text="Térfogat:")
cimke.grid(row=4, column=0, sticky='e')

mezo3=Entry(foablak)
mezo3.grid(row=4, column=1)

cimke=Label(foablak, text="Fahenger:")
cimke.grid(row=5, column=0, sticky='e')

mezo4=Entry(foablak)
mezo4.grid(row=5, column=1)

cimke=Label(foablak, text="Vashenger")
cimke.grid(row=6, column=0, sticky='e') 

mezo5=Entry(foablak)
mezo5.grid(row=6, column=1)


foablak.mainloop()