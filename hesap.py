def en_buyuk_ninci_sayi(liste, n):
    sirali_liste = sorted(liste, reverse=True)  # Listeyi büyükten küçüğe sırala
    if n <= len(sirali_liste):
        return sirali_liste[n - 1]  # Listenin n. büyük elemanını bul ve döndür
    else:
        return "Liste belirtilen indekse sahip değil"

# Örnek liste
ornek_liste = [5, 18, 3, 25, 47, 12, 35, 9, 10, 6, 22, 14, 33, 29, 40, 1, 8, 16, 7, 11]
n = 5  # Bulmak istediğiniz sıra numarası (n)

en_buyuk_ninci = en_buyuk_ninci_sayi(ornek_liste, n)
if isinstance(en_buyuk_ninci, int):
    print(f"{n}. en büyük sayı:", en_buyuk_ninci)
else:
    print(en_buyuk_ninci)
