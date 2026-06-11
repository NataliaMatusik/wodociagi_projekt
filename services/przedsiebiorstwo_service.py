from models.przedsiebiorstwo import Przedsiebiorstwo


class PrzedsiebiorstwoService:
    def __init__(self):
        self.przedsiebiorstwa = []

    def dodaj_przedsiebiorstwo(
            self,
            nazwa,
            miasto,
            liczba_klientow,
            x,
            y
    ):
        nowe = Przedsiebiorstwo(
            nazwa,
            miasto,
            liczba_klientow,
            x,
            y
        )

        self.przedsiebiorstwa.append(nowe)

    def pobierz_wszystkie(self):
        return self.przedsiebiorstwa