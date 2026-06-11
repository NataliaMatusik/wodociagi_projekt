class Klient:
    def __init__(self, imie, nazwisko, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

    def __str__(self):
        return (
            f"{self.imie} {self.nazwisko} | "
            f"Adres: {self.adres}"
        )