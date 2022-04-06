from tkinter import *

def nevjegy():
    abl2=Toplevel(foablak)
    uz2=Message(abl2,text='Készítette: Gipsz Jakab\nPiripócs\n2009.06.04', width=300)
    gomb2=Button(abl2,text='Kilép', command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

def felszin():
    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        felszin=2*(a*b+c*b+a*c)
        mezo4.delete(0,END)
        mezo4.insert(0,str(felszin))
    abl3=Toplevel(foablak)
    abl3.title('A téglatest felszíne')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3,text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    mezo4=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=3, column=2, sticky=W)
    mezo4.grid(row=5, column=2, sticky=W)
    abl3.mainloop()

def terfogat():
    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        terfogat=a*b*c
        mezo4.delete(0,END)
        mezo4.insert(0,str(terfogat))
    abl3=Toplevel(foablak)
    abl3.title('A téglatest térfogata')
    abl3.minsize(width=300, height=100)
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3,text='Számítás', command=szamit)
    mezo1=Entry(abl3)
    mezo2=Entry(abl3)
    mezo3=Entry(abl3)
    mezo4=Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W)
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=3, column=2, sticky=W)
    mezo4.grid(row=5, column=2, sticky=W)
    abl3.mainloop()

foablak=Tk()
foablak.title('A téglatest adatai')
foablak.minsize(width=300, height=100)

menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text='Fájl', underline=0)
menu1.pack(side=LEFT)
fail=Menu(menu1)
fail.add_command(label='Névjegy', command=nevjegy, underline=0)
fail.add_command(label='Kilépés', command=foablak.destroy, underline=0)
menu1.config(menu=fail)

menu2=Menubutton(menusor, text='Téglatest', underline=0)
menu2.pack(side=LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label='Felszín', command=felszin, underline=0)
teglatest.add_command(label='Térfogat', command=terfogat, underline=0)
menu2.config(menu=teglatest)





foablak.mainloop()