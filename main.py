import tkinter as tk
from services.przedsiebiorstwo_service import PrzedsiebiorstwoService
from services.pracownik_service import PracownikService
from services.klient_service import KlientService


def odswiez_liste_przedsiebiorstw():
    listbox_przedsiebiorstwa.delete(0, tk.END)

    for przedsiebiorstwo in service.pobierz_wszystkie():
        listbox_przedsiebiorstwa.insert(tk.END, przedsiebiorstwo)


def odswiez_liste_pracownikow():
    listbox_pracownicy.delete(0, tk.END)

    for pracownik in pracownik_service.pobierz_wszystkich():
        listbox_pracownicy.insert(tk.END, pracownik)


def odswiez_liste_klientow():
    listbox_klienci.delete(0, tk.END)

    for klient in klient_service.pobierz_wszystkich():
        listbox_klienci.insert(tk.END, klient)


def dodaj_przedsiebiorstwo():
    nazwa = entry_nazwa.get()
    miasto = entry_miasto.get()
    liczba_klientow = entry_liczba_klientow.get()
    x = entry_x_przedsiebiorstwa.get()
    y = entry_y_przedsiebiorstwa.get()

    service.dodaj_przedsiebiorstwo(
        nazwa,
        miasto,
        liczba_klientow,
        x,
        y
    )

    odswiez_liste_przedsiebiorstw()

    entry_nazwa.delete(0, tk.END)
    entry_miasto.delete(0, tk.END)
    entry_liczba_klientow.delete(0, tk.END)
    entry_x_przedsiebiorstwa.delete(0, tk.END)
    entry_y_przedsiebiorstwa.delete(0, tk.END)


def usun_przedsiebiorstwo():
    zaznaczenie = listbox_przedsiebiorstwa.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]
        service.przedsiebiorstwa.pop(indeks)
        odswiez_liste_przedsiebiorstw()

def edytuj_przedsiebiorstwo():
    zaznaczenie = listbox_przedsiebiorstwa.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]
        przedsiebiorstwo = service.przedsiebiorstwa[indeks]

        entry_nazwa.delete(0, tk.END)
        entry_miasto.delete(0, tk.END)
        entry_liczba_klientow.delete(0, tk.END)
        entry_x_przedsiebiorstwa.delete(0, tk.END)
        entry_y_przedsiebiorstwa.delete(0, tk.END)

        entry_nazwa.insert(0, przedsiebiorstwo.nazwa)
        entry_miasto.insert(0, przedsiebiorstwo.miasto)
        entry_liczba_klientow.insert(0, przedsiebiorstwo.liczba_klientow)
        entry_x_przedsiebiorstwa.insert(0, przedsiebiorstwo.x)
        entry_y_przedsiebiorstwa.insert(0, przedsiebiorstwo.y)

        button_dodaj.config(
            text="Zapisz zmiany",
            command=lambda: zapisz_zmiany_przedsiebiorstwa(indeks)
        )


def zapisz_zmiany_przedsiebiorstwa(indeks):
    service.przedsiebiorstwa[indeks].nazwa = entry_nazwa.get()
    service.przedsiebiorstwa[indeks].miasto = entry_miasto.get()
    service.przedsiebiorstwa[indeks].liczba_klientow = entry_liczba_klientow.get()
    service.przedsiebiorstwa[indeks].x = entry_x_przedsiebiorstwa.get()
    service.przedsiebiorstwa[indeks].y = entry_y_przedsiebiorstwa.get()

    odswiez_liste_przedsiebiorstw()

    entry_nazwa.delete(0, tk.END)
    entry_miasto.delete(0, tk.END)
    entry_liczba_klientow.delete(0, tk.END)
    entry_x_przedsiebiorstwa.delete(0, tk.END)
    entry_y_przedsiebiorstwa.delete(0, tk.END)

    button_dodaj.config(
        text="Dodaj przedsiębiorstwo",
        command=dodaj_przedsiebiorstwo
    )



def usun_pracownika():
    zaznaczenie = listbox_pracownicy.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]

        pracownik_service.pracownicy.pop(indeks)

        odswiez_liste_pracownikow()


def edytuj_pracownika():
    zaznaczenie = listbox_pracownicy.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]
        pracownik = pracownik_service.pracownicy[indeks]

        entry_imie.delete(0, tk.END)
        entry_nazwisko.delete(0, tk.END)
        entry_stanowisko.delete(0, tk.END)
        entry_firma_pracownika.delete(0, tk.END)
        entry_x_pracownika.delete(0, tk.END)
        entry_y_pracownika.delete(0, tk.END)

        entry_imie.insert(0, pracownik.imie)
        entry_nazwisko.insert(0, pracownik.nazwisko)
        entry_stanowisko.insert(0, pracownik.stanowisko)
        entry_firma_pracownika.insert(0, pracownik.przedsiebiorstwo)
        entry_x_pracownika.insert(0, pracownik.x)
        entry_y_pracownika.insert(0, pracownik.y)

        button_dodaj_pracownika.config(
            text="Zapisz zmiany",
            command=lambda: zapisz_zmiany_pracownika(indeks)
        )


def zapisz_zmiany_pracownika(indeks):
    pracownik_service.pracownicy[indeks].imie = entry_imie.get()
    pracownik_service.pracownicy[indeks].nazwisko = entry_nazwisko.get()
    pracownik_service.pracownicy[indeks].stanowisko = entry_stanowisko.get()
    pracownik_service.pracownicy[indeks].przedsiebiorstwo = entry_firma_pracownika.get()
    pracownik_service.pracownicy[indeks].x = entry_x_pracownika.get()
    pracownik_service.pracownicy[indeks].y = entry_y_pracownika.get()

    odswiez_liste_pracownikow()

    entry_imie.delete(0, tk.END)
    entry_nazwisko.delete(0, tk.END)
    entry_stanowisko.delete(0, tk.END)
    entry_firma_pracownika.delete(0, tk.END)
    entry_x_pracownika.delete(0, tk.END)
    entry_y_pracownika.delete(0, tk.END)

    button_dodaj_pracownika.config(
        text="Dodaj pracownika",
        command=dodaj_pracownika
    )



def dodaj_pracownika():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    stanowisko = entry_stanowisko.get()
    przedsiebiorstwo = entry_firma_pracownika.get()
    x = entry_x_pracownika.get()
    y = entry_y_pracownika.get()

    pracownik_service.dodaj_pracownika(
        imie,
        nazwisko,
        stanowisko,
        przedsiebiorstwo,
        x,
        y
    )

    odswiez_liste_pracownikow()

    entry_imie.delete(0, tk.END)
    entry_nazwisko.delete(0, tk.END)
    entry_stanowisko.delete(0, tk.END)
    entry_firma_pracownika.delete(0, tk.END)
    entry_x_pracownika.delete(0, tk.END)
    entry_y_pracownika.delete(0, tk.END)


def dodaj_klienta():
    imie = entry_imie_klienta.get()
    nazwisko = entry_nazwisko_klienta.get()
    adres = entry_adres_klienta.get()
    przedsiebiorstwo = entry_firma_klienta.get()
    x = entry_x_klienta.get()
    y = entry_y_klienta.get()

    klient_service.dodaj_klienta(
        imie,
        nazwisko,
        adres,
        przedsiebiorstwo,
        x,
        y
    )

    odswiez_liste_klientow()

    entry_imie_klienta.delete(0, tk.END)
    entry_nazwisko_klienta.delete(0, tk.END)
    entry_adres_klienta.delete(0, tk.END)
    entry_firma_klienta.delete(0, tk.END)
    entry_x_klienta.delete(0, tk.END)
    entry_y_klienta.delete(0, tk.END)



def usun_klienta():
    zaznaczenie = listbox_klienci.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]

        klient_service.klienci.pop(indeks)

        listbox_klienci.delete(0, tk.END)

        for klient in klient_service.pobierz_wszystkich():
            listbox_klienci.insert(tk.END, klient)

def edytuj_klienta():
    zaznaczenie = listbox_klienci.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]
        klient = klient_service.klienci[indeks]

        entry_imie_klienta.delete(0, tk.END)
        entry_nazwisko_klienta.delete(0, tk.END)
        entry_adres_klienta.delete(0, tk.END)
        entry_firma_klienta.delete(0, tk.END)
        entry_x_klienta.delete(0, tk.END)
        entry_y_klienta.delete(0, tk.END)

        entry_imie_klienta.insert(0, klient.imie)
        entry_nazwisko_klienta.insert(0, klient.nazwisko)
        entry_adres_klienta.insert(0, klient.adres)
        entry_firma_klienta.insert(0, klient.przedsiebiorstwo)
        entry_x_klienta.insert(0, klient.x)
        entry_y_klienta.insert(0, klient.y)

        button_dodaj_klienta.config(
            text="Zapisz zmiany",
            command=lambda: zapisz_zmiany_klienta(indeks)
        )



def zapisz_zmiany_klienta(indeks):
    klient_service.klienci[indeks].imie = entry_imie_klienta.get()
    klient_service.klienci[indeks].nazwisko = entry_nazwisko_klienta.get()
    klient_service.klienci[indeks].adres = entry_adres_klienta.get()
    klient_service.klienci[indeks].przedsiebiorstwo = entry_firma_klienta.get()
    klient_service.klienci[indeks].x = entry_x_klienta.get()
    klient_service.klienci[indeks].y = entry_y_klienta.get()

    odswiez_liste_klientow()

    entry_imie_klienta.delete(0, tk.END)
    entry_nazwisko_klienta.delete(0, tk.END)
    entry_adres_klienta.delete(0, tk.END)
    entry_firma_klienta.delete(0, tk.END)
    entry_x_klienta.delete(0, tk.END)
    entry_y_klienta.delete(0, tk.END)

    button_dodaj_klienta.config(
        text="Dodaj klienta",
        command=dodaj_klienta
    )


def pokaz_klientow_przedsiebiorstwa():
    nazwa_przedsiebiorstwa = entry_wyszukaj_przedsiebiorstwo.get()

    listbox_wyniki.delete(0, tk.END)

    for klient in klient_service.pobierz_wszystkich():
        if klient.przedsiebiorstwo == nazwa_przedsiebiorstwa:
            listbox_wyniki.insert(tk.END, klient)


def pokaz_pracownikow_przedsiebiorstwa():
    nazwa_przedsiebiorstwa = entry_wyszukaj_przedsiebiorstwo.get()

    listbox_wyniki.delete(0, tk.END)

    for pracownik in pracownik_service.pobierz_wszystkich():
        if pracownik.przedsiebiorstwo == nazwa_przedsiebiorstwa:
            listbox_wyniki.insert(tk.END, pracownik)


root = tk.Tk()

root.title("System przedsiębiorstw wodociągowych")
root.geometry("1300x900")

service = PrzedsiebiorstwoService()
pracownik_service = PracownikService()
klient_service = KlientService()


label_tytul = tk.Label(
    root,
    text="System przedsiębiorstw wodociągowych",
    font=("Arial", 18, "bold")
)
label_tytul.pack(pady=20)


ramka_glowna = tk.Frame(root)
ramka_glowna.pack(pady=10)
ramka_dol = tk.Frame(root)
ramka_dol.pack(pady=5)


ramka_formularz = tk.Frame(ramka_glowna)
ramka_formularz.grid(row=0, column=0, padx=20)


ramka_lista = tk.Frame(ramka_glowna)
ramka_lista.grid(row=0, column=1, padx=20)


ramka_pracownicy = tk.Frame(ramka_glowna)
ramka_pracownicy.grid(row=0, column=2, padx=20)



# FORMULARZ PRZEDSIĘBIORSTWA

label_formularz = tk.Label(
    ramka_formularz,
    text="Formularz przedsiębiorstwa",
    font=("Arial", 12, "bold")
)
label_formularz.grid(row=0, column=0, columnspan=2, pady=10)

label_nazwa = tk.Label(ramka_formularz, text="Nazwa:")
entry_nazwa = tk.Entry(ramka_formularz)

label_miasto = tk.Label(ramka_formularz, text="Miasto:")
entry_miasto = tk.Entry(ramka_formularz)

label_liczba_klientow = tk.Label(ramka_formularz, text="Liczba klientów:")
entry_liczba_klientow = tk.Entry(ramka_formularz)

label_x_przedsiebiorstwa = tk.Label(ramka_formularz, text="X:")
entry_x_przedsiebiorstwa = tk.Entry(ramka_formularz)

label_y_przedsiebiorstwa = tk.Label(ramka_formularz, text="Y:")
entry_y_przedsiebiorstwa = tk.Entry(ramka_formularz)

label_nazwa.grid(row=1, column=0, sticky="w")
entry_nazwa.grid(row=1, column=1)

label_miasto.grid(row=2, column=0, sticky="w")
entry_miasto.grid(row=2, column=1)

label_liczba_klientow.grid(row=3, column=0, sticky="w")
entry_liczba_klientow.grid(row=3, column=1)

label_x_przedsiebiorstwa.grid(row=4, column=0, sticky="w")
entry_x_przedsiebiorstwa.grid(row=4, column=1)

label_y_przedsiebiorstwa.grid(row=5, column=0, sticky="w")
entry_y_przedsiebiorstwa.grid(row=5, column=1)

button_dodaj = tk.Button(
    ramka_formularz,
    text="Dodaj przedsiębiorstwo",
    command=dodaj_przedsiebiorstwo
)
button_dodaj.grid(row=6, column=0, columnspan=2, pady=10)

button_usun = tk.Button(
    ramka_formularz,
    text="Usuń przedsiębiorstwo",
    command=usun_przedsiebiorstwo
)
button_usun.grid(row=7, column=0, columnspan=2, pady=5)


button_edytuj = tk.Button(
    ramka_formularz,
    text="Edytuj przedsiębiorstwo",
    command=edytuj_przedsiebiorstwo
)
button_edytuj.grid(row=8, column=0, columnspan=2, pady=5)



# LISTA PRZEDSIĘBIORSTW

label_lista = tk.Label(
    ramka_lista,
    text="Lista przedsiębiorstw",
    font=("Arial", 12, "bold")
)
label_lista.grid(row=0, column=0, pady=10)

listbox_przedsiebiorstwa = tk.Listbox(
    ramka_lista,
    width=45,
    height=2
)
listbox_przedsiebiorstwa.grid(row=1, column=0)


# PRACOWNICY

label_pracownicy = tk.Label(
    ramka_pracownicy,
    text="Pracownicy",
    font=("Arial", 12, "bold")
)
label_pracownicy.grid(row=0, column=0, columnspan=2, pady=10)

label_imie = tk.Label(ramka_pracownicy, text="Imię:")
entry_imie = tk.Entry(ramka_pracownicy)

label_nazwisko = tk.Label(ramka_pracownicy, text="Nazwisko:")
entry_nazwisko = tk.Entry(ramka_pracownicy)

label_stanowisko = tk.Label(ramka_pracownicy, text="Stanowisko:")
entry_stanowisko = tk.Entry(ramka_pracownicy)

label_firma_pracownika = tk.Label(ramka_pracownicy, text="Przedsiębiorstwo:")
entry_firma_pracownika = tk.Entry(ramka_pracownicy)
label_x_pracownika = tk.Label(ramka_pracownicy, text="X:")
entry_x_pracownika = tk.Entry(ramka_pracownicy)

label_y_pracownika = tk.Label(ramka_pracownicy, text="Y:")
entry_y_pracownika = tk.Entry(ramka_pracownicy)

label_imie.grid(row=1, column=0, sticky="w")
entry_imie.grid(row=1, column=1)

label_nazwisko.grid(row=2, column=0, sticky="w")
entry_nazwisko.grid(row=2, column=1)

label_stanowisko.grid(row=3, column=0, sticky="w")
entry_stanowisko.grid(row=3, column=1)

label_firma_pracownika.grid(row=4, column=0, sticky="w")
entry_firma_pracownika.grid(row=4, column=1)



label_y_pracownika.grid(row=6, column=0, sticky="w")
entry_y_pracownika.grid(row=6, column=1)



button_dodaj_pracownika = tk.Button(
    ramka_pracownicy,
    text="Dodaj pracownika",
    command=dodaj_pracownika
)
button_dodaj_pracownika.grid(row=7, column=0, columnspan=2, pady=5)


button_usun_pracownika = tk.Button(
    ramka_pracownicy,
    text="Usuń pracownika",
    command=usun_pracownika
)

button_usun_pracownika.grid(row=8, column=0, columnspan=2, pady=5)


button_edytuj_pracownika = tk.Button(
    ramka_pracownicy,
    text="Edytuj pracownika",
    command=edytuj_pracownika
)
button_edytuj_pracownika.grid(row=9, column=0, columnspan=2, pady=5)


listbox_pracownicy = tk.Listbox(
    ramka_pracownicy,
    width=35,
    height=2
)
listbox_pracownicy.grid(row=10, column=0, columnspan=2, pady=5)

label_x_pracownika.grid(row=5, column=0, sticky="w")
entry_x_pracownika.grid(row=5, column=1)

label_y_pracownika.grid(row=6, column=0, sticky="w")
entry_y_pracownika.grid(row=6, column=1)



# KLIENCI

ramka_klienci = tk.Frame(ramka_dol)
ramka_klienci.grid(row=0, column=0, padx=20)

label_klienci = tk.Label(
    ramka_klienci,
    text="Klienci",
    font=("Arial", 12, "bold")
)
label_klienci.grid(row=0, column=0, columnspan=2, pady=10)

label_imie_klienta = tk.Label(ramka_klienci, text="Imię:")
entry_imie_klienta = tk.Entry(ramka_klienci)

label_nazwisko_klienta = tk.Label(ramka_klienci, text="Nazwisko:")
entry_nazwisko_klienta = tk.Entry(ramka_klienci)

label_adres_klienta = tk.Label(ramka_klienci, text="Adres:")
entry_adres_klienta = tk.Entry(ramka_klienci)

label_firma_klienta = tk.Label(ramka_klienci, text="Przedsiębiorstwo:")
entry_firma_klienta = tk.Entry(ramka_klienci)

label_x_klienta = tk.Label(ramka_klienci, text="X:")
entry_x_klienta = tk.Entry(ramka_klienci)

label_y_klienta = tk.Label(ramka_klienci, text="Y:")
entry_y_klienta = tk.Entry(ramka_klienci)

label_imie_klienta.grid(row=1, column=0, sticky="w")
entry_imie_klienta.grid(row=1, column=1)

label_nazwisko_klienta.grid(row=2, column=0, sticky="w")
entry_nazwisko_klienta.grid(row=2, column=1)

label_adres_klienta.grid(row=3, column=0, sticky="w")
entry_adres_klienta.grid(row=3, column=1)

label_firma_klienta.grid(row=4, column=0, sticky="w")
entry_firma_klienta.grid(row=4, column=1)

label_x_klienta.grid(row=5, column=0, sticky="w")
entry_x_klienta.grid(row=5, column=1)

label_y_klienta.grid(row=6, column=0, sticky="w")
entry_y_klienta.grid(row=6, column=1)

button_dodaj_klienta = tk.Button(
    ramka_klienci,
    text="Dodaj klienta",
    command=dodaj_klienta
)
button_dodaj_klienta.grid(row=7, column=0, columnspan=2, pady=5)

button_usun_klienta = tk.Button(
    ramka_klienci,
    text="Usuń klienta",
    command=usun_klienta
)
button_usun_klienta.grid(row=8, column=0, columnspan=2, pady=5)


button_edytuj_klienta = tk.Button(
    ramka_klienci,
    text="Edytuj klienta",
    command=edytuj_klienta
)
button_edytuj_klienta.grid(row=9, column=0, columnspan=2, pady=5)


listbox_klienci = tk.Listbox(
    ramka_klienci,
    width=70,
    height=2
)
listbox_klienci.grid(row=10, column=0, columnspan=2, pady=5)





# WYSZUKIWANIE

ramka_wyniki = tk.Frame(ramka_dol)
ramka_wyniki.grid(row=0, column=1, padx=20)

label_wyszukaj = tk.Label(
    ramka_wyniki,
    text="Wyszukaj dane przedsiębiorstwa",
    font=("Arial", 12, "bold")
)
label_wyszukaj.grid(row=0, column=0, columnspan=4, pady=5)

label_wyszukaj_przedsiebiorstwo = tk.Label(
    ramka_wyniki,
    text="Nazwa przedsiębiorstwa:"
)
label_wyszukaj_przedsiebiorstwo.grid(row=1, column=0, sticky="w")

entry_wyszukaj_przedsiebiorstwo = tk.Entry(ramka_wyniki)
entry_wyszukaj_przedsiebiorstwo.grid(row=1, column=1)

button_pokaz_klientow = tk.Button(
    ramka_wyniki,
    text="Pokaż klientów",
    command=pokaz_klientow_przedsiebiorstwa
)
button_pokaz_klientow.grid(row=1, column=2, padx=5)

button_pokaz_pracownikow = tk.Button(
    ramka_wyniki,
    text="Pokaż pracowników",
    command=pokaz_pracownikow_przedsiebiorstwa
)
button_pokaz_pracownikow.grid(row=1, column=3, padx=5)

listbox_wyniki = tk.Listbox(
    ramka_wyniki,
    width=80,
    height=2
)
listbox_wyniki.grid(row=2, column=0, columnspan=4, pady=10)


root.mainloop()