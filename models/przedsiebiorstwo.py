class Przedsiebiorstwo:
    def __init__(self, nazwa, miasto, liczba_klientow):
        self.nazwa = nazwa
        self.miasto = miasto
        self.liczba_klientow = liczba_klientow

    def __str__(self):
        return (
            f"{self.nazwa} | "
            f"Miasto: {self.miasto} | "
            f"Klienci: {self.liczba_klientow}"
        )