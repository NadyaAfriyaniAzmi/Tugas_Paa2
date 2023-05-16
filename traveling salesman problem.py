import itertools


def hitung_jarak(kota1, kota2):
    # Menghitung jarak Euclidean antara dua kota
    x1, y1 = kota1
    x2, y2 = kota2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def tsp(kota):
    # Menghasilkan semua permutasi yang mungkin dari kota-kota
    permutasi = itertools.permutations(kota)

    # Inisialisasi variabel untuk melacak rute terbaik dan panjangnya
    rute_terbaik = None
    jarak_terbaik = float('inf')

    # Melakukan iterasi pada semua permutasi dan menghitung jaraknya
    for permutasi_kota in permutasi:
        jarak = 0

        # Menghitung jarak total untuk permutasi saat ini
        for i in range(len(permutasi_kota) - 1):
            jarak += hitung_jarak(permutasi_kota[i], permutasi_kota[i + 1])

        # Menambahkan jarak dari kota terakhir kembali ke kota awal
        jarak += hitung_jarak(permutasi_kota[-1], permutasi_kota[0])

        # Memperbarui rute terbaik jika ditemukan jarak yang lebih pendek
        if jarak < jarak_terbaik:
            rute_terbaik = permutasi_kota
            jarak_terbaik = jarak

    return rute_terbaik, jarak_terbaik


# Contoh penggunaan
kota = [(0, 3), (2, 7), (1, 1), (9, 2), (0, 6)]

rute_terbaik, jarak_terbaik = tsp(kota)

print("Rute terbaik:", rute_terbaik)
print("Jarak terbaik:", jarak_terbaik)
