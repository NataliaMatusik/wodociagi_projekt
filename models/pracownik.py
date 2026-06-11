class Pracownik:
    def __init__(
            self,
            imie,
            nazwisko,
            stanowisko,
            przedsiebiorstwo,
            x,
            y
    ):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.przedsiebiorstwo = przedsiebiorstwo
        self.x = x
        self.y = y

    def __str__(self):
        return (
            f"{self.imie} {self.nazwisko} | "
            f"Stanowisko: {self.stanowisko} | "
            f"Przedsiębiorstwo: {self.przedsiebiorstwo} | "
            f"X: {self.x} | "
            f"Y: {self.y}"
        )