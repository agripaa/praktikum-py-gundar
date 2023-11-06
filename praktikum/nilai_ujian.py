def main():
    JUMLAH_UJIAN = 3
    rata_rata_mahasiswa = []

    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

    for mahasiswa in range(1, jumlah_mahasiswa + 1):
        total_nilai = 0

        print("=" * 50)
        print(f"Masukkan nilai ujian untuk mahasiswa {mahasiswa}")
        print("-" * 50)

        for ujian in range(1, JUMLAH_UJIAN + 1):
            nilai = float(input(f"Masukkan nilai ujian ke-{ujian}: "))
            total_nilai += nilai

        rata_rata = total_nilai / JUMLAH_UJIAN
        rata_rata_mahasiswa.append(rata_rata)

    print("=" * 50)
    for i, rata_rata in enumerate(rata_rata_mahasiswa):
        print(f"Rata-rata ujian mahasiswa {i + 1}: {rata_rata:.2f}")


# Panggil fungsi main
main()
