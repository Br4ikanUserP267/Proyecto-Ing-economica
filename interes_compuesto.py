import numpy as np

def calcular_vf(vp:float, i:float, n:float) -> float :
    return vp*(1+i)**n

def calcular_vp(vf:float, i:float, n:float) -> float:
    return vf / ((1+i)**n)

def calcular_tasa(vf:float, vp:float, n:float) -> float :
    return np.power((vf/vp), 1/n) - 1

def calcular_tiempo(vf:float, vp:float, i:float) -> float :
    return np.log(vf/vp) / np.log(1+i)
