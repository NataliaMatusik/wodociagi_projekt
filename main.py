import tkinter as tk

root = tk.Tk()

root.title("System przedsiębiorstw wodociągowych")
root.geometry("1000x700")


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


root.mainloop()