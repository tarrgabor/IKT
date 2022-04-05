from tkinter import*

def osszegek():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = int(mezo2.get())
    felszin=2*(a*b+b*c+a*c)
    terfogat=a*b*c
    
    mezo4.delete(0, END)
    mezo4.insert(0,str(terfogat))
    mezo5.delete(0, END)
    mezo5.insert(0,str(terfogat))

def ujablak():
    ablak=Toplevel(foablak)
    cimke=Label(foablak, text="Térfogat:")
    cimke.grid(row=1, column=0,)

    mezo4=Entry(foablak)
    mezo4.grid(row=1, column=1)
    
    cimke=Label(foablak, text="Felszin:")
    cimke.grid(row=2, column=0,)

    mezo5=Entry(foablak)
    mezo5.grid(row=1, column=1)
    
    


foablak=Tk()

cimke=Label(foablak, text="a")
cimke.grid(row= 1, column=0)

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1)

cimke=Label(foablak, text="b")
cimke.grid(row=2, column=0)

mezo2=Entry(foablak)
mezo2.grid(row=2, column=1)

cimke=Label(foablak, text="c")
cimke.grid(row=3, column=0)

mezo2=Entry(foablak)
mezo2.grid(row=3, column=1)

gomb1=Button(foablak, text="Számítás", command=ujablak)
gomb1.grid(row=4, column=1)


foablak.mainloop()