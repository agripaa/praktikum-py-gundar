def kali_kartesian(A, B):
    hasil = set()
    for elemen_A in A:
        for elemen_B in B:
            hasil.add((elemen_A, elemen_B))
    return hasil


A = {2, 5}
B = {3, 4}
A_x_B = kali_kartesian(A, B)
print("A x B =", A_x_B)
