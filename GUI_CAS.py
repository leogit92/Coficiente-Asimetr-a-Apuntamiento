from tkinter import *
from tkinter.ttk import Treeview

import ControladorM3M4 as CM
#from tkinter.ttk import *

root = Tk()


#LblLnBS = Label(root, text=" ")
#LblLnBS.grid(row=0,column=0)
LblM3 = Label(root, text="Datos separados por - ")
#Lbl.grid(row=1,column=0)
LblM3.place(x=40,y=17)
entM3 = Entry(root, width=40)
#ent.grid(row=1,column=1,columnspan=3)
entM3.place(x=180,y=17)
LblM4 = Label(root, text="Datos separados por - ")
LblM4.place(x=640,y=17)
entM4 = Entry(root, width=40)
entM4.place(x=780,y=17)

TblCm3 = Treeview(root,columns=11)
TblCm3['columns'] = ["πΒ Μ ","Xi","Fi","ππβπΒ Μ ","(ππβπΒ Μ)Β²","(ππβπΒ Μ)Β²x Fi","(π±π’βπ±Β Μ)Β³","(π±π’βπ±Β Μ)Β³x Fi"]
TblCm3['show'] = "headings"
TblCm3.heading("πΒ Μ ",text="πΒ Μ ")
TblCm3.heading("Xi",text="Xi")
TblCm3.heading("Fi",text="Fi")
TblCm3.heading("ππβπΒ Μ ",text="ππβπΒ Μ ")
TblCm3.heading("(ππβπΒ Μ)Β²",text="(ππβπΒ Μ)Β²")
TblCm3.heading("(ππβπΒ Μ)Β²x Fi",text="(ππβπΒ Μ)Β²x Fi")
TblCm3.heading("(π±π’βπ±Β Μ)Β³",text="(π±π’βπ±Β Μ)Β³")
TblCm3.heading("(π±π’βπ±Β Μ)Β³x Fi",text="(π±π’βπ±Β Μ)Β³x Fi")
TblCm3.column("πΒ Μ ",minwidth=0,width=55, stretch=NO)
TblCm3.column("Xi",minwidth=0,width=55, stretch=NO)
TblCm3.column("Fi",minwidth=0,width=55, stretch=NO)
TblCm3.column("ππβπΒ Μ ",minwidth=0,width=70, stretch=NO)
TblCm3.column("(ππβπΒ Μ)Β²",minwidth=0,width=70, stretch=NO)
TblCm3.column("(ππβπΒ Μ)Β²x Fi",minwidth=0,width=70, stretch=NO)
TblCm3.column("(π±π’βπ±Β Μ)Β³",minwidth=0,width=70, stretch=NO)
TblCm3.column("(π±π’βπ±Β Μ)Β³x Fi",minwidth=0,width=70, stretch=NO)

TblCm3.place(x=30,y=50)

LblVar3 = Label(root, text="Varianza (SΒ²) = ")
LblVar3.place(x=45,y=300)
LblVar3S = Label(root, text=" ")
LblVar3S.place(x=200,y=300)
LblDesv3 = Label(root, text="DesviaciΓ³n estΓ‘ndar (S) = ")
LblDesv3.place(x=45,y=340)
LblDesv3S = Label(root, text=" ")
LblDesv3S.place(x=200,y=340)
LblM3 = Label(root, text="Momento de orden 3 (mΒ³) = ")
LblM3.place(x=45,y=380)
LblM3S = Label(root, text=" ")
LblM3S.place(x=200,y=380)
LblAS3 = Label(root, text="AsimetrΓ­a (AS) = ")
LblAS3.place(x=45,y=420)
LblAS3S = Label(root, text=" ")
LblAS3S.place(x=200,y=420)
LblMA3 = Label(root, text="Media (Β Μπ ) = ")
LblMA3.place(x=45,y=460)
LblMA3S = Label(root, text=" ")
LblMA3S.place(x=200,y=460)

TblCm4 = Treeview(root,columns=11)
TblCm4['columns'] = ["πΒ Μ ","Xi","Fi","ππβπΒ Μ ","(ππβπΒ Μ)Β²","(ππβπΒ Μ)Β²x Fi","(π±π’βπ±Β Μ )^π","(π±π’βπ±Β Μ)^πxFi"]
TblCm4['show'] = "headings"
TblCm4.heading("πΒ Μ ",text="πΒ Μ ")
TblCm4.heading("Xi",text="Xi")
TblCm4.heading("Fi",text="Fi")
TblCm4.heading("ππβπΒ Μ ",text="ππβπΒ Μ ")
TblCm4.heading("(ππβπΒ Μ)Β²",text="(ππβπΒ Μ)Β²")
TblCm4.heading("(ππβπΒ Μ)Β²x Fi",text="(ππβπΒ Μ)Β²x Fi")
TblCm4.heading("(π±π’βπ±Β Μ )^π",text="(π±π’βπ±Β Μ )^π")
TblCm4.heading("(π±π’βπ±Β Μ)^πxFi",text="(π±π’βπ±Β Μ)^πxFi")
TblCm4.column("πΒ Μ ",minwidth=0,width=55, stretch=NO)
TblCm4.column("Xi",minwidth=0,width=55, stretch=NO)
TblCm4.column("Fi",minwidth=0,width=55, stretch=NO)
TblCm4.column("ππβπΒ Μ ",minwidth=0,width=70, stretch=NO)
TblCm4.column("(ππβπΒ Μ)Β²",minwidth=0,width=70, stretch=NO)
TblCm4.column("(ππβπΒ Μ)Β²x Fi",minwidth=0,width=70, stretch=NO)
TblCm4.column("(π±π’βπ±Β Μ )^π",minwidth=0,width=70, stretch=NO)
TblCm4.column("(π±π’βπ±Β Μ)^πxFi",minwidth=0,width=80, stretch=NO)

TblCm4.place(x=630,y=50)

LblVar4 = Label(root, text="Varianza (SΒ²) = ")
LblVar4.place(x=645,y=300)
LblVar4S = Label(root, text=" ")
LblVar4S.place(x=800,y=300)
LblDesv4 = Label(root, text="DesviaciΓ³n estΓ‘ndar (S) = ")
LblDesv4.place(x=645,y=340)
LblDesv4S = Label(root, text=" ")
LblDesv4S.place(x=800,y=340)
LblM4 = Label(root, text="Momento de orden 4 (mβ΄) = ")
LblM4.place(x=645,y=380)
LblM4S = Label(root, text=" ")
LblM4S.place(x=800,y=380)
LblAS4 = Label(root, text="AsimetrΓ­a (AS) = ")
LblAS4.place(x=645,y=420)
LblAS4S = Label(root, text=" ")
LblAS4S.place(x=800,y=420)
LblAP4 = Label(root, text="Apuntamiento (AP) = ")
LblAP4.place(x=645,y=460)
LblAP4S = Label(root, text=" ")
LblAP4S.place(x=800,y=460)
LblMA4 = Label(root, text="Media (Β Μπ ) = ")
LblMA4.place(x=645,y=500)
LblMA4S = Label(root, text=" ")
LblMA4S.place(x=800,y=500)

def LlenarTablaM3(DicDat):
    NFil = 0
    NCol = 0
    FilDat = TblCm3.get_children()
    #print(x)
    if len(FilDat) > 0:
        for item in FilDat:
            TblCm3.delete(item)
    cont = 1
    for key,Val in DicDat['Tab']["Xi"].items():
        LDat = []
        if cont == len(DicDat['Tab']["Xi"]):
            LDat.append("SUMA")
        elif cont > 1:
            LDat.append(" ")
        else:
            LDat.append(DicDat["MA"])
        cont += 1
        for Tal,Dat in DicDat['Tab'].items():
            #print(Dat)
            for keyD,ValD in Dat.items():
                if keyD == key:
                    LDat.append(ValD) 
        TblCm3.insert('',NFil,NCol,values=LDat)
        NFil += 1
        NCol += 1

def LlenarTablaM4(DicDat):
    NFil = 0
    NCol = 0
    FilDat = TblCm4.get_children()
    #print(x)
    if len(FilDat) > 0:
        for item in FilDat:
            TblCm4.delete(item)
    cont = 1
    for key,Val in DicDat['Tab']["Xi"].items():
        LDat = []
        if cont == len(DicDat['Tab']["Xi"]):
            LDat.append("SUMA")
        elif cont > 1:
            LDat.append(" ")
        else:
            LDat.append(DicDat["MA"])
        cont += 1
        for Tal,Dat in DicDat['Tab'].items():
            #print(Dat)
            for keyD,ValD in Dat.items():
                if keyD == key:
                    LDat.append(ValD) 
        TblCm4.insert('',NFil,NCol,values=LDat)
        NFil += 1
        NCol += 1


def PDTM3():
    #LblRango['text'] = f"El rango es: {ent.get()}"
    VarR = str(entM3.get())
    ListVR = VarR.split('-')
    #ListINT = [int(ND) for ND in ListVR]
    ListINT = [float(ND) for ND in ListVR]
    #DicDT = CCal.FirstFormule(ListINT)
    DicDT = CM.DictFormuleM3(ListINT)
    LblVar3S['text'] = f"{DicDT['FM3']['S2']}"
    LblDesv3S['text'] = f"{DicDT['FM3']['S']}"
    LblM3S['text'] = f"{DicDT['FM3']['M3']}"
    LblAS3S['text'] = f"{DicDT['FM3']['AS']}"
    LblMA3S['text'] = f"{DicDT['FM3']['MA']}"
    LlenarTablaM3(DicDT['FM3'])

def PDTM4():
    #LblRango['text'] = f"El rango es: {ent.get()}"
    VarR = str(entM4.get())
    ListVR = VarR.split('-')
    #ListINT = [int(ND) for ND in ListVR]
    ListINT = [float(ND) for ND in ListVR]
    #DicDT = CCal.FirstFormule(ListINT)
    DicDT = CM.DictFormuleM4(ListINT)
    LblVar4S['text'] = f"{DicDT['FM4']['S2']}"
    LblDesv4S['text'] = f"{DicDT['FM4']['S']}"
    LblM4S['text'] = f"{DicDT['FM4']['M4']}"
    LblAS4S['text'] = f"{DicDT['FM4']['AS']}"
    LblAP4S['text'] = f"{DicDT['FM4']['AP']}"
    LblMA4S['text'] = f"{DicDT['FM4']['MA']}"
    LlenarTablaM4(DicDT['FM4'])
        

    
LblBS = Label(root, text=" ")
LblBS.grid(row=1,column=4,columnspan=2)
LblBS2 = Label(root, text=" ")
LblBS2.grid(row=1,column=5,columnspan=2)
BtnM3 = Button(root, text="Hacer cΓ‘lculos", command=PDTM3)
#Btn1.grid(row=1,column=6)
#Btn1.place(x=1100,y=17)
BtnM3.place(x=450,y=17)
BtnM4 = Button(root, text="Hacer cΓ‘lculos", command=PDTM4)
BtnM4.place(x=1060,y=17)


root.geometry("1200x540")
root.title("Coeficiente absoluto de AsimetrΓ­a y Apuntamiento")
root.mainloop()