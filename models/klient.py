class Klient:
    def __init__(
            self,
            imie,
            nazwisko,
            adres,
            przedsiebiorstwo,
            x,
            y
    ):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.przedsiebiorstwo = przedsiebiorstwo
        self.x = x
        self.y = y

    def __str__(self):
        return (
            f"{self.imie} {self.nazwisko} | "
            f"Adres: {self.adres} | "
            f"Przedsiębiorstwo: {self.przedsiebiorstwo} | "
            f"X: {self.x} | "
            f"Y: {self.y}"
        )