import math

from tkinter import *

def terfogat():
    bor =int(mezo1.get())
    a = int(mezo1.get())
    b = int(mezo2.get())
    terfogat = round (math.pi * a * a * b * 0.01)
    liter=terfogat*0.01
    if liter <= bor:
        mezo5.delete(0, END)
        mezo5.insert(0,"Nem fér bele")
    else:
        mezo5.delete(0, END)
        mezo5.insert(0,"Belefér")
    MUKODJMARMERTNEMIRJAKIIGAZABOLMENNYIHELYVANBENNE = liter - bor
    telitettseg = round (bor * (100 / terfogat))
    mezo3.delete(0, END)
    mezo3.insert(0,str(round(terfogat, 0))+" cm3")
    mezo6.delete(0, END)
    mezo6.insert(0,str(round(MUKODJMARMERTNEMIRJAKIIGAZABOLMENNYIHELYVANBENNE))+" l")
    mezo7.delete(0, END)
    mezo7.insert(0,str(round(telitettseg, 0))+" %")

foablak=Tk()
foablak.config()

gyoker = 'H:\\ikt project munka\\python\\képek\\'
icon = PhotoImage(file=gyoker+'log-cartoon-png-6.png')
foablak.iconphoto(True, icon)

cimke=Label(foablak, text="Bor(L):")
cimke.grid(row= 0, column=0, sticky='e')

mezo0=Entry(foablak)
mezo0.grid(row=0, column=1)

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


cimke=Label(foablak, text="Belefér-e a bor?")
cimke.grid(row=6, column=0, sticky='e')

mezo5=Entry(foablak)
mezo5.grid(row=6, column=1)

cimke=Label(foablak, text="Mennyi hely maradt még benne?")
cimke.grid(row=7, column=0, sticky='e')

mezo6=Entry(foablak)
mezo6.grid(row=7, column=1)

cimke=Label(foablak, text="Telítettség")
cimke.grid(row=8, column=0, sticky='e')

mezo7=Entry(foablak)
mezo7.grid(row=8, column=1)

foablak.mainloop()