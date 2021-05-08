from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Calculadora cientifica")
root.configure(background = "white")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.actual = ""
        self.input_valor = True
        self.check_suma = False
        self.op = ""
        self.resultado = False

    def ingresando_numero(self, num):
        self.resultado = False
        primer_numero = vistaTexto.get()
        segundo_numero = str(num)
        if self.input_valor:
            self.actual = segundo_numero
            self.input_valor = False
        else:
            if segundo_numero == ".":
                if segundo_numero in primer_numero:
                    return
            self.actual = primer_numero + segundo_numero
        self.vista(self.actual)

    def valor_total(self):
        self.resultado = True
        self.actual = float(self.actual)
        if self.check_suma == True:
            self.validar()
        else:
            self.total = float(vistaTexto.get())
    def vista(self, valor):
        vistaTexto.delete(0, END)
        vistaTexto.insert(0, valor)

    def validar(self):
        if self.op == "Suma":
            self.total  += self.actual
        if self.op == "Resta":
            self.total -= self.actual
        if self.op == "Multiplicacion":
            self.total *= self.actual
        if self.op == "Division":
            self.total /= self.actual
        if self.op == "Mod":
            self.total %= self.actual
        self.input_valor = True
        self.check_suma = False
        self.vista(self.total)

    def operacion(self, op):
        self.actual = float(self.actual)
        if self.check_suma:
            self.validar()
        elif not self.resultado:
            self.total = self.actual
            self.input_valor = True
        self.check_suma = True
        self.op = op
        self.resultado = False

    def limpiar_entrada(self):
        self.resultado = False
        self.actual = "0"
        self.vista(0)
        self.input_valor = True

    def limpiar_todo(self):
        self.limpiar_entrada()
        self.total = 0

    def pi(self):
        self.resultado = False
        self.actual = math.pi
        self.vista(self.actual)

    def tau(self):
        self.resultado = False
        self.actual = math.tau
        self.vista(self.actual)

    def e(self):
        self.resultado = False
        self.actual = math.e
        self.vista(self.actual)

    def math_PM(self):
        self.resultado = False
        self.actual = -(float(vistaTexto.get()))
        self.vista(self.actual)

    def raiz_cuadrada(self):
        self.resultado = False
        self.actual = math.sqrt (float(vistaTexto.get()))
        self.vista(self.actual)

    def coseno(self):
        self.resultado = False
        self.actual = math.cos(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def coseno_h(self):
        self.resultado = False
        self.actual = math.cosh(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def tangente(self):
        self.resultado = False
        self.actual = math.tan(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def tangente_h(self):
        self.resultado = False
        self.actual = math.tanh(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def seno(self):
        self.resultado = False
        self.actual = math.sin(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def seno_h(self):
        self.resultado = False
        self.actual = math.sinh(math.radians(float(vistaTexto.get())))
        self.vista(self.actual)

    def log(self):
        self.resultado = False
        self.actual = math.log(float(vistaTexto.get()))
        self.vista(self.actual)

    def exp(self):
        self.resultado = False
        self.actual = math.exp(float(vistaTexto.get()))
        self.vista(self.actual)

    def acosh(self):
        self.resultado = False
        self.actual = math.acosh(float(vistaTexto.get()))
        self.vista(self.actual)

    def asinh(self):
        self.resultado = False
        self.actual = math.asinh(float(vistaTexto.get()))
        self.vista(self.actual)

    def expm1(self):
        self.resultado = False
        self.actual = math.expm1(float(vistaTexto.get()))
        self.vista(self.actual)

    def lgamma(self):
        self.resultado = False
        self.actual = math.lgamma(float(vistaTexto.get()))
        self.vista(self.actual)

    def degrees(self):
        self.resultado = False
        self.actual = math.degrees(float(vistaTexto.get()))
        self.vista(self.actual)

    def log2(self):
        self.resultado = False
        self.actual = math.log2(float(vistaTexto.get()))
        self.vista(self.actual)

    def log10(self):
        self.resultado = False
        self.actual = math.log10(float(vistaTexto.get()))
        self.vista(self.actual)

    def log1p(self):
        self.resultado = False
        self.actual = math.log1p(float(vistaTexto.get()))
        self.vista(self.actual)


valor_agregado = Calc()

vistaTexto = Entry(calc, font = ('Kozuka Mincho Pr6N',20,'bold'), bg = "white", bd = 30, width = 28, justify = RIGHT)
vistaTexto.grid(row = 0, column = 0, columnspan = 4, pady = 1)
vistaTexto.insert(0,"0")

teclas_numericas = "789456123"
i = 0
boton = []
for j in range(2,5):
    for k in range(3):
        boton.append(Button(calc, width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bg = "silver", bd = 4, text = teclas_numericas[i]))
        boton[i].grid(row = j, column = k, pady = 1)
        boton[i]["command"] = lambda x = teclas_numericas [i]: valor_agregado.ingresando_numero(x)
        i += 1

boton_limpiar = Button(calc, text = "CE", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.limpiar_entrada).grid(row = 1, column = 0, pady = 1)
boton_limpiar_todo = Button(calc, text = "C", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.limpiar_todo).grid(row = 1, column = 1, pady = 1)

boton_raiz = Button(calc, text = "√", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.raiz_cuadrada).grid(row = 1, column = 2, pady = 1)
boton_suma = Button(calc, text = "+", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = lambda: valor_agregado.operacion("Suma")).grid(row = 1, column = 3, pady = 1)
boton_resta = Button(calc, text = "-", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = lambda: valor_agregado.operacion("Resta")).grid(row = 2, column = 3, pady = 1)
boton_multiplicacion = Button(calc, text = "*", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = lambda: valor_agregado.operacion("Multiplicacion")).grid(row = 3, column = 3, pady = 1)
boton_division = Button(calc, text = chr(247), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = lambda: valor_agregado.operacion("Division")).grid(row = 4, column = 3, pady = 1)

boton_cero = Button(calc, text = "0", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "silver",
                    command = lambda: valor_agregado.ingresando_numero(0)).grid(row = 5, column = 0, pady = 1)
boton_punto = Button(calc, text = ".", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = lambda: valor_agregado.ingresando_numero(".")).grid(row = 5, column = 1, pady = 1)
boton_punto_medio = Button(calc, text = chr(177), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.math_PM).grid(row = 5, column = 2, pady = 1)
boton_igual = Button(calc, text = "=", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.valor_total).grid(row = 5, column = 3, pady = 1)

boton_pi = Button(calc, text = chr(960), width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.pi).grid(row = 1, column = 4, pady = 1)
boton_cos = Button(calc, text = "cos", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.coseno).grid(row = 1, column = 5, pady = 1)
boton_tan = Button(calc, text = "tan", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.tangente).grid(row = 1, column = 6, pady = 1)
boton_sen = Button(calc, text = "sin", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.seno).grid(row = 1, column = 7, pady = 1)

boton_2pi = Button(calc, text = "2π", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.tau).grid(row = 2, column = 4, pady = 1)
boton_cosh = Button(calc, text = "cosh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.coseno_h).grid(row = 2, column = 5, pady = 1)
boton_tanh = Button(calc, text = "tanh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.tangente_h).grid(row = 2, column = 6, pady = 1)
boton_senh = Button(calc, text = "sinh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.seno_h).grid(row = 2, column = 7, pady = 1)

boton_log = Button(calc, text = "log", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.log).grid(row = 3, column = 4, pady = 1)
boton_exp = Button(calc, text = "Exp", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.exp).grid(row = 3, column = 5, pady = 1)
boton_mod = Button(calc, text = "Mod", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = lambda: valor_agregado.operacion("Mod")).grid(row = 3, column = 6, pady = 1)
boton_e = Button(calc, text = "e", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                   command = valor_agregado.e).grid(row = 3, column = 7, pady = 1)

boton_log2 = Button(calc, text = "log2", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.log2).grid(row = 4, column = 4, pady = 1)
boton_deg = Button(calc, text = "deg", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.degrees).grid(row = 4, column = 5, pady = 1)
boton_acosh = Button(calc, text = "acosh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.acosh).grid(row = 4, column = 6, pady = 1)
boton_asinh = Button(calc, text = "asinh", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.asinh).grid(row = 4, column = 7, pady = 1)

boton_log10 = Button(calc, text = "log10", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.log10).grid(row = 5, column = 4, pady = 1)
boton_log1p = Button(calc, text = "log1p", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.log1p).grid(row = 5, column = 5, pady = 1)
boton_expm1 = Button(calc, text = "expm1", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.expm1).grid(row = 5, column = 6, pady = 1)
boton_lgamma = Button(calc, text = "lgamma", width = 6, height = 2, font = ('Kozuka Mincho Pr6N',20,'bold'), bd = 4, bg = "grey",
                    command = valor_agregado.lgamma).grid(row = 5, column = 7, pady = 1)

labelVista = Label(calc, text = "Calculadora cientifica", font = ("Kozuka Mincho Prn6N", 30, 'bold'), justify = CENTER)
labelVista.grid(row = 0, column = 4, columnspan = 4)

def Salida():
    Salida = tkinter.messagebox.askyesno("Calculadora cientifica","Confirma si quieres salir")
    if Salida > 0:
        root.destroy()
        return

def Cientifica():
    root.resizable(width = False, height = False)
    root.geometry("944x568+0+0")

def Basica():
    root.resizable(width = False, height = False)
    root.geometry("480x568+0+0")


barra_menu = Menu(calc)

menu_principal = Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Archivo", menu = menu_principal)
menu_principal.add_command(label = "Básica", command = Basica)
menu_principal.add_command(label = "Cientifica", command = Cientifica)
menu_principal.add_separator()
menu_principal.add_command(label = "Salir", command = Salida)

root.config(menu = barra_menu)
root.mainloop()
