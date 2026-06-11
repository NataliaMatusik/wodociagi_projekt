from models.klient import Klient


class KlientService:
    def __init__(self):
        self.klienci = []

    def dodaj_klienta(
            self,
            imie,
            nazwisko,
            adres,
            przedsiebiorstwo,
            x,
            y
    ):
        nowy_klient = Klient(
            imie,
            nazwisko,
            adres,
            przedsiebiorstwo,
            x,
            y
        )

        self.klienci.append(nowy_klient)

    def pobierz_wszystkich(self):
        return self.klienci