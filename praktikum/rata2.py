def main():
    total = 0
    count = 0

    while True:
        num = int(
            input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): ")
        )
        if num < 0:
            break
        total += num
        count += 1

    if count > 0:
        average = total / count
    else:
        average = 0

    print(f"Rata-rata angka yang dimasukkan: {average}")


if __name__ == "__main__":
    main()
