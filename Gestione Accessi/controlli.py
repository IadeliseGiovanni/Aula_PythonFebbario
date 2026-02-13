# controlli.py

from datetime import datetime


class ControlloAccessi:

    def __init__(self):
        self.__log = []  # INCAPSULAMENTO (attributo privato)

    def ingresso(self, utente):

        # POLIMORFISMO (ruolo cambia in base al tipo di oggetto)
        if utente.badge_attivo():
            orario = datetime.now().strftime("%H:%M:%S")
            messaggio = f"{orario} - {utente.get_nome()} ({utente.ruolo()}) ENTRATA"
            self.__log.append(messaggio)
            print(messaggio)
        else:
            print(f"Accesso NEGATO per {utente.get_nome()} (badge disattivato)")

    def uscita(self, utente):
        orario = datetime.now().strftime("%H:%M:%S")
        messaggio = f"{orario} - {utente.get_nome()} ({utente.ruolo()}) USCITA"
        self.__log.append(messaggio)
        print(messaggio)

    def mostra_log(self):
        print("\n--- LOG ACCESSI ---")
        for evento in self.__log:
            print(evento)

#Il polimorfismo si trova nel metodo ruolo(),
#  che viene implementato in modo diverso da Dipendente e Manager, e viene usato nel metodo ingresso del file controll