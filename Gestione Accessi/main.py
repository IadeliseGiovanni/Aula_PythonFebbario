# main.py

# MODULARITÀ (import dei moduli)
from utenti import Dipendente, Manager
from controlli import ControlloAccessi


def main():

    # CREAZIONE OGGETTI
    dip = Dipendente("Mario", "B001")
    man = Manager("Luca", "B002")

    sistema = ControlloAccessi()

    # INGRESSI
    sistema.ingresso(dip)
    sistema.ingresso(man)

    # DISATTIVO BADGE
    dip.disattiva_badge()

    # PROVO INGRESSO
    sistema.ingresso(dip)

    # USCITA
    sistema.uscita(man)

    sistema.mostra_log()


if __name__ == "__main__":
    main()
