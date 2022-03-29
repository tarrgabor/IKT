import math

from tkinter import *


def terfogat():
    bor = int(mezo1.get())
    a = int(mezo2.get())
    b = int(mezo3.get())
    c = a**2*math.pi*b
    liter = c*0.01
    belefer = c*b
    mennyi = a*b
    telitettseg = c*a
    mezo4.delete(0, END)
    mezo4.insert(0,str(round(c, 2))+" cm3")
    mezo5.delete(0, END)
    mezo5.insert(0,str(round(liter, 2))+" l")
    mezo6.delete(0, END)
    mezo6.insert(0,str(round(belefer))
    mezo7.delete(0, END)
    mezo7.insert(0,str(round(belefer))
    mezo8.delete(0, END)
    mezo8.insert(0,str(round(mennyi, 2))+" l")
    mezo9.delete(0, END)
    mezo9.insert(0,str(round(telitettseg, 2))+" %")
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

cimke=Label(foablak, text="Liter")
cimke.grid(row=5, column=0, sticky='e')

mezo4=Entry(foablak)
mezo4.grid(row=5, column=1)

cimke=Label(foablak, text="Belefér e?")
cimke.grid(row=6, column=0, sticky='e') 

mezo6=Entry(foablak)
mezo6.grid(row=7, column=1)

cimke=Label(foablak, text="Mennyi hely maradt?")
cimke.grid(row=7, column=0, sticky='e') 

mezo7=Entry(foablak)
mezo.grid(row=7, column=1)

cimke=Label(foablak, text="Telitettsége:")
cimke.grid(row=7, column=0, sticky='e') 

mezo8=Entry(foablak)
mezo8.grid(row=8, column=1)



foablak.mainloop()