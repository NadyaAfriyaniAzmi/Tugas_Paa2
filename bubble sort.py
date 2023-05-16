def bubble_sort(arr):
    n = len(arr)

    # Melintasi semua elemen array
    for i in range(n - 1):
        # Elemen terakhir sebanyak i sudah berada pada posisi yang tepat
        for j in range(0, n - i - 1):
            # Tukar jika elemen yang ditemukan lebih besar dari elemen berikutnya
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Contoh penggunaan
arr = [27, 34, 6, 2, 17, 11, 98]

print("Array asli:", arr)
bubble_sort(arr)
print("Array yang sudah diurutkan:", arr)


