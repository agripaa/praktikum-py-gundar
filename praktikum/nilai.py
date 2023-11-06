def nilai():
    result, counts = 0, 0
    for i in range(3):
        counts = int(input(f"Masukkan nilai ujian {i+1}: "))
        result += counts
    rata2 = result / 3
    print(f"Rata-rata nilai ujian: {rata2}")


nilai()
