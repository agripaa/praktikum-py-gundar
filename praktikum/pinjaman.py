def main():
    gaji = int(input("Masukkan gaji Anda: "))
    time = int(input("Lama bekerja (tahun): "))

    if gaji >= 3000000 and time >= 3:
        print("Anda terkualifikasi untuk menerima pinjaman!")
    else:
        print("Anda tidak terkualifikasi untuk menerima pinjaman!")


if __name__ == "__main__":
    main()
