import tkinter as tk
from services.przedsiebiorstwo_service import PrzedsiebiorstwoService
from services.pracownik_service import PracownikService


def dodaj_przedsiebiorstwo():
    nazwa = entry_nazwa.get()
    miasto = entry_miasto.get()
    liczba_klientow = entry_liczba_klientow.get()

    service.dodaj_przedsiebiorstwo(
        nazwa,
        miasto,
        liczba_klientow
    )

    listbox_przedsiebiorstwa.delete(0, tk.END)

    for przedsiebiorstwo in service.pobierz_wszystkie():
        listbox_przedsiebiorstwa.insert(tk.END, przedsiebiorstwo)

    entry_nazwa.delete(0, tk.END)
    entry_miasto.delete(0, tk.END)
    entry_liczba_klientow.delete(0, tk.END)

def usun_przedsiebiorstwo():
    zaznaczenie = listbox_przedsiebiorstwa.curselection()

    if zaznaczenie:
        indeks = zaznaczenie[0]
        service.przedsiebiorstwa.pop(indeks)

        listbox_przedsiebiorstwa.delete(0, tk.END)

        for przedsiebiorstwo in service.pobierz_wszystkie():
            listbox_przedsiebiorstwa.insert(tk.END, przedsiebiorstwo)


def dodaj_pracownika():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    stanowisko = entry_stanowisko.get()
    przedsiebiorstwo = entry_firma_pracownika.get()

    pracownik_service.dodaj_pracownika(
        imie,
        nazwisko,
        stanowisko,
        przedsiebiorstwo
    )

    listbox_pracownicy.delete(0, tk.END)

    for pracownik in pracownik_service.pobierz_wszystkich():
        listbox_pracownicy.insert(tk.END, pracownik)

    entry_imie.delete(0, tk.END)
    entry_nazwisko.delete(0, tk.END)
    entry_stanowisko.delete(0, tk.END)
    entry_firma_pracownika.delete(0, tk.END)


root = tk.Tk()

root.title("System przedsiębiorstw wodociągowych")
root.geometry("1000x700")
service = PrzedsiebiorstwoService()
pracownik_service = PracownikService()


label_tytul = tk.Label(
    root,
    text="System przedsiębiorstw wodociągowych",
    font=("Arial", 18, "bold")
)
label_tytul.pack(pady=20)


ramka_glowna = tk.Frame(root)
ramka_glowna.pack(pady=10)


ramka_formularz = tk.Frame(ramka_glowna)
ramka_formularz.grid(row=0, column=0, padx=20)


ramka_lista = tk.Frame(ramka_glowna)
ramka_lista.grid(row=0, column=1, padx=20)
ramka_pracownicy = tk.Frame(ramka_glowna)
ramka_pracownicy.grid(row=0, column=2, padx=20)


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

label_nazwa.grid(row=1, column=0, sticky="w")
entry_nazwa.grid(row=1, column=1)

label_miasto.grid(row=2, column=0, sticky="w")
entry_miasto.grid(row=2, column=1)

label_liczba_klientow.grid(row=3, column=0, sticky="w")
entry_liczba_klientow.grid(row=3, column=1)

button_dodaj = tk.Button(
    ramka_formularz,
    text="Dodaj przedsiębiorstwo",
    command=dodaj_przedsiebiorstwo
)

button_dodaj.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)

button_usun = tk.Button(
    ramka_formularz,
    text="Usuń przedsiębiorstwo",
    command=usun_przedsiebiorstwo
)

button_usun.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=5
)


label_lista = tk.Label(
    ramka_lista,
    text="Lista przedsiębiorstw",
    font=("Arial", 12, "bold")
)
label_lista.grid(row=0, column=0, pady=10)

listbox_przedsiebiorstwa = tk.Listbox(
    ramka_lista,
    width=50,
    height=15
)

listbox_przedsiebiorstwa.grid(row=1, column=0)

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

label_imie.grid(row=1, column=0, sticky="w")
entry_imie.grid(row=1, column=1)

label_nazwisko.grid(row=2, column=0, sticky="w")
entry_nazwisko.grid(row=2, column=1)

label_stanowisko.grid(row=3, column=0, sticky="w")
entry_stanowisko.grid(row=3, column=1)

label_firma_pracownika.grid(row=4, column=0, sticky="w")
entry_firma_pracownika.grid(row=4, column=1)


button_dodaj_pracownika = tk.Button(
    ramka_pracownicy,
    text="Dodaj pracownika",
    command=dodaj_pracownika
)

button_dodaj_pracownika.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=5
)

listbox_pracownicy = tk.Listbox(
    ramka_pracownicy,
    width=40,
    height=10
)
listbox_pracownicy.grid(row=6, column=0, columnspan=2, pady=10)


root.mainloop()