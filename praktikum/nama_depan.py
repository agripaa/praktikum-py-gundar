def main():
    nama_lengkap = input("Masukkan nama: ")
    nama_split = nama_lengkap.split()

    inisial_nama_depan = nama_split[0][0]
    inisial_nama_belakang = nama_split[1][0]

    print(f"Inisial nama Anda: {inisial_nama_depan}. {inisial_nama_belakang}.")


# Panggil fungsi main
main()
