# Program ini mengkonversi input tanggal dengan format hh/bb/ttt dari pengguna
# menjadi tanggal dalam format hh nama_bulan tttt (12 Maret 2021)
def main():
    # Gunakan list berikut untuk mendapatkan string nama bulan
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

    # [1] Minta input tanggal dalam bentuk hh/bb/tttt dengan prompt 'Masukkan tanggal dalam format hh/bb/tttt: '
    tanggal_input = input("Masukkan tanggal dalam format hh/bb/tttt: ")

    # [2] Gunakan method split untuk memisahkan tanggal, bulan, dan tahun dan simpan ke sebuah list
    tanggal_list = tanggal_input.split("/")

    # [3] Gunakan struktur seleksi untuk menvalidasi apakah bulan yang dimasukkan antara 1 s.d 12
    # Jika tidak valid, tampilkan: "Anda tidak memasukkan tanggal yang benar."
    # Jika valid, tampilkan tanggal dengan format hh nama_bulan tahun (12 Maret 2021)
    if len(tanggal_list) == 3:
        hari = tanggal_list[0]
        bulan_index = (
            int(tanggal_list[1]) - 1
        )  # Ambil index bulan dari list lookup_bulan
        tahun = tanggal_list[2]

        if 1 <= bulan_index + 1 <= 12:
            nama_bulan = lookup_bulan[bulan_index]
            print(f"{hari} {nama_bulan} {tahun}")
        else:
            print("Anda tidak memasukkan tanggal yang benar.")
    else:
        print("Anda tidak memasukkan tanggal yang benar.")


# Panggil fungsi main
main()
