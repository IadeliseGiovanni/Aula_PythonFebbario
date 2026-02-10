'''1 Gestione Clienti:



I clienti possono visualizzare gli articoli disponibili in inventario.



I clienti possono selezionare e acquistare articoli dall'inventario.



Il sistema tiene traccia degli acquisti dei clienti.'''

class Negozio:
    def __init__(self):
        self.inventario = {} 
        self.vendite = []     
        self.guadagni = 0     
        self.admins = {"admin": "123"} 

    def aggiungi_prodotto(self, nome, prezzo, quantita):
        self.inventario[nome] = {"prezzo": prezzo, "quantita": quantita}
        print(f"prodotto {nome} aggiunto con successo!")

    def visualizza_inventario(self):
        print("\n--- vetrina negozio ---")
        for nome, info in self.inventario.items():
            p = info["prezzo"]
            q = info["quantita"]
            print(f"articolo: {nome} | prezzo: {p}€ | pezzi: {q}")

    def acquista_prodotto(self, nome_prodotto, qta_da_comprare):
        if nome_prodotto in self.inventario:
            if self.inventario[nome_prodotto]["quantita"] >= qta_da_comprare:
                prezzo_unitario = self.inventario[nome_prodotto]["prezzo"]
                costo_totale = prezzo_unitario * qta_da_comprare
                self.inventario[nome_prodotto]["quantita"] -= qta_da_comprare
                self.guadagni += costo_totale
                self.vendite.append(f"venduto {qta_da_comprare}x {nome_prodotto} per {costo_totale}€")
                print(f"acquisto di {nome_prodotto} riuscito! totale: {costo_totale}€")
            else:
                print("quantità non sufficiente!")
        else:
            print("prodotto non trovato!")

    def report_amministratore(self):
        print("\n=== REPORT AMMINISTRAZIONE ===")
        print(f"incasso totale: {self.guadagni}€")
        for v in self.vendite:
            print(f"- {v}")

mio_negozio = Negozio()
mio_negozio.aggiungi_prodotto("mela", 0.5, 10)
mio_negozio.aggiungi_prodotto("pane", 1.2, 5)

while True:
    print("\n1. cliente | 2. admin | 3. esci")
    scelta = input("chi sei? ")
    
    if scelta == "1":
        mio_negozio.visualizza_inventario()
        prodotto = input("cosa vuoi comprare? ")
        quantita = int(input("quanti? "))
        mio_negozio.acquista_prodotto(prodotto, quantita)
        
    elif scelta == "2":
        u = input("admin user: ")
        p = input("password: ")
        if u in mio_negozio.admins and mio_negozio.admins[u] == p:
            mio_negozio.report_amministratore()
        else:
            print("errore!")
            
    elif scelta == "3":
        print("grazie e arrivederci!")
        break


    #2

def rimuovi_prodotto(self, nome):
        #controllo se il prodotto è presente
        if nome in self.inventario:
            del self.inventario[nome]
            print(f"prodotto {nome} rimosso dal listino.")
        else:
            print(f"errore: il prodotto {nome} non esiste.")

def aggiorna_scorte(self, nome, nuova_qta):
        if nome in self.inventario:
            #accedo alla chiave "quantita" e gli assegno il nuovo valore
            self.inventario[nome]["quantita"] = nuova_qta
            print(f"quantità di {nome} aggiornata a {nuova_qta} pezzi.")
        else:
            print(f"errore: impossibile aggiornare, {nome} non trovato.")

def aggiorna_prezzo(self, nome, nuovo_prezzo):
        if nome in self.inventario:
            #cambio il valore
            self.inventario[nome]["prezzo"] = nuovo_prezzo
            print(f"prezzo di {nome} aggiornato a {nuovo_prezzo}€.")
        else:
            print(f"errore: prodotto {nome} non trovato.")