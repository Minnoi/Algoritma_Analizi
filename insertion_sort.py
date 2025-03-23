def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]  # Yerleştirilecek eleman
        j = i - 1

        # Key'den büyük elemanları sağa kaydır
        while j >= 0 and key < dizi[j]:
            dizi[j + 1] = dizi[j]
            j -= 1
        dizi[j + 1] = key  # Key'i doğru pozisyona yerleştir
    return dizi
