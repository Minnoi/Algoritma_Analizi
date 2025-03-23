def max_subarray_sum(arr):
    def helper(low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        # Sol, sağ ve ortadan geçen maksimumları bul
        left_max = helper(low, mid)
        right_max = helper(mid + 1, high)
        cross_max = max_crossing_sum(low, mid, high)

        return max(left_max, right_max, cross_max)

    def max_crossing_sum(low, mid, high):
        # Orta noktadan sola doğru maksimum toplam
        left_sum = -float('inf')
        total = 0
        for i in range(mid, low - 1, -1):
            total += arr[i]
            if total > left_sum:
                left_sum = total

        # Orta noktadan sağa doğru maksimum toplam
        right_sum = -float('inf')
        total = 0
        for i in range(mid + 1, high + 1):
            total += arr[i]
            if total > right_sum:
                right_sum = total

        return left_sum + right_sum

    return helper(0, len(arr) - 1)

# Örnek Kullanım
dizi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maksimum Alt Dizi Toplamı:", max_subarray_sum(dizi))  # Çıktı: 6
