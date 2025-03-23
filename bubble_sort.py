def bubble_sort(dizi):
    n = len(dizi)
    for i in range(n):
        swapped = False  # Optimizasyon için swap kontrolü
        for j in range(0, n-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]  # Swap işlemi
                swapped = True
        if not swapped:  # Hiç swap yapılmadıysa liste sıralıdır
            break
    return dizi
