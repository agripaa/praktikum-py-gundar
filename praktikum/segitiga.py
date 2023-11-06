def main():
    count = int(input("Masukkan sebuah angka: "))
    for i in range(count, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()
