import raport_tekstu as rt
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def wybierz_plik():
    sciezka_pliku = filedialog.askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])
    if not sciezka_pliku:
        messagebox.showwarning("Brak pliku", "Nie wybrano pliku!")
        return None

    with open(sciezka_pliku, "r", encoding="utf-8") as plik:
        zawartosc = plik.read()

    return zawartosc


def analiza_i_wyswietl():
    tekst = wybierz_plik()
    if tekst:
        wynik = rt.raport_gen(tekst)
        pole_tekstowe.delete(1.0, tk.END)  # Czyszczenie pola tekstowego
        pole_tekstowe.insert(tk.END, wynik)  # Wstawienie wyników analizy


# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Analiza Tekstu")
root.geometry("500x400")

# Przycisk do wyboru pliku
przycisk_wybierz = tk.Button(root, text="Wybierz plik", command=analiza_i_wyswietl)
przycisk_wybierz.pack(pady=10)

# Pole tekstowe do wyświetlania wyników
pole_tekstowe = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
pole_tekstowe.pack(padx=10, pady=10)

root.mainloop()
