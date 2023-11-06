def validasi_password(passwd):
    spesial_karakter = ["$", "@", "#", "%"]

    # Variabel-variabel untuk menyimpan hasil pengujian ketentuan. Inisialisasi dengan False.
    panjang_benar = False
    ada_digit = False
    ada_huruf_besar = False
    ada_huruf_kecil = False
    ada_spesial_karakter = False

    # [1] Validasi panjang karakter
    if 6 <= len(passwd) <= 20:
        panjang_benar = True

    # [1] Validasi digit, huruf besar, huruf kecil, dan spesial karakter
    for char in passwd:
        if char.isdigit():
            ada_digit = True
        if char.isupper():
            ada_huruf_besar = True
        if char.islower():
            ada_huruf_kecil = True
        if char in spesial_karakter:
            ada_spesial_karakter = True

    # [2] Jika semua ketentuan terpenuhi, tetapkan variabel nilai_kembali dengan True
    # dan selain itu tetapkan dengan False
    if (
        panjang_benar
        and ada_digit
        and ada_huruf_besar
        and ada_huruf_kecil
        and ada_spesial_karakter
    ):
        nilai_kembali = True
    else:
        nilai_kembali = False

    # [3] Kembalikan variabel nilai_kembali
    return nilai_kembali


# simple code

# def validasi_password(passwd):
#     spesial_karakter = ['$', '@', '#', '%']

#     panjang_benar = 6 <= len(passwd) <= 20
#     ada_digit = any(char.isdigit() for char in passwd)
#     ada_huruf_besar = any(char.isupper() for char in passwd)
#     ada_huruf_kecil = any(char.islower() for char in passwd)
#     ada_spesial_karakter = any(char in spesial_karakter for char in passwd)

#     return panjang_benar and ada_digit and ada_huruf_besar and ada_huruf_kecil and ada_spesial_karakter
