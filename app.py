from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import interes_compuesto as icom
import conversor as con
import numpy as np
import numpy_financial as npf

def calcular_amortizacion():
    try:
        monto_prestamo = float(entrada_principal.get())
        tasa_interes = float(entrada_tasa_interes.get())
        plazo_meses = int(entrada_plazo.get())

        tasa_interes_decimal = tasa_interes / 100
        cuota_mensual = monto_prestamo * (tasa_interes_decimal / 12) / (1 - (1 + tasa_interes_decimal / 12) ** -plazo_meses)

        resultado_amortizacion.delete(1.0, END)

        for mes in range(1, plazo_meses + 1):
            interes_mensual = monto_prestamo * tasa_interes_decimal / 12
            amortizacion_mensual = cuota_mensual - interes_mensual
            monto_prestamo -= amortizacion_mensual

            resultado_amortizacion.insert(END, f"Mes {mes}: Cuota: {cuota_mensual:.2f} - "
                                               f"Interés: {interes_mensual:.2f} - "
                                               f"Amortización: {amortizacion_mensual:.2f} - "
                                               f"Saldo Restante: {monto_prestamo:.2f}\n")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def calcular_valor_final():
    try:
        vp = float(entrada_vp.get())
        tasa = float(entrada_tasa.get())
        tiempo = float(entrada_tiempo.get())

        if unidad_tasa.get() == 2:
            tasa = con.convertir_tasa_semestral(tasa)

        if unidad_tiempo.get() == 2:
            tiempo = con.convertir_semestres_a_anios(tiempo)
        elif unidad_tiempo.get() == 3:
            tiempo = con.convertir_trimestes_a_anios(tiempo)
        elif unidad_tiempo.get() == 4:
            tiempo = con.convertir_meses_a_anios(tiempo)

        vf = icom.calcular_vf(vp, tasa, tiempo)
        resultado_valor_final.set(round(vf, 3))
        txt_resultado_valor_final.set(f"El valor final es {round(resultado_valor_final.get(), 3)}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def toggle_dark_mode():
    current_theme = ventana.tk.call("ttk::style", "theme", "use")
    new_theme = "alt" if current_theme == "default" else "default"
    ventana.tk.call("ttk::style", "theme", new_theme)


ventana = Tk()
ventana.title("Proyecto Final")
ventana.geometry("800x600")

# Modo oscuro
toggle_button = Button(ventana, text="Toggle Dark Mode", command=toggle_dark_mode)
toggle_button.pack(pady=10)


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

label_vp = Label(frame_valor_final, text="Valor Presente:")
label_vp.pack()
entrada_vp = Entry(frame_valor_final)
entrada_vp.pack()

label_tasa = Label(frame_valor_final, text="Tasa de Interés:")
label_tasa.pack()
entrada_tasa = Entry(frame_valor_final)
entrada_tasa.pack()

label_tiempo = Label(frame_valor_final, text="Tiempo:")
label_tiempo.pack()
entrada_tiempo = Entry(frame_valor_final)
entrada_tiempo.pack()

label_unidad_tasa = Label(frame_valor_final, text="Unidad de Tasa:")
label_unidad_tasa.pack()

radio_tasa_anual = Radiobutton(frame_valor_final, text="Anual", variable=unidad_tasa, value=1)
radio_tasa_anual.pack()

radio_tasa_semestral = Radiobutton(frame_valor_final, text="Semestral", variable=unidad_tasa, value=2)
radio_tasa_semestral.pack()

label_unidad_tiempo = Label(frame_valor_final, text="Unidad de Tiempo:")
label_unidad_tiempo.pack()

radio_tiempo_anios = Radiobutton(frame_valor_final, text="Años", variable=unidad_tiempo, value=1)
radio_tiempo_anios.pack()

radio_tiempo_semestres = Radiobutton(frame_valor_final, text="Semestres", variable=unidad_tiempo, value=2)
radio_tiempo_semestres.pack()

radio_tiempo_trimestres = Radiobutton(frame_valor_final, text="Trimestres", variable=unidad_tiempo, value=3)
radio_tiempo_trimestres.pack()

radio_tiempo_meses = Radiobutton(frame_valor_final, text="Meses", variable=unidad_tiempo, value=4)
radio_tiempo_meses.pack()

boton_calcular = Button(frame_valor_final, text="Calcular", command=calcular_valor_final)
boton_calcular.pack()

label_resultado_valor_final = Label(frame_valor_final, textvariable=txt_resultado_valor_final)
label_resultado_valor_final.pack()

notebook.add(frame_valor_final, text="Valor Final")

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

boton_calcular_amortizacion = Button(frame_amortizacion, text="Calcular Amortización", command=calcular_amortizacion)
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
