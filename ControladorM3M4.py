from statistics import *
from math import *

from sympy import LM


def DictFormuleM3(Datos: list):
    Datos.sort()
    LMed = []
    for item in Datos:
        if not item in LMed:
            LMed.append(item)
    DictDatosR = dict()
    DictDatosR['FM3'] = {}
    DictDatosR['FM3']['Tab'] = {}
    DictDatosR['FM3']['Tab']["Xi"] = {}
    DictDatosR['FM3']['Tab']["Fi"] = {}
    DictDatosR['FM3']['Tab']["XiX"] = {}
    DictDatosR['FM3']['Tab']["XiX2"] = {}
    DictDatosR['FM3']['Tab']["XiX2Fi"] = {}
    DictDatosR['FM3']['Tab']["XiX3"] = {}
    DictDatosR['FM3']['Tab']["XiX3Fi"] = {}
    DictDatosR['FM3']['S2'] = round(variance(LMed),3)
    DictDatosR['FM3']['S'] = round(sqrt(DictDatosR['FM3']['S2']),3)
    DictDatosR['FM3']['MA'] = mean(LMed)
    #for item in Datos:
    for item in Datos:
        existe = False
        VarT = "V"+str(item)
        for key,val in DictDatosR['FM3']['Tab']["Fi"].items():
            if key == VarT:
                existe = True
        if existe != True:
            #print(DictDatosR["FM3"]["MA"])
            #print(item)
            DictDatosR['FM3']['Tab']["Xi"][VarT]=item
            DictDatosR['FM3']['Tab']["Fi"][VarT]=0
            DictDatosR['FM3']['Tab']["Fi"][VarT] = Datos.count(item)
            DictDatosR['FM3']['Tab']["XiX"][VarT]=DictDatosR['FM3']['Tab']["Xi"][VarT]-DictDatosR['FM3']['MA']
            DictDatosR['FM3']['Tab']["XiX2"][VarT] = pow(DictDatosR['FM3']['Tab']["XiX"][VarT],2)
            DictDatosR['FM3']['Tab']["XiX2Fi"][VarT] = DictDatosR['FM3']['Tab']["XiX2"][VarT]*DictDatosR['FM3']['Tab']["Fi"][VarT]
            DictDatosR['FM3']['Tab']["XiX3"][VarT] = pow(DictDatosR['FM3']['Tab']["XiX"][VarT],3)
            DictDatosR['FM3']['Tab']["XiX3Fi"][VarT] = DictDatosR['FM3']['Tab']["XiX3"][VarT]*DictDatosR['FM3']['Tab']["Fi"][VarT]
    DictDatosR['FM3']['Tab']["Xi"]["SM"]=" "
    DictDatosR['FM3']['Tab']["XiX"]["SM"]=" "
    #print(DictDatosR['FM3']['Tab']["Xi"])
    lTipo = ["Fi","XiX2","XiX2Fi","XiX3","XiX3Fi"]
    for DT in lTipo:
        VSuma = 0
        for key,dat in DictDatosR["FM3"]['Tab'][DT].items():
            #print(dat)
            VSuma += dat
        DictDatosR['FM3']['Tab'][DT]["SM"] = VSuma
    DictDatosR['FM3']['M3'] = round(DictDatosR['FM3']['Tab']["XiX3Fi"]["SM"]/DictDatosR['FM3']['Tab']["Fi"]["SM"],3)
    DictDatosR['FM3']['AS'] = round(DictDatosR['FM3']['M3']/(pow(DictDatosR['FM3']['S'],3)),3)

    #print(DictDatosR['FM3']['Tab']["Fi"])
    #print(DictDatosR['FM3']['Tab']["Xi"])
    #print(DictDatosR['FM3']['Tab']["XiX"])
    #print(DictDatosR['FM3']['Tab']["XiX2"])
    #print(DictDatosR['FM3']['Tab']["XiX2Fi"])
    #print(DictDatosR['FM3']['Tab']["XiX3"])
    #print(DictDatosR['FM3']['Tab']["XiX3Fi"])
    return DictDatosR


def DictFormuleM4(Datos: list):
    Datos.sort()
    LMed = []
    for item in Datos:
        if not item in LMed:
            LMed.append(item)
    DictDatosR = dict()
    DictDatosR['FM4'] = {}
    DictDatosR['FM4']['Tab'] = {}
    DictDatosR['FM4']['Tab']["Xi"] = {}
    DictDatosR['FM4']['Tab']["Fi"] = {}
    DictDatosR['FM4']['Tab']["XiX"] = {}
    DictDatosR['FM4']['Tab']["XiX2"] = {}
    DictDatosR['FM4']['Tab']["XiX2Fi"] = {}
    DictDatosR['FM4']['Tab']["XiX4"] = {}
    DictDatosR['FM4']['Tab']["XiX4Fi"] = {}
    DictDatosR['FM4']['S2'] = round(variance(LMed),3)
    DictDatosR['FM4']['S'] = round(sqrt(DictDatosR['FM4']['S2']),3)
    DictDatosR['FM4']['MA'] = mean(LMed)
    #for item in Datos:
    for item in Datos:
        existe = False
        VarT = "V"+str(item)
        for key,val in DictDatosR['FM4']['Tab']["Fi"].items():
            if key == VarT:
                existe = True
        if existe != True:
            #print(DictDatosR["FM3"]["MA"])
            #print(item)
            DictDatosR['FM4']['Tab']["Xi"][VarT]=item
            DictDatosR['FM4']['Tab']["Fi"][VarT]=0
            DictDatosR['FM4']['Tab']["Fi"][VarT] = Datos.count(item)
            DictDatosR['FM4']['Tab']["XiX"][VarT]=DictDatosR['FM4']['Tab']["Xi"][VarT]-DictDatosR['FM4']['MA']
            DictDatosR['FM4']['Tab']["XiX2"][VarT] = pow(DictDatosR['FM4']['Tab']["XiX"][VarT],2)
            DictDatosR['FM4']['Tab']["XiX2Fi"][VarT] = DictDatosR['FM4']['Tab']["XiX2"][VarT]*DictDatosR['FM4']['Tab']["Fi"][VarT]
            DictDatosR['FM4']['Tab']["XiX4"][VarT] = pow(DictDatosR['FM4']['Tab']["XiX"][VarT],4)
            DictDatosR['FM4']['Tab']["XiX4Fi"][VarT] = DictDatosR['FM4']['Tab']["XiX4"][VarT]*DictDatosR['FM4']['Tab']["Fi"][VarT]
    DictDatosR['FM4']['Tab']["Xi"]["SM"]=" "
    DictDatosR['FM4']['Tab']["XiX"]["SM"]=" "
    #print(DictDatosR['FM4']['Tab']["Xi"])
    lTipo = ["Fi","XiX2","XiX2Fi","XiX4","XiX4Fi"]
    for DT in lTipo:
        VSuma = 0
        for key,dat in DictDatosR["FM4"]['Tab'][DT].items():
            #print(dat)
            VSuma += dat
        DictDatosR['FM4']['Tab'][DT]["SM"] = VSuma
    DictDatosR['FM4']['M4'] = round(DictDatosR['FM4']['Tab']["XiX4Fi"]["SM"]/DictDatosR['FM4']['Tab']["Fi"]["SM"],3)
    DictDatosR['FM4']['AS'] = round(DictDatosR['FM4']['M4']/(pow(DictDatosR['FM4']['S'],4)),3)
    DictDatosR['FM4']['AP'] = round(DictDatosR['FM4']['M4']/DictDatosR['FM4']['S2'],3)

    #print(DictDatosR['FM4']['Tab']["Fi"])
    #print(DictDatosR['FM4']['Tab']["Xi"])
    #print(DictDatosR['FM4']['Tab']["XiX"])
    #print(DictDatosR['FM4']['Tab']["XiX2"])
    #print(DictDatosR['FM4']['Tab']["XiX2Fi"])
    #print(DictDatosR['FM4']['Tab']["XiX4"])
    #print(DictDatosR['FM4']['Tab']["XiX4Fi"])
    return DictDatosR



    
