'''creare un sistema di funzioni che richiami tutte le singole parti che abbiamo creato nel precedente esercizio, 
devono essere usate SOLO funzioni e almeno da 2 decoratori ed essere ripetibile'''


import time                                            # prendo l'orologio per gestire i tempi

def logger(funzione):                                  # segno quando parte il lavoro
    def wrapper(*args):                      # contenitore universale per i dati
        print(f"\n[LOG] avvio di: {funzione.__name__}") # dico quale funzione sta girando
        return funzione(*args)               # eseguo l'azione vera e propria
    return wrapper                                     # chiudo il logger

def calcola_tempo(funzione):                           # cronometro la velocità del codice
    def wrapper(*args):                      # altro contenitore per i dati
        inizio = time.time()                           # segno l'ora esatta di inizio
        risultato = funzione(*args)          # faccio fare il calcolo alla funzione
        fine = time.time()                             # segno l'ora di fine
        print(f"[TIMER] ci ha messo: {fine - inizio:.6f}s") # stampo quanto tempo è passato
        return risultato                               # ti ridò il risultato finale
    return wrapper                                     # chiudo il cronometro

def calcola_fattoriale(n):                             # logica per il calcolo matematico
    risultato = 1                                      # parto da uno per moltiplicare
    for i in range(1, n + 1):                          # giro per ogni numero fino a n
        risultato *= i                                 # moltiplico il totale per il numero corrente
    return risultato                                   # ti dico quanto fa il totale

@logger                                                # primo decoratore applicato
@calcola_tempo                                         # secondo decoratore applicato
def esegui_sistema(numero):                            # funzione principale richiesta dalla traccia
    print(f"inizio il calcolo per il numero {numero}") # messaggio di avvio
    f = calcola_fattoriale(numero)                     # richiamo il calcolo
    print(f"il risultato finale è: {f}")               # stampo il numerone uscito fuori

# esecuzione
esegui_sistema(5)                                     
esegui_sistema(10)                                   