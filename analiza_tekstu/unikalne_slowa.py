def wez_unikalne_slowa(text):
    slowa = text.lower().split()
    slowa_bez_interpunkcji = [slowo.strip(".,!?;:") for slowo in slowa]
    unikalne_slowa = set(slowa_bez_interpunkcji)
    return len(unikalne_slowa)