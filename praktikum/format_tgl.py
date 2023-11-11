def main():
    lookup_bulan = [
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ]

    tanggal_input = input("Masukkan tanggal dalam format hh/bb/tttt: ")
    tanggal_list = tanggal_input.split("/")

    if len(tanggal_list) == 3:
        hari = tanggal_list[0]
        bulan = tanggal_list[1].zfill(
            2
        )  # Tambahkan nol di depan bulan jika hanya satu digit
        tahun = tanggal_list[2]

        if 1 <= int(bulan) <= 12:
            nama_bulan = lookup_bulan[int(bulan) - 1]
            print(
                f"{int(hari)} {nama_bulan} {tahun}"
            )  # Mengubah hari ke integer agar nol di depannya tidak hilang
        else:
            print("Anda tidak memasukkan tanggal yang benar.")
    else:
        print("Anda tidak memasukkan tanggal yang benar.")


# Panggil fungsi main
main()
