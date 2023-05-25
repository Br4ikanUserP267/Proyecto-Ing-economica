
#Convierte semestres a años
def convertir_semestres_a_anios(semestres: float) -> float:
    return semestres / 2

def convertir_trimestes_a_anios(trimestres: float) -> float :
    return trimestres / 4

def convertir_meses_a_anios(meses: float) -> float :
    return meses / 12

#Convertir tasas efectivas a tasa efectiva anual
def convertir_tasa_semestral(TES: float) -> float :
    return ((1+TES)**2) - 1

def convertir_tasa_trimestral(TET: float) -> float :
    return ((1+TET)**4) - 1

def convertir_tasa_mensual(TET: float) -> float :
    return ((1+TET)**12) - 1
def convertir_interes_compuesto(monto: float, tasa: float, periodo: float) -> float:
    # Add your conversion logic here
    resultado = monto * (1 + tasa) ** periodo
    return resultado
