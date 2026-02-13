# utenti.py

# ASTRAZIONE
class Utente:
    def __init__(self, nome, codice_badge):
        self._nome = nome                  # INCAPSULAMENTO
        self._codice_badge = codice_badge  # INCAPSULAMENTO
        self._badge_attivo = True          # INCAPSULAMENTO

    def get_nome(self):
        return self._nome

    def badge_attivo(self):
        return self._badge_attivo

    def disattiva_badge(self):
        self._badge_attivo = False

    # POLIMORFISMO (metodo astratto)
    def ruolo(self):
        raise NotImplementedError("Metodo da implementare")


# EREDITARIETÀ
class Dipendente(Utente):

    # POLIMORFISMO
    def ruolo(self):
        return "Dipendente"


# EREDITARIETÀ
class Manager(Utente):

    # POLIMORFISMO
    def ruolo(self):
        return "Manager"

#erditarietà  dove dipende da dipendente e manager dipendono dalla classe utente
#L’incapsulamento protegge i dati usando attributi interni come _nome e __log.