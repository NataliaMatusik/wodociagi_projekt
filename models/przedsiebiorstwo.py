class Przedsiebiorstwo:
    def __init__(
            self,
            nazwa,
            miasto,
            liczba_klientow,
            x,
            y
    ):
        self.nazwa = nazwa
        self.miasto = miasto
        self.liczba_klientow = liczba_klientow
        self.x = x
        self.y = y

    def __str__(self):
        return (
            f"{self.nazwa} | "
            f"Miasto: {self.miasto} | "
            f"Klienci: {self.liczba_klientow} | "
            f"X: {self.x} | "
            f"Y: {self.y}"
        )