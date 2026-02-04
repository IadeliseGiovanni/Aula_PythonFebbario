#1 Esercizio
numero = int (input("Inserisci il numero") )
if numero %2 == 0:
    print ("pari")
else :
    print ("dispari")


#2 Esercizio 
# --- PUNTO 1: PARI O DISPARI ---
numero = int(input("Inserisci un numero: "))
if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")
while True:
    n = int(input("Inserisci un numero per il countdown: "))
    for i in range(n, -1, -1):
        print(i)

numeri = [2, 3, 5, 8]
for n in numeri:
    print(n * n)


lista_utente = []
while len(lista_utente) < 5:
    valore = int(input("Inserisci un numero per la lista: "))
    lista_utente.append(valore)


if len(lista_utente) == 0:
    print("Lista Vuota")
else:
    massimo = lista_utente[0]
    for n in lista_utente:
        if n > massimo:
            massimo = n

    conteggio = 0
    while conteggio < len(lista_utente):
        conteggio = conteggio + 1
        
    print("Il numero massimo trovato è:", massimo)
    print("Il numero di elementi nella lista è:", conteggio)    

    