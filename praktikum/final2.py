def main():
    while True:
        try:
            num1 = int(input("Masukkan angka 1: "))
            num2 = int(input("Masukkan angka 2: "))
            total = num1 + num2
            print(f"Jumlah = {total}")
        except ValueError:
            print("Input tidak valid.")
            continue

        choice = input("Masukkan y untuk melanjutkan: ")
        if choice != "y":
            break


if __name__ == "__main__":
    main()
