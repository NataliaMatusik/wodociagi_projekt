import folium


def czy_poprawne_wspolrzedne(x, y):
    try:
        float(x)
        float(y)
        return True
    except ValueError:
        return False


def dodaj_marker_z_etykieta(mapa, x, y, popup, etykieta, kolor):
    folium.Marker(
        location=[float(x), float(y)],
        popup=popup,
        icon=folium.Icon(color=kolor)
    ).add_to(mapa)

    folium.Marker(
        location=[float(x), float(y)],
        icon=folium.DivIcon(
            html=f"""
            <div style="
                font-size: 12px;
                font-weight: bold;
                color: black;
                white-space: nowrap;
                transform: translate(20px, -10px);
            ">
                {etykieta}
            </div>
            """
        )
    ).add_to(mapa)


def generuj_mape(przedsiebiorstwa, klienci, pracownicy):
    mapa = folium.Map(
        location=[52.0, 19.0],
        zoom_start=6
    )

    for przedsiebiorstwo in przedsiebiorstwa:
        if czy_poprawne_wspolrzedne(przedsiebiorstwo.x, przedsiebiorstwo.y):
            dodaj_marker_z_etykieta(
                mapa,
                przedsiebiorstwo.x,
                przedsiebiorstwo.y,
                f"Przedsiębiorstwo: {przedsiebiorstwo.nazwa}",
                f"Firma: {przedsiebiorstwo.nazwa}",
                "blue"
            )

    for klient in klienci:
        if czy_poprawne_wspolrzedne(klient.x, klient.y):
            dodaj_marker_z_etykieta(
                mapa,
                klient.x,
                klient.y,
                f"Klient: {klient.imie} {klient.nazwisko}",
                f"Klient: {klient.imie} {klient.nazwisko}",
                "green"
            )

    for pracownik in pracownicy:
        if czy_poprawne_wspolrzedne(pracownik.x, pracownik.y):
            dodaj_marker_z_etykieta(
                mapa,
                pracownik.x,
                pracownik.y,
                f"Pracownik: {pracownik.imie} {pracownik.nazwisko}",
                f"Pracownik: {pracownik.imie} {pracownik.nazwisko}",
                "red"
            )

    mapa.save("mapa.html")