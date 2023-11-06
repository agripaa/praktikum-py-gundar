def main():
    # Variabel untuk menyimpan karakter-karakter yang terdapat dalam string yang diinput pengguna
    karakter_list = []
    # Variabel untuk menyimpan banyaknya karakter yang terdapat dalam string yang diinput pengguna
    banyak_karakter = []

    # [1] Minta pengguna memasukkan sebuah teks dengan prompt 'Masukkan sebuah teks: ' dan simpan dalam sebuah variabel
    input_string = input("Masukkan sebuah teks: ")

    # [2] Gunakan method lower untuk mengonversi semua karakter ke huruf kecil.
    input_string = input_string.lower()

    # [3] Gunakan struktur loop untuk mengiterasi string input dari indeks 0 hingga terakhir.
    for char in input_string:
        # Di dalam loop ini juga terdapat loop yang mengiterasi karakter_list dan menguji masing-masing karakter dalam karakter_list
        # dengan karakter dari input_string
        found = False
        for i in range(len(karakter_list)):
            if karakter_list[i] == char:
                banyak_karakter[i] += 1
                found = True
                break
        if not found:
            karakter_list.append(char)
            banyak_karakter.append(1)

    # [4] Cari jumlah terbanyak pada banyak_karakter dan simpan indeksnya
    indeks_terbanyak = 0
    for i in range(1, len(banyak_karakter)):
        if banyak_karakter[i] > banyak_karakter[indeks_terbanyak]:
            indeks_terbanyak = i

    # [5] Tampilkan karakter terbanyak. Gunakan indeks yang didapat pada [4]
    karakter_terbanyak = karakter_list[indeks_terbanyak]
    print("Karakter terbanyak:  " + karakter_terbanyak)


# Panggil fungsi main
main()
