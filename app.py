from tkinter import ttk
from tkinter import *

from tkinter import messagebox
import interes_compuesto as icom
import conversor as con
import numpy as np
import numpy_financial as npf
import tkinter as tk

import math



def calcular_amortizacion(tipo_amortizacion):
    try:
        monto_prestamo = float(entrada_principal.get())
        tasa_interes = float(entrada_tasa_interes.get())
        plazo_meses = int(entrada_plazo.get())

        tasa_interes_decimal = tasa_interes / 100

        resultado_amortizacion.delete(1.0, END)

        if tipo_amortizacion == "cuota_fija_con_cuotas_extraordinarias":
            cuota_mensual = monto_prestamo * (tasa_interes_decimal / 12) / (1 - (1 + tasa_interes_decimal / 12) ** -plazo_meses)

            for mes in range(1, plazo_meses + 1):
                if mes in [6, 12, 18]:  # Ejemplo de cuotas extraordinarias en los meses 6, 12 y 18
                    cuota_mensual += 100  # Monto de la cuota extraordinaria
                interes_mensual = monto_prestamo * tasa_interes_decimal / 12
                amortizacion_mensual = cuota_mensual - interes_mensual
                monto_prestamo -= amortizacion_mensual

                resultado_amortizacion.insert(END, f"Mes {mes}: Cuota: {cuota_mensual:.2f} - "
                                                   f"Interés: {interes_mensual:.2f} - "
                                                   f"Amortización: {amortizacion_mensual:.2f} - "
                                                   f"Saldo Restante: {monto_prestamo:.2f}\n")

        elif tipo_amortizacion == "cuota_fija_con_periodo_gracia":
            periodo_gracia = 3  # Ejemplo de período de gracia de 3 meses
            cuota_mensual = monto_prestamo * (tasa_interes_decimal / 12) / (1 - (1 + tasa_interes_decimal / 12) ** -plazo_meses)

            for mes in range(1, plazo_meses + 1):
                if mes <= periodo_gracia:
                    cuota_mensual = 0  # No se realiza el pago durante el período de gracia
                interes_mensual = monto_prestamo * tasa_interes_decimal / 12
                amortizacion_mensual = cuota_mensual - interes_mensual
                monto_prestamo -= amortizacion_mensual

                resultado_amortizacion.insert(END, f"Mes {mes}: Cuota: {cuota_mensual:.2f} - "
                                                   f"Interés: {interes_mensual:.2f} - "
                                                   f"Amortización: {amortizacion_mensual:.2f} - "
                                                   f"Saldo Restante: {monto_prestamo:.2f}\n")

        elif tipo_amortizacion == "cuota_creciente_lineal":
            cuota_inicial = 100  # Ejemplo de cuota inicial
            incremento_cuota = 50  # Ejemplo de incremento de cuota mensual
            cuota_mensual = cuota_inicial

            for mes in range(1, plazo_meses + 1):
                interes_mensual = monto_prestamo * tasa_interes_decimal / 12
                amortizacion_mensual = cuota_mensual - interes_mensual
                monto_prestamo -= amortizacion_mensual
                cuota_mensual += incremento_cuota

                resultado_amortizacion.insert(END, f"Mes {mes}: Cuota: {cuota_mensual:.2f} - "
                                                   f"Interés: {interes_mensual:.2f} - "
                                                   f"Amortización: {amortizacion_mensual:.2f} - "
                                                   f"Saldo Restante: {monto_prestamo:.2f}\n")

        elif tipo_amortizacion == "cuota_creciente_exponencial":
            cuota_inicial = 100  # Ejemplo de cuota inicial
            multiplicador_cuota = 1.1  # Ejemplo de multiplicador para incrementar la cuota mensual
            cuota_mensual = cuota_inicial

            for mes in range(1, plazo_meses + 1):
                interes_mensual = monto_prestamo * tasa_interes_decimal / 12
                amortizacion_mensual = cuota_mensual - interes_mensual
                monto_prestamo -= amortizacion_mensual
                cuota_mensual *= multiplicador_cuota

                resultado_amortizacion.insert(END, f"Mes {mes}: Cuota: {cuota_mensual:.2f} - "
                                                   f"Interés: {interes_mensual:.2f} - "
                                                   f"Amortización: {amortizacion_mensual:.2f} - "
                                                   f"Saldo Restante: {monto_prestamo:.2f}\n")

        else:
            messagebox.showerror("Error", "Tipo de amortización no válido.")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")



def calcular_vf_anualidades_vencidas(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa
    return vf

# Calcula el valor final de anualidades anticipadas
def calcular_vf_anualidades_anticipadas(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa * (1 + tasa)
    return vf

# Calcula el valor final de un gradiente lineal creciente
def calcular_vf_gradiente_lineal_creciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa + cuota * tiempo
    return vf

# Calcula el valor final de un gradiente lineal decreciente
def calcular_vf_gradiente_lineal_decreciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa - cuota * tiempo
    return vf

# Calcula el valor final de un gradiente geométrico creciente
def calcular_vf_gradiente_geometrico_creciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa + cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / (tasa ** 2)
    return vf

# Calcula el valor final de un gradiente geométrico decreciente
def calcular_vf_gradiente_geometrico_decreciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa - cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / (tasa ** 2)
    return vf

# Función para calcular el valor final de anualidades vencidas
def calcular_vf_anualidades_vencidas(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa
    return vf

# Función para calcular el valor final de anualidades anticipadas
def calcular_vf_anualidades_anticipadas(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa * (1 + tasa)
    return vf

# Función para calcular el valor final de un gradiente lineal creciente
def calcular_vf_gradiente_lineal_creciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa + cuota * tiempo
    return vf

# Función para calcular el valor final de un gradiente lineal decreciente
def calcular_vf_gradiente_lineal_decreciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa - cuota * tiempo
    return vf

# Función para calcular el valor final de un gradiente geométrico creciente
def calcular_vf_gradiente_geometrico_creciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa + cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / (tasa ** 2)
    return vf

# Función para calcular el valor final de un gradiente geométrico decreciente
def calcular_vf_gradiente_geometrico_decreciente(cuota, tasa, tiempo):
    vf = cuota * ((1 + tasa) ** tiempo - 1) / tasa - cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / (tasa ** 2)
    return vf


# Función para calcular el valor presente de anualidades vencidas
def calcular_vp_anualidades_vencidas(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa)
    return vp

# Función para calcular el valor presente de anualidades anticipadas
def calcular_vp_anualidades_anticipadas(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa) / (1 + tasa)
    return vp

# Función para calcular el valor presente de un gradiente lineal creciente
def calcular_vp_gradiente_lineal_creciente(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa) - cuota * tiempo / ((1 + tasa) ** tiempo - 1)
    return vp

# Función para calcular el valor presente de un gradiente lineal decreciente
def calcular_vp_gradiente_lineal_decreciente(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa) + cuota * tiempo / ((1 + tasa) ** tiempo - 1)
    return vp

# Función para calcular el valor presente de un gradiente geométrico creciente
def calcular_vp_gradiente_geometrico_creciente(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa) - cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / ((1 + tasa) ** tiempo - 1) / (tasa ** 2)
    return vp

# Función para calcular el valor presente de un gradiente geométrico decreciente
def calcular_vp_gradiente_geometrico_decreciente(vf, cuota, tasa, tiempo):
    vp = vf / ((1 + tasa) ** tiempo - 1) * tasa / (1 + tasa) + cuota * ((1 + tasa) ** tiempo - tasa * tiempo - 1) / ((1 + tasa) ** tiempo - 1) / (tasa ** 2)
    return vp



def calcular_anualidades_vencidas(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / ((1 + i)**nper - 1)
    return A

# Función para calcular el valor de las anualidades anticipadas
def calcular_anualidades_anticipadas(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / ((1 + i)**nper - 1) * (1 + i)
    return A

# Función para calcular el valor de los gradientes lineales crecientes
def calcular_gradientes_lineales_crecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper - nper * (1 + i)**(nper - 1))
    return A

# Función para calcular el valor de los gradientes lineales decrecientes
def calcular_gradientes_lineales_decrecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper + nper * (1 + i)**(nper - 1))
    return A

# Función para calcular el valor de los gradientes geométricos crecientes
def calcular_gradientes_geometricos_crecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper - (1 + i)**nper + 1)
    return A

# Función para calcular el valor de los gradientes geométricos decrecientes
def calcular_gradientes_geometricos_decrecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper + (1 + i)**nper - 1)
    return A





def calcular_anualidades_vencidas(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / ((1 + i)**nper - 1)
    return A

# Función para calcular el valor de las anualidades anticipadas
def calcular_anualidades_anticipadas(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / ((1 + i)**nper - 1) * (1 + i)
    return A

# Función para calcular el valor de los gradientes lineales crecientes
def calcular_gradientes_lineales_crecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper - nper * (1 + i)**(nper - 1))
    return A

# Función para calcular el valor de los gradientes lineales decrecientes
def calcular_gradientes_lineales_decrecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper + nper * (1 + i)**(nper - 1))
    return A

# Función para calcular el valor de los gradientes geométricos crecientes
def calcular_gradientes_geometricos_crecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper - (1 + i)**nper + 1)
    return A

# Función para calcular el valor de los gradientes geométricos decrecientes
def calcular_gradientes_geometricos_decrecientes(VA, VF, i, nper):
    A = (VF - VA * (1 + i)**nper) / (i * (1 + i)**nper + (1 + i)**nper - 1)
    return A



# Función para calcular el valor de la tasa en anualidades vencidas
def calcular_tasa_anualidades_vencidas(VA, VF, A, nper):
    tasa = ((VF - VA) / (VA * nper) + 1) ** (1 / nper) - 1
    return tasa

# Función para calcular el valor de la tasa en anualidades anticipadas
def calcular_tasa_anualidades_anticipadas(VA, VF, A, nper):
    tasa = ((VF - VA * (1 + A)) / (VA * A * nper) + 1) ** (1 / nper) - 1
    return tasa

# Función para calcular el valor de la tasa en gradientes lineales crecientes
def calcular_tasa_gradientes_lineales_crecientes(VA, VF, A, nper):
    tasa = ((VF - VA * (A + 1)) / (VA * A * (A + nper)) + 1) ** (1 / nper) - 1
    return tasa

# Función para calcular el valor de la tasa en gradientes lineales decrecientes
def calcular_tasa_gradientes_lineales_decrecientes(VA, VF, A, nper):
    tasa = ((VF - VA * (A - 1)) / (VA * A * (A + nper)) + 1) ** (1 / nper) - 1
    return tasa

# Función para calcular el valor de la tasa en gradientes geométricos crecientes
def calcular_tasa_gradientes_geometricos_crecientes(VA, VF, A, nper):
    tasa = (((VF - VA * (A + 1)) / (VA * (A - nper))) + 1) ** (1 / nper) - 1
    return tasa

# Función para calcular el valor de la tasa en gradientes geométricos decrecientes
def calcular_tasa_gradientes_geometricos_decrecientes(VA, VF, A, nper):
    tasa = (((VF - VA * (A - 1)) / (VA * (A - nper))) + 1) ** (1 / nper) - 1
    return tasa


# Función para calcular el valor de nper en anualidades vencidas
def calcular_nper_anualidades_vencidas(VA, VF, A, tasa):
    nper = math.log(((VF * tasa) + A) / (A * tasa + VA * tasa + A)) / math.log(1 + tasa)
    return nper

# Función para calcular el valor de nper en anualidades anticipadas
def calcular_nper_anualidades_anticipadas(VA, VF, A, tasa):
    nper = math.log(((VF * tasa) + A - (tasa * VA)) / (A * tasa + VA * tasa + A)) / math.log(1 + tasa)
    return nper

# Función para calcular el valor de nper en gradientes lineales crecientes
def calcular_nper_gradientes_lineales_crecientes(VA, VF, A, tasa):
    nper = (A - (VF * tasa)) / (A * tasa - VA * tasa + A * tasa + VF * tasa)
    return nper

# Función para calcular el valor de nper en gradientes lineales decrecientes
def calcular_nper_gradientes_lineales_decrecientes(VA, VF, A, tasa):
    nper = (A + (VF * tasa)) / (A * tasa + VA * tasa - A * tasa + VF * tasa)
    return nper

# Función para calcular el valor de nper en gradientes geométricos crecientes
def calcular_nper_gradientes_geometricos_crecientes(VA, VF, A, tasa):
    nper = math.log((A * tasa - VF * tasa) / (A * tasa - VA * tasa + A * tasa + VF * tasa - VF)) / math.log(1 + tasa)
    return nper

# Función para calcular el valor de nper en gradientes geométricos decrecientes
def calcular_nper_gradientes_geometricos_decrecientes(VA, VF, A, tasa):
    nper = math.log((A * tasa + VF * tasa) / (A * tasa + VA * tasa - A * tasa + VF * tasa + VF)) / math.log(1 + tasa)
    return nper
def calcular_cuota_anualidades_vencidas(VA, tasa, nper):
    cuota = (VA * tasa) / (1 - (1 + tasa)**(-nper))
    return cuota

# Función para calcular la cuota enésima de Anualidades Anticipadas
def calcular_cuota_anualidades_anticipadas(VA, tasa, nper):
    cuota = (VA * tasa) / ((1 + tasa)**nper - 1)
    return cuota

# Función para calcular la cuota enésima de Gradientes Lineales Crecientes
def calcular_cuota_gradientes_lineales_crecientes(VA, tasa, nper):
    cuota = (VA * tasa * (1 + tasa)**nper) / ((1 + tasa)**nper - 1)
    return cuota

# Función para calcular la cuota enésima de Gradientes Lineales Decrecientes
def calcular_cuota_gradientes_lineales_decrecientes(VA, tasa, nper):
    cuota = (VA * tasa * (1 + tasa)**nper) / ((1 + tasa)**nper + 1)
    return cuota

# Función para calcular la cuota enésima de Gradientes Geométricos Crecientes
def calcular_cuota_gradientes_geometricos_crecientes(VA, tasa, nper):
    cuota = (VA * tasa) / ((1 + tasa)**nper - 1)
    return cuota

# Función para calcular la cuota enésima de Gradientes Geométricos Decrecientes
def calcular_cuota_gradientes_geometricos_decrecientes(VA, tasa, nper):
    cuota = (VA * tasa) / ((1 + tasa)**nper + 1)
    return cuota







def calcular_valor_final():
    try:
        cuota = float(entrada_cuota.get())
        tasa = float(entrada_tasa.get())
        tiempo = float(entrada_tiempo.get())

        unidad_tasa_val = unidad_tasa.get()
        unidad_tiempo_val = unidad_tiempo.get()

        # Convertir la tasa según la unidad seleccionada
        if unidad_tasa_val == 2:  # Si la unidad es semestral
            tasa /= 2
        # Convertir el tiempo según la unidad seleccionada
        if unidad_tiempo_val == 3:  # Si la unidad es trimestral
            tiempo *= 4
        elif unidad_tiempo_val == 4:  # Si la unidad es mensual
            tiempo *= 12

        vf = 0

        if tipo_calculo.get() == 1:  # Anualidades vencidas
            vf = calcular_vf_anualidades_vencidas(cuota, tasa, tiempo)
        elif tipo_calculo.get() == 2:  # Anualidades anticipadas
            vf = calcular_vf_anualidades_anticipadas(cuota, tasa, tiempo)
        elif tipo_calculo.get() == 3:  # Gradientes lineales crecientes
            vf = calcular_vf_gradiente_lineal_creciente(cuota, tasa, tiempo)
        elif tipo_calculo.get() == 4:  # Gradientes lineales decrecientes
            vf = calcular_vf_gradiente_lineal_decreciente(cuota, tasa, tiempo)
        elif tipo_calculo.get() == 5:  # Gradientes geométricos crecientes
            vf = calcular_vf_gradiente_geometrico_creciente(cuota, tasa, tiempo)
        elif tipo_calculo.get() == 6:  # Gradientes geométricos decrecientes
            vf = calcular_vf_gradiente_geometrico_decreciente(cuota, tasa, tiempo)
        else:
            resultado_valor_final.set("Error: Tipo de cálculo inválido")

        resultado_valor_final.set(vf)

    except ValueError:
        resultado_valor_final.set("Error: Ingresa valores numéricos válidos")


def calcular_valor_presente():
    try:
        vf = float(entrada_vf.get())
        cuota = float(entrada_cuota.get())
        tasa = float(entrada_tasa.get())
        tiempo = float(entrada_tiempo.get())

        unidad_tasa_val = unidad_tasa.get()
        unidad_tiempo_val = unidad_tiempo.get()

        # Convertir la tasa según la unidad seleccionada
        if unidad_tasa_val == 2:  # Si la unidad es semestral
            tasa /= 2
        # Convertir el tiempo según la unidad seleccionada
        if unidad_tiempo_val == 3:  # Si la unidad es trimestral
            tiempo *= 4
        elif unidad_tiempo_val == 4:  # Si la unidad es mensual
            tiempo *= 12

        vp = 0

        tipo_calculo_val = tipo_calculo.current() + 1  # Obtener el índice seleccionado y sumar 1 para obtener el tipo de cálculo correspondiente

        if tipo_calculo_val == 1:  # Anualidades vencidas
            vp = calcular_vp_anualidades_vencidas(vf, cuota, tasa, tiempo)
        elif tipo_calculo_val == 2:  # Anualidades anticipadas
            vp = calcular_vp_anualidades_anticipadas(vf, cuota, tasa, tiempo)
        elif tipo_calculo_val == 3:  # Gradientes lineales crecientes
            vp = calcular_vp_gradiente_lineal_creciente(vf, cuota, tasa, tiempo)
        elif tipo_calculo_val == 4:  # Gradientes lineales decrecientes
            vp = calcular_vp_gradiente_lineal_decreciente(vf, cuota, tasa, tiempo)
        elif tipo_calculo_val == 5:  # Gradientes geométricos crecientes
            vp = calcular_vp_gradiente_geometrico_creciente(vf, cuota, tasa, tiempo)
        elif tipo_calculo_val == 6:  # Gradientes geométricos decrecientes
            vp = calcular_vp_gradiente_geometrico_decreciente(vf, cuota, tasa, tiempo)
        else:
            resultado_valor_presente.set("Error: Tipo de cálculo inválido")

        resultado_valor_presente.set(vp)

    except ValueError:
        resultado_valor_presente.set("Error: Ingresa valores numéricos válidos")



def calcular_A():
    try:
        VA = float(entrada_va.get())
        VF = float(entrada_vf.get())
        i = float(entrada_i.get())
        nper = float(entrada_nper.get())

        tipo_calculo_val = tipo_calculo.current()

        if tipo_calculo_val == 0:  # Anualidades vencidas
            A = calcular_anualidades_vencidas(VA, VF, i, nper)
        elif tipo_calculo_val == 1:  # Anualidades anticipadas
            A = calcular_anualidades_anticipadas(VA, VF, i, nper)
        elif tipo_calculo_val == 2:  # Gradientes lineales crecientes
            A = calcular_gradientes_lineales_crecientes(VA, VF, i, nper)
        elif tipo_calculo_val == 3:  # Gradientes lineales decrecientes
            A = calcular_gradientes_lineales_decrecientes(VA, VF, i, nper)
        elif tipo_calculo_val == 4:  # Gradientes geométricos crecientes
            A = calcular_gradientes_geometricos_crecientes(VA, VF, i, nper)
        elif tipo_calculo_val == 5:  # Gradientes geométricos decrecientes
            A = calcular_gradientes_geometricos_decrecientes(VA, VF, i, nper)
        else:
            resultado_A.set("Error: Tipo de cálculo inválido")

        resultado_A.set(A)

    except ValueError:
        resultado_A.set("Error: Ingresa valores numéricos válidos")



def calcular_tasa():
    try:
        VA = float(entrada_va.get())
        VF = float(entrada_vf.get())
        A = float(entrada_a.get())
        nper = float(entrada_nper.get())

        tipo_calculo_val = tipo_calculo.current()

        if tipo_calculo_val == 0:  # Anualidades vencidas
            tasa = calcular_tasa_anualidades_vencidas(VA, VF, A, nper)
        elif tipo_calculo_val == 1:  # Anualidades anticipadas
            tasa = calcular_tasa_anualidades_anticipadas(VA, VF, A, nper)
        elif tipo_calculo_val == 2:  # Gradientes lineales crecientes
            tasa = calcular_tasa_gradientes_lineales_crecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 3:  # Gradientes lineales decrecientes
            tasa = calcular_tasa_gradientes_lineales_decrecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 4:  # Gradientes geométricos crecientes
            tasa = calcular_tasa_gradientes_geometricos_crecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 5:  # Gradientes geométricos decrecientes
            tasa = calcular_tasa_gradientes_geometricos_decrecientes(VA, VF, A, nper)
        else:
            resultado_tasa.set("Error: Tipo de cálculo inválido")

        resultado_tasa.set(tasa)

    except ValueError:
        resultado_tasa.set("Error: Ingresa valores numéricos válidos")



def calcular_tasa():
    try:
        VA = float(entrada_va.get())
        VF = float(entrada_vf.get())
        A = float(entrada_a.get())
        nper = float(entrada_nper.get())

        tipo_calculo_val = tipo_calculo.current()

        if tipo_calculo_val == 0:  # Anualidades vencidas
            tasa = calcular_tasa_anualidades_vencidas(VA, VF, A, nper)
        elif tipo_calculo_val == 1:  # Anualidades anticipadas
            tasa = calcular_tasa_anualidades_anticipadas(VA, VF, A, nper)
        elif tipo_calculo_val == 2:  # Gradientes lineales crecientes
            tasa = calcular_tasa_gradientes_lineales_crecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 3:  # Gradientes lineales decrecientes
            tasa = calcular_tasa_gradientes_lineales_decrecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 4:  # Gradientes geométricos crecientes
            tasa = calcular_tasa_gradientes_geometricos_crecientes(VA, VF, A, nper)
        elif tipo_calculo_val == 5:  # Gradientes geométricos decrecientes
            tasa = calcular_tasa_gradientes_geometricos_decrecientes(VA, VF, A, nper)
        else:
            resultado_tasa.set("Error: Tipo de cálculo inválido")

        resultado_tasa.set(tasa)

    except ValueError:
        resultado_tasa.set("Error: Ingresa valores numéricos válidos")

def calcular_nper():
    try:
        VA = float(entrada_va.get())
        VF = float(entrada_vf.get())
        A = float(entrada_a.get())
        tasa = float(entrada_tasa.get())

        tipo_calculo_val = tipo_calculo.current()

        if tipo_calculo_val == 0:  # Anualidades vencidas
            nper = calcular_nper_anualidades_vencidas(VA, VF, A, tasa)
        elif tipo_calculo_val == 1:  # Anualidades anticipadas
            nper = calcular_nper_anualidades_anticipadas(VA, VF, A, tasa)
        elif tipo_calculo_val == 2:  # Gradientes lineales crecientes
            nper = calcular_nper_gradientes_lineales_crecientes(VA, VF, A, tasa)
        elif tipo_calculo_val == 3:  # Gradientes lineales decrecientes
            nper = calcular_nper_gradientes_lineales_decrecientes(VA, VF, A, tasa)
        elif tipo_calculo_val == 4:  # Gradientes geométricos crecientes
            nper = calcular_nper_gradientes_geometricos_crecientes(VA, VF, A, tasa)
        elif tipo_calculo_val == 5:  # Gradientes geométricos decrecientes
            nper = calcular_nper_gradientes_geometricos_decrecientes(VA, VF, A, tasa)
        else:
            resultado_nper.set("Error: Tipo de cálculo inválido")

        resultado_nper.set(nper)

    except ValueError:
        resultado_nper.set("Error: Ingresa valores numéricos válidos")

def calcular_cuota():
    try:
        VA = float(entrada_va.get())
        VF = float(entrada_vf.get())
        tasa = float(entrada_tasa.get())
        nper = float(entrada_nper.get())

        tipo_calculo_val = tipo_calculo.current()

        if tipo_calculo_val == 0:  # Anualidades vencidas
            cuota = calcular_cuota_anualidades_vencidas(VA, tasa, nper)
        elif tipo_calculo_val == 1:  # Anualidades anticipadas
            cuota = calcular_cuota_anualidades_anticipadas(VA, tasa, nper)
        elif tipo_calculo_val == 2:  # Gradientes lineales crecientes
            cuota = calcular_cuota_gradientes_lineales_crecientes(VA, tasa, nper)
        elif tipo_calculo_val == 3:  # Gradientes lineales decrecientes
            cuota = calcular_cuota_gradientes_lineales_decrecientes(VA, tasa, nper)
        elif tipo_calculo_val == 4:  # Gradientes geométricos crecientes
            cuota = calcular_cuota_gradientes_geometricos_crecientes(VA, tasa, nper)
        elif tipo_calculo_val == 5:  # Gradientes geométricos decrecientes
            cuota = calcular_cuota_gradientes_geometricos_decrecientes(VA, tasa, nper)
        else:
            resultado_cuota.set("Error: Tipo de cálculo inválido")

        resultado_cuota.set(cuota)

    except ValueError:
        resultado_cuota.set("Error: Ingresa valores numéricos válidos")

ventana = Tk()
ventana.title("Proyecto Final")
ventana.geometry("800x600")


notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True)

# Variables para interes compuesto globales
resultado_valor_final = DoubleVar()
txt_resultado_valor_final = StringVar()
unidad_tasa = IntVar()
unidad_tiempo = IntVar()

# Frame del cálculo de valor final

frame_valor_final = Frame(notebook)
frame_valor_final.pack(fill="both", expand=True)

label_vf = Label(frame_valor_final, text="Valor Final:")
label_vf.pack()
entrada_vf = Entry(frame_valor_final)
entrada_vf.pack()

label_cuota = Label(frame_valor_final, text="Cuota:")
label_cuota.pack()
entrada_cuota = Entry(frame_valor_final)
entrada_cuota.pack()

label_tasa = Label(frame_valor_final, text="Tasa de Interés:")
label_tasa.pack()
entrada_tasa = Entry(frame_valor_final)
entrada_tasa.pack()

label_tiempo = Label(frame_valor_final, text="Tiempo:")
label_tiempo.pack()
entrada_tiempo = Entry(frame_valor_final)
entrada_tiempo.pack()

unidad_tasa = IntVar()
label_unidad_tasa = Label(frame_valor_final, text="Unidad de Tasa:")
label_unidad_tasa.pack()

radio_anual = Radiobutton(frame_valor_final, text="Anual", variable=unidad_tasa, value=1)
radio_anual.pack()

radio_semestral = Radiobutton(frame_valor_final, text="Semestral", variable=unidad_tasa, value=2)
radio_semestral.pack()

unidad_tiempo = IntVar()
label_unidad_tiempo = Label(frame_valor_final, text="Unidad de Tiempo:")
label_unidad_tiempo.pack()

radio_anios = Radiobutton(frame_valor_final, text="Años", variable=unidad_tiempo, value=1)
radio_anios.pack()

radio_semestres = Radiobutton(frame_valor_final, text="Semestres", variable=unidad_tiempo, value=2)
radio_semestres.pack()

radio_trimestres = Radiobutton(frame_valor_final, text="Trimestres", variable=unidad_tiempo, value=3)
radio_trimestres.pack()

radio_meses = Radiobutton(frame_valor_final, text="Meses", variable=unidad_tiempo, value=4)
radio_meses.pack()

tipo_calculo = IntVar()
label_tipo_calculo = Label(frame_valor_final, text="Tipo de Cálculo:")
label_tipo_calculo.pack()

radio_anualidades_vencidas = Radiobutton(frame_valor_final, text="Anualidades Vencidas", variable=tipo_calculo, value=1)
radio_anualidades_vencidas.pack()

radio_anualidades_anticipadas = Radiobutton(frame_valor_final, text="Anualidades Anticipadas", variable=tipo_calculo, value=2)
radio_anualidades_anticipadas.pack()

radio_gradiente_lineal_creciente = Radiobutton(frame_valor_final, text="Gradiente Lineal Creciente", variable=tipo_calculo, value=3)
radio_gradiente_lineal_creciente.pack()

radio_gradiente_lineal_decreciente = Radiobutton(frame_valor_final, text="Gradiente Lineal Decreciente", variable=tipo_calculo, value=4)
radio_gradiente_lineal_decreciente.pack()

radio_gradiente_geometrico_creciente = Radiobutton(frame_valor_final, text="Gradiente Geométrico Creciente", variable=tipo_calculo, value=5)
radio_gradiente_geometrico_creciente.pack()

radio_gradiente_geometrico_decreciente = Radiobutton(frame_valor_final, text="Gradiente Geométrico Decreciente", variable=tipo_calculo, value=6)
radio_gradiente_geometrico_decreciente.pack()

boton_calcular = Button(frame_valor_final, text="Calcular", command=calcular_valor_final)
boton_calcular.pack()

resultado_valor_final = DoubleVar()
label_resultado_valor_final = Label(frame_valor_final, textvariable=resultado_valor_final)
label_resultado_valor_final.pack()

notebook.add(frame_valor_final, text="Valor Final")

#Valor Present


frame_valor_presente = ttk.Frame(notebook)
frame_valor_presente.pack(fill="both", expand=True)

# Agregar el frame al notebook
notebook.add(frame_valor_presente, text="Valor Presente")

# Crear los elementos y widgets necesarios dentro del frame

# Etiqueta y campo de texto para el valor futuro
label_vf = ttk.Label(frame_valor_presente, text="Valor Futuro:")
label_vf.pack()
entrada_vf = ttk.Entry(frame_valor_presente)
entrada_vf.pack()

# Etiqueta y campo de texto para la cuota
label_cuota = ttk.Label(frame_valor_presente, text="Cuota:")
label_cuota.pack()
entrada_cuota = ttk.Entry(frame_valor_presente)
entrada_cuota.pack()

# Etiqueta y campo de texto para la tasa
label_tasa = ttk.Label(frame_valor_presente, text="Tasa:")
label_tasa.pack()
entrada_tasa = ttk.Entry(frame_valor_presente)
entrada_tasa.pack()

# Etiqueta y campo de texto para el tiempo
label_tiempo = ttk.Label(frame_valor_presente, text="Tiempo:")
label_tiempo.pack()
entrada_tiempo = ttk.Entry(frame_valor_presente)
entrada_tiempo.pack()

# Opciones de selección para la unidad de tasa
label_unidad_tasa = ttk.Label(frame_valor_presente, text="Unidad de Tasa:")
label_unidad_tasa.pack()
unidad_tasa = ttk.Combobox(frame_valor_presente, values=["Anual", "Semestral"])
unidad_tasa.pack()

# Opciones de selección para la unidad de tiempo
label_unidad_tiempo = ttk.Label(frame_valor_presente, text="Unidad de Tiempo:")
label_unidad_tiempo.pack()
unidad_tiempo = ttk.Combobox(frame_valor_presente, values=["Anual", "Trimestral", "Mensual"])
unidad_tiempo.pack()

# Opciones de selección para el tipo de cálculo
label_tipo_calculo = ttk.Label(frame_valor_presente, text="Tipo de Cálculo:")
label_tipo_calculo.pack()
tipo_calculo = ttk.Combobox(frame_valor_presente, values=["Anualidades vencidas", "Anualidades anticipadas", "Gradientes lineales crecientes", "Gradientes lineales decrecientes", "Gradientes geométricos crecientes", "Gradientes geométricos decrecientes"])
tipo_calculo.pack()

# Resultado del cálculo del valor presente
resultado_valor_presente = tk.StringVar()
label_resultado = ttk.Label(frame_valor_presente, text="Valor Presente:")
label_resultado.pack()
label_valor_presente = ttk.Label(frame_valor_presente, textvariable=resultado_valor_presente)
label_valor_presente.pack()

boton_calcular = ttk.Button(frame_valor_presente, text="Calcular", command=calcular_valor_presente)
boton_calcular.pack()


#Para A


frame_calculo_A = ttk.Frame(notebook)
frame_calculo_A.pack(fill="both", expand=True)

label_va = ttk.Label(frame_calculo_A, text="VA:")
label_va.pack()
entrada_va = ttk.Entry(frame_calculo_A)
entrada_va.pack()

label_vf = ttk.Label(frame_calculo_A, text="VF:")
label_vf.pack()
entrada_vf = ttk.Entry(frame_calculo_A)
entrada_vf.pack()

label_i = ttk.Label(frame_calculo_A, text="i:")
label_i.pack()
entrada_i = ttk.Entry(frame_calculo_A)
entrada_i.pack()

label_nper = ttk.Label(frame_calculo_A, text="nper:")
label_nper.pack()
entrada_nper = ttk.Entry(frame_calculo_A)
entrada_nper.pack()

label_tipo_calculo = ttk.Label(frame_calculo_A, text="Tipo de Cálculo:")
label_tipo_calculo.pack()
tipo_calculo = ttk.Combobox(frame_calculo_A, values=["Anualidades vencidas", "Anualidades anticipadas", "Gradientes lineales crecientes", "Gradientes lineales decrecientes", "Gradientes geométricos crecientes", "Gradientes geométricos decrecientes"])
tipo_calculo.pack()

boton_calcular = ttk.Button(frame_calculo_A, text="Calcular", command=calcular_A)
boton_calcular.pack()

resultado_A = tk.StringVar()
label_resultado_A = ttk.Label(frame_calculo_A, textvariable=resultado_A)
label_resultado_A.pack()

notebook.add(frame_calculo_A, text="Calcular A")


#Para I 


frame_calculo_tasa = ttk.Frame(notebook)
frame_calculo_tasa.pack(fill="both", expand=True)

label_va = ttk.Label(frame_calculo_tasa, text="VA:")
label_va.pack()
entrada_va = ttk.Entry(frame_calculo_tasa)
entrada_va.pack()

label_vf = ttk.Label(frame_calculo_tasa, text="VF:")
label_vf.pack()
entrada_vf = ttk.Entry(frame_calculo_tasa)
entrada_vf.pack()

label_a = ttk.Label(frame_calculo_tasa, text="A:")
label_a.pack()
entrada_a = ttk.Entry(frame_calculo_tasa)
entrada_a.pack()

label_nper = ttk.Label(frame_calculo_tasa, text="nper:")
label_nper.pack()
entrada_nper = ttk.Entry(frame_calculo_tasa)
entrada_nper.pack()

label_tipo_calculo = ttk.Label(frame_calculo_tasa, text="Tipo de Cálculo:")
label_tipo_calculo.pack()
tipo_calculo = ttk.Combobox(frame_calculo_tasa, values=["Anualidades vencidas", "Anualidades anticipadas", "Gradientes lineales crecientes", "Gradientes lineales decrecientes", "Gradientes geométricos crecientes", "Gradientes geométricos decrecientes"])
tipo_calculo.pack()

boton_calcular = ttk.Button(frame_calculo_tasa, text="Calcular", command=calcular_tasa)
boton_calcular.pack()

resultado_tasa = tk.StringVar()
label_resultado_tasa = ttk.Label(frame_calculo_tasa, textvariable=resultado_tasa)
label_resultado_tasa.pack()

notebook.add(frame_calculo_tasa, text="Calcular Tasa")



#Calcular Nper 

frame_numero_periodos = ttk.Frame(notebook)
frame_numero_periodos.pack()

# Crear los elementos del marco "frame_numero_periodos"
label_va = ttk.Label(frame_numero_periodos, text="Valor Actual (VA):")
label_va.grid(column=0, row=0, padx=5, pady=5)
entrada_va = ttk.Entry(frame_numero_periodos)
entrada_va.grid(column=1, row=0, padx=5, pady=5)

label_vf = ttk.Label(frame_numero_periodos, text="Valor Futuro (VF):")
label_vf.grid(column=0, row=1, padx=5, pady=5)
entrada_vf = ttk.Entry(frame_numero_periodos)
entrada_vf.grid(column=1, row=1, padx=5, pady=5)

label_a = ttk.Label(frame_numero_periodos, text="Anualidad (A):")
label_a.grid(column=0, row=2, padx=5, pady=5)
entrada_a = ttk.Entry(frame_numero_periodos)
entrada_a.grid(column=1, row=2, padx=5, pady=5)

label_tasa = ttk.Label(frame_numero_periodos, text="Tasa:")
label_tasa.grid(column=0, row=3, padx=5, pady=5)
entrada_tasa = ttk.Entry(frame_numero_periodos)
entrada_tasa.grid(column=1, row=3, padx=5, pady=5)

boton_calcular_nper = ttk.Button(frame_numero_periodos, text="Calcular", command=calcular_nper)
boton_calcular_nper.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

label_resultado_nper = ttk.Label(frame_numero_periodos, text="Número de períodos:")
label_resultado_nper.grid(column=0, row=5, padx=5, pady=5)
resultado_nper = tk.StringVar()
resultado_nper_label = ttk.Label(frame_numero_periodos, textvariable=resultado_nper)
resultado_nper_label.grid(column=1, row=5, padx=5, pady=5)

# Agregar el marco "frame_numero_periodos" al notebook
notebook.add(frame_numero_periodos, text="Número de Períodos")

#Couta enesima 



# Frame para el cálculo de cuotas
frame_cuotas = ttk.Frame(notebook)
frame_cuotas.pack()

# Etiquetas y entradas de texto
label_va = ttk.Label(frame_cuotas, text="Valor Actual (VA):")
label_va.grid(row=0, column=0, padx=5, pady=5)
entrada_va = ttk.Entry(frame_cuotas)
entrada_va.grid(row=0, column=1, padx=5, pady=5)

label_tasa = ttk.Label(frame_cuotas, text="Tasa de Interés (%):")
label_tasa.grid(row=1, column=0, padx=5, pady=5)
entrada_tasa = ttk.Entry(frame_cuotas)
entrada_tasa.grid(row=1, column=1, padx=5, pady=5)

label_nper = ttk.Label(frame_cuotas, text="Número de Períodos (n):")
label_nper.grid(row=2, column=0, padx=5, pady=5)
entrada_nper = ttk.Entry(frame_cuotas)
entrada_nper.grid(row=2, column=1, padx=5, pady=5)

label_resultado = ttk.Label(frame_cuotas, text="Resultado:")
label_resultado.grid(row=3, column=0, padx=5, pady=5)
resultado_cuota = tk.StringVar()
etiqueta_resultado = ttk.Label(frame_cuotas, textvariable=resultado_cuota)
etiqueta_resultado.grid(row=3, column=1, padx=5, pady=5)

# Botón para calcular la cuota enésima
boton_calcular = ttk.Button(frame_cuotas, text="Calcular", command=calcular_cuota)
boton_calcular.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# Añadir el frame de cuotas al notebook
notebook.add(frame_cuotas, text="Cálculo de Cuotas")











# Variables para el conversor
monto = DoubleVar()
tasa_conversor = DoubleVar()
periodo = DoubleVar()
resultado = DoubleVar()
txt_resultado = StringVar()

def convertir():
    try:
        resultado.set(con.convertir_interes_compuesto(monto.get(), tasa_conversor.get(), periodo.get()))
        txt_resultado.set(f"El resultado es: {resultado.get()}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

frame_conversor = Frame(notebook)

label_monto = Label(frame_conversor, text="Monto:")
label_monto.pack()
entrada_monto = Entry(frame_conversor, textvariable=monto)
entrada_monto.pack()

label_tasa_conversor = Label(frame_conversor, text="Tasa de interés:")
label_tasa_conversor.pack()
entrada_tasa_conversor = Entry(frame_conversor, textvariable=tasa_conversor)
entrada_tasa_conversor.pack()

label_periodo = Label(frame_conversor, text="Período:")
label_periodo.pack()
entrada_periodo = Entry(frame_conversor, textvariable=periodo)
entrada_periodo.pack()

boton_convertir = Button(frame_conversor, text="Convertir", command=convertir)
boton_convertir.pack()

label_resultado = Label(frame_conversor, textvariable=txt_resultado)
label_resultado.pack()

notebook.add(frame_conversor, text="Conversor")

# Frame de simulación de amortización
frame_amortizacion = Frame(notebook)
frame_amortizacion.pack(fill="both", expand=True)

label_principal = Label(frame_amortizacion, text="Monto del préstamo:")
label_principal.pack()
entrada_principal = Entry(frame_amortizacion)
entrada_principal.pack()

label_tasa_interes = Label(frame_amortizacion, text="Tasa de interés (%):")
label_tasa_interes.pack()
entrada_tasa_interes = Entry(frame_amortizacion)
entrada_tasa_interes.pack()

label_plazo = Label(frame_amortizacion, text="Plazo (meses):")
label_plazo.pack()
entrada_plazo = Entry(frame_amortizacion)
entrada_plazo.pack()

opcion_amortizacion = StringVar()
opcion_amortizacion.set("cuota_fija_con_cuotas_extraordinarias")  # Valor predeterminado

radio_cuota_fija_extraordinarias = Radiobutton(frame_amortizacion, text="Cuota Fija con Cuotas Extraordinarias",
                                              variable=opcion_amortizacion, value="cuota_fija_con_cuotas_extraordinarias")
radio_cuota_fija_extraordinarias.pack()

radio_cuota_fija_gracia = Radiobutton(frame_amortizacion, text="Cuota Fija con Período de Gracia",
                                      variable=opcion_amortizacion, value="cuota_fija_con_periodo_gracia")
radio_cuota_fija_gracia.pack()

radio_cuota_creciente_lineal = Radiobutton(frame_amortizacion, text="Cuota Creciente Lineal",
                                           variable=opcion_amortizacion, value="cuota_creciente_lineal")
radio_cuota_creciente_lineal.pack()

radio_cuota_creciente_exponencial = Radiobutton(frame_amortizacion, text="Cuota Creciente Exponencial",
                                                variable=opcion_amortizacion, value="cuota_creciente_exponencial")
radio_cuota_creciente_exponencial.pack()

boton_calcular_amortizacion = Button(frame_amortizacion, text="Calcular Amortización",
                                     command=lambda: calcular_amortizacion(opcion_amortizacion.get()))
boton_calcular_amortizacion.pack()

resultado_amortizacion = Text(frame_amortizacion, height=10)
resultado_amortizacion.pack()


notebook.add(frame_amortizacion, text="Simulación Amortización")

# Frame de evaluación financiera
frame_evaluacion_financiera = Frame(notebook)
frame_evaluacion_financiera.pack(fill="both", expand=True)

label_inversion = Label(frame_evaluacion_financiera, text="Inversión:")
label_inversion.pack()
entrada_inversion = Entry(frame_evaluacion_financiera)
entrada_inversion.pack()

label_flujos = Label(frame_evaluacion_financiera, text="Flujos de efectivo:")
label_flujos.pack()
entrada_flujos = Entry(frame_evaluacion_financiera)
entrada_flujos.pack()

label_tasa_descuento = Label(frame_evaluacion_financiera, text="Tasa de descuento:")
label_tasa_descuento.pack()

entrada_tasa_descuento = Entry(frame_evaluacion_financiera)
entrada_tasa_descuento.pack()

label_periodo = Label(frame_evaluacion_financiera, text="Período:")
label_periodo.pack()
entrada_periodo = Entry(frame_evaluacion_financiera)
entrada_periodo.pack()

# Función para calcular el Valor Presente Neto (VPN)
def calcular_vpn():
    try:
        inversion = float(entrada_inversion.get())
        flujos_str = entrada_flujos.get()

        flujos = [float(f) for f in flujos_str.split(',')]
        tasa_descuento = float(entrada_tasa_descuento.get())
        periodo = int(entrada_periodo.get())

        vpn = npf.npv(tasa_descuento, flujos)
        vpn = round(vpn, 2)

        if vpn > inversion:
            mensaje = f"El VPN es {vpn}. El proyecto es rentable."
        elif vpn < inversion:
            mensaje = f"El VPN es {vpn}. El proyecto no es rentable."
        else:
            mensaje = f"El VPN es {vpn}. El proyecto es indiferente."

        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Botón para calcular el VPN
boton_calcular_vpn = Button(frame_evaluacion_financiera, text="Calcular VPN", command=calcular_vpn)
boton_calcular_vpn.pack()

notebook.add(frame_evaluacion_financiera, text="Evaluación Financiera")

ventana.mainloop()
