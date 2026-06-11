from models.pracownik import Pracownik


class PracownikService:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(
            self,
            imie,
            nazwisko,
            stanowisko,
            przedsiebiorstwo
    ):
        nowy_pracownik = Pracownik(
            imie,
            nazwisko,
            stanowisko,
            przedsiebiorstwo
        )

        self.pracownicy.append(nowy_pracownik)

    def pobierz_wszystkich(self):
        return self.pracownicy