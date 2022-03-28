import math

from tkinter import *

def terfogat():
    bor =int(mezo1.get())
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a**2*math.pi*b
    liter = c*0.01
    belefer = a*b
    mennyi = a*b
    telitettseg = a*b*c
    mezo4.delete(0, END)
    mezo4.insert(0,str(round(c, 2))+" cm3")
    mezo5.delete(0, END)
    mezo5.insert(0,str(round(liter, 2))+" l")
    mezo6.delete(0, END)
    mezo6.insert(0,str(round(belefer, 2))+" l")
    mezo7.delete(0, END)
    mezo7.insert(0,str(round(mennyi, 2))+" l")
    mezo8.delete(0, END)
    mezo8.insert(0,str(round(telitettseg, 2))+" %")

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

cimke=Label(foablak, text="Liter:")
cimke.grid(row=5, column=0, sticky='e')

mezo4=Entry(foablak)
mezo4.grid(row=5, column=1)

cimke=Label(foablak, text="Belefér e a bor?")
cimke.grid(row=6, column=0, sticky='e')

mezo5=Entry(foablak)
mezo5.grid(row=6, column=1)

cimke=Label(foablak, text="Mennyi hely maradt még benne?")
cimke.grid(row=7, column=0, sticky='e')

mezo5=Entry(foablak)
mezo5.grid(row=7, column=1)

cimke=Label(foablak, text="Telítettség")
cimke.grid(row=8, column=0, sticky='e')

mezo5=Entry(foablak)
mezo5.grid(row=8, column=1)

foablak.mainloop()