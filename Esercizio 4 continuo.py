lista = []
while len(lista) < 5:
    valore = int(input("Inserisci un numero: "))
    lista.append(valore) #aggiunge

if len(lista) == 0: #lunghezza
    print("Lista Vuota")
else:
    massimo = lista[0]
    for n in lista:
        if n > massimo:
            massimo = n
    
    conteggio = 0
    while conteggio < len(lista):
        conteggio = conteggio + 1

    print("Il numero massimo è:", massimo)
    print("Nella lista ci sono", conteggio, "numeri")

#5 Esercizio
