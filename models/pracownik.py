class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, przedsiebiorstwo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.przedsiebiorstwo = przedsiebiorstwo

    def __str__(self):
        return (
            f"{self.imie} {self.nazwisko} | "
            f"Stanowisko: {self.stanowisko} | "
            f"Przedsiębiorstwo: {self.przedsiebiorstwo}"
        )