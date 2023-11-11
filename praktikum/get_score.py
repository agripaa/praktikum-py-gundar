# Fungsi ini meminta pengguna memasukkan rangkaian angka-angka
# dan menggunakan sentinel untuk mengakhiri input angka.
# Fungsi ini mengembalikan sebuah list yang berisi angka-angka yang diinput pengguna
def get_score():
    # Buat list kosong untuk menyimpan angka-angka yang dimasukkan pengguna
    score_list = []

    # [1] Minta pengguna memasukkan skor berupa angka
    # [2] Tulis struktur loop yang meminta pengguna memasukkan angka-angka
    # Gunakan sentinel dengan angka negatif untuk mengakhiri input
    while True:
        skor = int(input("Masukkan skor (masukkan angka negatif untuk menyudahi): "))
        if skor < 0:
            break
        else:
            score_list.append(skor)

    return score_list
