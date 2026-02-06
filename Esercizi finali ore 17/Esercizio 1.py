'''Crea un esercizio che rappresenti tutto quello che hai imparato nella settimana precedente, riprendi la tabella delle conoscenze per maggiori info.'''

import time                                            # prendo gli strumenti per gestire il tempo

def logger(funzione):                                  # creo il sistema per segnarmi quando parte la funzione
    def wrapper(*args):                      # questo serve per gestire ogni tipo di dato in ingresso
        print(f"\n[LOG] sto facendo partire: {funzione.__name__}") # mi avvisa quale funzione sta girando
        return funzione(*args)               # avvio il lavoro vero
    return wrapper                                     # riporto fuori il risultato

def calcola_tempo(funzione):                           # sistema per cronometrare il codice
    def wrapper(*args):                      # contenitore per far passare i dati
        inizio = time.time()                           # segno l'ora esatta dell'inizio
        risultato = funzione(*args)          # faccio fare il calcolo
        fine = time.time()                             # segno l'ora della fine
        print(f"[TIMER] ci ha messo: {fine - inizio:.6f}s") # stampo la durata
        return risultato                               # ti ridò il risultato finale
    return wrapper                                     # chiudo il cronometro

def calcola_fattoriale(n):                             # logica per il calcolo del fattoriale
    risultato = 1                                      # parto da uno per moltiplicare
    for i in range(1, n + 1):                          # giro per ogni numero fino a n
        risultato *= i                                 # moltiplico il totale per il numero corrente
    return risultato                                   # alla fine ti dico il totale

@logger                                                # primo decoratore applicato (parte 2)
@calcola_tempo                                         # secondo decoratore applicato (parte 2)
def sistema_riassuntivo(lista_numeri):                 # funzione che richiama le parti precedenti
    print("--- AVVIO SISTEMA DI CONTROLLO ---")       # messaggio di benvenuto
    for n in lista_numeri:                             # rendo il sistema ripetibile su una lista
        res = calcola_fattoriale(n)                    # richiamo la parte del fattoriale
        print(f"fattoriale di {n}: {res}")             # mostro il risultato
    print("--- OPERAZIONE COMPLETATA ---")             # messaggio di chiusura


numeri_da_testare = [5, 10]                            # lista di numeri per il test
sistema_riassuntivo(numeri_da_testare)                 # lancio il sistema completo