def jumlah_list(input_list):
    # [1] Buat dua variabel akumulator untuk menyimpan jumlah elemen-elemen genap dan jumlah elemen-elemen ganjil
    total_genap = 0
    total_ganjil = 0

    # [2] Gunakan struktur loop untuk mengiterasi indeks dari input_list
    # Gunakan juga struktur seleksi dengan modulus untuk menguji indeks genap dan ganjil dan akumulasikan
    # elemen dengan indeks tersebut ke variabel akumulator yang sesuai
    for i in range(len(input_list)):
        if i % 2 == 0:  # indeks genap
            total_genap += input_list[i]
        else:  # indeks ganjil
            total_ganjil += input_list[i]

    # [3] Tampilkan jumlah elemen-elemen tersebut dengan teks:
    print(f"Total elemen indeks ganjil: {total_ganjil}")
    print(f"Total elemen indeks genap: {total_genap}")
