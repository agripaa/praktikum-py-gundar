def main():
    arr = []
    count1 = int(input("Masukkan angka 1: "))
    count2 = int(input("Masukkan angka 2: "))
    count3 = int(input("Masukkan angka 3: "))

    arr.append(count1)
    arr.append(count2)
    arr.append(count3)
    maxArr = max(arr)
    print(f"Angka terbesar =  {maxArr}")


main()


# simple code

# def main():
#     arr = []
#     for i in range(1, 4):
#         count = int(input(f"Masukkan angka {i}: "))
#         arr.append(count)

#     maxArr = max(arr)
#     print(f"Angka terbesar =  {maxArr}")

# if __name__ == "__main__":
#     main()
