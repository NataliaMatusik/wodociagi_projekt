from services.przedsiebiorstwo_service import PrzedsiebiorstwoService


service = PrzedsiebiorstwoService()

service.dodaj_przedsiebiorstwo(
    "MPWiK Kraków",
    "Kraków",
    150000
)

service.dodaj_przedsiebiorstwo(
    "Wodociągi Warszawskie",
    "Warszawa",
    300000
)

for p in service.pobierz_wszystkie():
    print(p)