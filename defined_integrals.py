import sympy as sp

# integrale in dx
def integrali_definiti(y, x, a, b):
    # calcolo integrale
    integrando = sp.sympify(y)
    integrale = sp.integrate(integrando, (x, a, b))
    return integrale.doit()

# integrale doppio in dx dy
def doppio(integrando, x_lower, x_upper, y_lower, y_upper):
    # estremi di integrazione
    x = sp.symbols('x')
    y = sp.symbols('y')

    # calcolo integrale
    funzione = sp.sympify(integrando)
    integrale = sp.integrate(sp.integrate(funzione, (x, x_lower, x_upper)), (y, y_lower, y_upper))
    return integrale

# integrale triplo in dx dy dz
def triplo(integrando, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper):
    # estremi di integrazione
    x = sp.symbols('x')
    y = sp.symbols('y')
    z = sp.symbols('z')
    
    # calcolo integrale
    funzione = sp.sympify(integrando)
    integrale = sp.integrate(sp.integrate(sp.integrate(funzione, (x, x_lower, x_upper)), (y, y_lower, y_upper)), (z, z_lower, z_upper))
    return integrale

print("Calcolo integrali definiti 2.0")
print("1. Integrale definito in dx")
print("2. Integrale definito doppio in dxdy")
print("3. Integrale definito triplo in dxdydz")

while True:
    try:
        # scelta calcolo integrale
        scelta = input("Scegli tra (1/2/3):")

        if scelta == "1":
            # funzione da integrare
            integrale_indef = input("Inserisci la funzione di cui calcolare l'integrale definito (usa x come variabile): ")
            
            # limite inferiore
            a_lower = float(input("Inserisci il primo estremo di integrazione (a): "))

            #limite superiore
            b_upper = float(input("Inserisci il secondo estremo di integrazione (b): "))
            
            x = sp.Symbol('x')
            y = sp.Symbol('y')

            print("L'integrale indefinito di", repr(integrale_indef), "in dx è:", integrali_definiti(integrale_indef, x, a_lower, b_upper))

        # integrale definito doppio
        elif scelta == "2":
            # funzione da integrare
            integrando = input("Inserisci la funzione da integrare (usa x,y come variabili): ")

            # estremi x
            x_lower = float(input("Inserisci il limite inferiore di x (a): "))
            x_upper = float(input("Inserisci il limite superiore di x (b): "))
            
            # estremi y
            y_lower = float(input("Inserisci il limite inferiore di y (a): "))
            y_upper = float(input("Inserisci il limite superiore di y (b): "))

            # risultato
            risultato = doppio(integrando, x_lower, x_upper, y_lower, y_upper)
            print("Il risultato dell'integrale doppio di", repr(integrando), "su x da", x_lower, "a", x_upper, "e su y da", y_lower, "a", y_upper, "è:", risultato)
        
        # integrale definito triplo
        elif scelta == "3":
            # funzione da integrare
            integrando = input("Inserisci la funzione da integrare (usa x,y,z come variabili): ")
            
            # estremi x
            x_lower = float(input("Inserisci il limite inferiore di x (a): "))
            x_upper = float(input("Inserisci il limite superiore di x (b): "))
            
            # estremi y
            y_lower = float(input("Inserisci il limite inferiore di y (a): "))
            y_upper = float(input("Inserisci il limite superiore di y (b): "))
            
            # estremi z
            z_lower = float(input("Inserisci il limite inferiore di z (a): "))
            z_upper = float(input("Inserisci il limite superiore di z (b): "))

            # risultato
            risultato = triplo(integrando, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)
            print("Il risultato dell'integrale triplo di", repr(integrando), "su x da", x_lower, "a", x_upper, "su y da", y_lower, "a", y_upper, "e su z da", z_lower, "a", z_upper, "è:", risultato)

        else:
            print("Scelta non valida, riprova")
    
    except KeyboardInterrupt:
        break          