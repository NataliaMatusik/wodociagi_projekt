from models.klient import Klient


class KlientService:
    def __init__(self):
        self.klienci = []

    def dodaj_klienta(
            self,
            imie,
            nazwisko,
            adres,
            przedsiebiorstwo
    ):
        nowy_klient = Klient(
            imie,
            nazwisko,
            adres,
            przedsiebiorstwo
        )

        self.klienci.append(nowy_klient)

    def pobierz_wszystkich(self):
        return self.klienci