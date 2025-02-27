import analiza_tekstu as a

def palindrom_test(pal):
    # Usunięcie spacji i zamiana na małe litery
    pal = ''.join(pal.lower().split())

    # Sprawdzenie, czy tekst czytany od tyłu jest taki sam
    return pal == pal[::-1]


def najczestsze_slowa(text, n=5):
    # Zamiana na małe litery i podział na słowa
    text = text.lower().split()

    # Tworzenie słownika częstości słów
    czestotliwosc = {}
    for slowo in text:
        czestotliwosc[slowo] = czestotliwosc.get(slowo, 0) + 1

    # Posortowanie słów według liczby wystąpień (od największej)
    najczestsze = sorted(czestotliwosc.items(), key=lambda x: x[1], reverse=True)

    return najczestsze[:n]  # Zwrócenie n najczęstszych słów

def raport_gen(text):
    liczba_slow = a.licz_slowa(text)
    liczba_znakow = a.licz_znaki(text)
    liczba_unikalnych_slow = a.wez_unikalne_slowa(text)

    wynik = f"Wyniki analizy:\nLiczba słów: {liczba_slow}\nLiczba znaków: {liczba_znakow}\nLiczba unikalnych słów: {liczba_unikalnych_slow} \nCzy palindrom: {palindrom_test(text)} \nNajczęść 5 używanych słów:{najczestsze_slowa(text)}"
    return wynik
