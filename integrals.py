import sympy as sp

def integrali_indefiniti(y, x):
    return sp.integrate(y, x)

# integrale definito in dx
def integrali_definiti(y, x, a , b):
    return sp.integrate(y,(x, a, b))

print("1. Integrale indefinito")
print("2. Integrale definito")

while True:
    try:
        # prendi l'input dall'utente
        scelta = input("Scegli tra(1/2): ")

        # integrale indefinito (SOLO in dx)
        if scelta == '1':
            integrale_def = input("Inserisci la funzione di cui calcolare l'integrale indefinito: ")

            x = sp.Symbol('x')
            y = sp.Symbol('y')

            print("L'integrale indefinito di", integrale_def, "in dx è:", integrali_indefiniti(integrale_def, x), "+ c")
        
        # integrale definito (SOLO in dx)
        if scelta == '2':
            integrale_indef = input("Inserisci la funzione di cui calcolare l'integrale definito: ")
            a = float(input("Inserisci il primo estremo di integrazione: "))
            b = float(input("Inserisci il secondo estremo di integrazione: "))
            
            x = sp.Symbol('x')
            y = sp.Symbol('y')

            print("L'integrale indefinito di", integrale_indef, "in dx è:", integrali_definiti(integrale_indef, x, a, b))

    # command+c o ctrl+c per stoppare lo script
    except KeyboardInterrupt:
        break
    