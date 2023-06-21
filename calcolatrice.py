# -*- coding: utf-8 -*-
# Calcolatrice
import math
import sympy as sp
import mpmath as mp
import numpy as np
import matplotlib.pyplot as plt

def addizione(x,y):
    return x + y

def sottrazione(x,y):
    return x-y

def moltiplicazione(x,y):
    return x*y

def divisione(x,y):
    return x/y

def potenza(x,y):
    return x**y

def radice_quadrata(x):
    return math.sqrt(x)

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arcoseno(x):
    return math.asin(x)

def arcocoseno(x):
    return math.acos(x)

def arcotangente(x):
    return math.atan(x)

def logaritmo_naturale(x,y):
    return math.log(x,y)

def logaritmo(x, y):
    return math.log(x, y)

def gradi_in_radianti(x):
    return math.radians(x)

def integrali_indefiniti(y, x):
    return sp.integrate(y, x)

def integrali_definiti(y, x, a , b):
    return sp.integrate(y,(x, a, b))

def fattoriale(x):
    return math.factorial(x)

def max_comun_divisore(x, y):
    return math.gcd(x, y)

def min_comune_multiplo(x, y):
    return math.lcm(x, y)

def derivata_nesima(y, x, n):
    return sp.diff(y, x, n)

def scomposizione_numeri_primi(x):
    return sp.factorint(x)

def limite(f, x, z):
    return sp.limit(f, x, z)

def equazioni(x, y):
    return sp.solve(x, y)

def secante(x):
    return mp.sec(x)

def cotangente(x):
    return mp.cot(x)

def cosecante(x):
    return mp.csc(x)

def espansione(x):
    return sp.expand(x)

def num_complessi(x, y):
    return complex(x, y)

def maggiore_minore_uguale(x, y):
    if x == y:
        return x, "è uguale a", y
    if x < y:
        return x, "è minore di", y
    if x > y:
        return x, "è maggiore di", y

def matrice(x):
    return np.array(x)

print("Calcolatrice scientifica versione 1.0")
print("Seleziona un'operazione: ")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")
print("5. Elevamento a potenza")
print("6. Radice quadrata")
print("7. Seno")
print("8. Coseno")
print("9. Tangente")
print("10. Arcoseno")
print("11. Arcocoseno")
print("12. Arcotangente")
print("13. Logaritmo naturale")
print("14. Logaritmo in base n")
print("15. Gradi in radianti")
print("16. Integrale indefinito")
print("17. Integrale definito")
print("18. Fattoriali")
print("19. Massimo comun divisore")
print("20. Minimo comune multiplo")
print("21. Derivate")
print("22. Scomposizione in fattori primi")
print("23. Limiti")
print("24. Equazioni di n grado")
print("25. Secante")
print("26. Cotangente")
print("27. Cosecante")
print("28. Quadrato di binomio")
print("29. Cubo di binomio")
print("30. Quadrato di trinomio")
print("31. Cubo di trinomio")
print("32. Studio di funzione")
print("33. Numeri complessi")
print("34. Stabilire se un numero è maggiore, minore o uguale di un altro")
print("35. Matrici")

while True:
    # prendi l'input dall'utente
    scelta = input("Scegli tra(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35): ")

    # controlla se la scelta è una delle 5 opzioni
    if scelta in('1', '2', '3', '4', '5', '34'):
        num1 = float(input("Inserisci il valore da immettere nell'operazione scelta: "))
        num2 = float(input("Inserisci il valore da immettere nell'operazione scelta: "))

    if scelta in('6', '7', '8', '9', '10', '11', '12', '13', '15', '25', '26', '27'):
        num3 = float(input("Inserisci il valore da immettere nell'operazione scelta: "))

    if scelta in('16', '21', '28', '29', '30', '35'):
        num9 = input("Inserisci il valore da immettere nell'operazione scelta: ")

    if scelta in('17'):
        num10 = input("Inserisci il valore da immettere nell'operazione scelta: ")
        num11 = float(input("Inserisci il primo estremo di integrazione: "))
        num12 = float(input("Inserisci il secondo estremo di integrazione: "))

    if scelta in('18', '22'):
        num13 = int(input("Inserisci il valore da immettere nell'operazione scelta:"))

    if scelta in('19', '20'):
        num14 = int(input("Inserisci il primo numero:"))
        num15 = int(input("Inserisci il secondo numero:"))

    if scelta in('21'):
        num16 = input("Inserisci il valore da immettere nell'operazione scelta: ")
        grado_derivata = int(input("Inserisci il grado di derivazione: "))

    if scelta in('23'):
        num17 = input("Inserisci il valore da immettere nell'operazione scelta: ")

    if scelta in('14'):
        num18 = float(input("Inserisci il valore di cui vuoi calcolare il suo logaritmo:"))
        num19 = int(input("Inserisci la base del logaritmo:"))

    if scelta in('24'):
        num20 = input("Inserisci l'equazione che vuoi risolvere:")
        num21 = input("Inserisci la variabile rispetto alla quale vuoi risolverla:")

    if scelta in('33'):
        num22 = int(input("Inserisci la parte reale del numero complesso:"))
        num23 = int(input("Inserisci la parte immaginaria del numero complesso:"))

    if scelta == '1':
        print(num1, "+", num2, "=", addizione(num1, num2))

    elif scelta == '2':
        print(num1, "-", num2, "=", sottrazione(num1, num2))

    elif scelta == '3':
        print(num1, "*", num2, "=", moltiplicazione(num1, num2))

    elif scelta == '4':
        print(num1, "/", num2, "=", divisione(num1, num2))

    elif scelta == '5':
        print(num1, "**", num2, "=", potenza(num1, num2))

    elif scelta == '6':
        print("Radice quadrata di:", num3, "=", radice_quadrata(num3))

    elif scelta == '7':
        num4 = math.radians(num3)
        print("sin(", num4, ")=", seno(num4))

    elif scelta == '8':
        num5 = math.radians(num3)
        print("cos(", num5, ")=", coseno(num5))

    elif scelta == '9':
        num8 = math.radians(num3)
        print("tan(", num3, ")=", tangente(num8))

    elif scelta == '10':
        print("arcsin(", num3, ")=", arcoseno(num3))

    elif scelta == '11':
        print("arccos(", num3, ")=", arcocoseno(num3))

    elif scelta == '12':
        print("arctan(", num3, ")=", arcotangente(num3))

    elif scelta == '13':
        print("ln(", num3, ")=", logaritmo_naturale(num3))

    elif scelta == '14':
        print("Il logaritmo in base", num19, "di", num18, "è:", logaritmo(num18, num19))

    elif scelta == "15":
        print("L'angolo di", num3, "gradi in radianti è:", gradi_in_radianti(num3))

    elif scelta == '16':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        y = num9
        print("Integrale indefinito di", y, "in dx è:", integrali_indefiniti(y, x))

    elif scelta == '17':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        y = num10
        a = num11
        b = num12
        print("Integrale indefinito di", y, "in dx è:", integrali_definiti(y, x, a, b))

    elif scelta == '18':
        print("Il fattoriale di", num13, "è:", fattoriale(num13))

    elif scelta == '19':
        print("Il massimo comun divisore tra", num14, "e", num15, "è:", max_comun_divisore(num14, num15))

    elif scelta == '20':
        print("Il minimo comune multiplo tra", num14, "e", num15, "è:", min_comune_multiplo(num14, num15))

    elif scelta == '21':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        y = num16
        n = grado_derivata
        print("Derivata n-esima di (grado scelto dall'input)", y, "è:", derivata_nesima(y, x, n))

    elif scelta == '22':
        print("La scomposizione in fattori primi di", num13, "è:", scomposizione_numeri_primi(num13))

    elif scelta == '23':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Limite di", num17, "=", limite(num17, x, sp.oo))

    elif scelta == '24':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Il risultato dell'equazione", num20, "è:", equazioni(num20, num21))

    elif scelta == '25':
        print("La secante di", num3, "è:", secante(num3))

    elif scelta == '26':
        print("La cotangente di", num3, "è:", cotangente(num3))

    elif scelta == '27':
        print("La cosecante di", num3, "è:", cosecante(num3))

    elif scelta == '28':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Il quadrato di binomio di", num9, "è:", espansione(num9))

    elif scelta == '29':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Il cubo di binomio di", num9, "è:", espansione(num9))

    elif scelta == '30':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Il quadrato di trinomio di", num9, "è:", espansione(num9))

    elif scelta == '31':
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        print("Il cubo di trinomio di", num9, "è:", espansione(num9))

    elif scelta == '32':
        x = np.linspace(-20, 20, 8000)
        y = 3*x +2
        plt.figure('Studio di funzione')
        plt.title('Studio di funzione')
        plt.xlim([-20, 20])
        plt.ylim([-20, 20])
        plt.plot(x, y, color='green', label = y, linewidth=4)
        plt.axhline(color='black')
        plt.axvline(color='black')
        plt.legend()
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        plt.style.use("seaborn-dark-palette")

    elif scelta == '33':
        print("Il numero complesso generato dalle variabili inserite è:", num_complessi(num22, num23))

    elif scelta == '34':
        print(maggiore_minore_uguale(num1, num2))

    elif scelta == '35':
        print("Il risultato della matrice è:", matrice(x))

    operazione = input("Vuoi fare un'altra operazione (si/no): ")
    if operazione == "no":
        break

    if operazione != "si":
        print("Input errato")
