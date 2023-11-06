A = {2, 5, 6, 9, -3, -1}
B = {0, 2, 4, 5, -1}
# gabungan A dan B
A_u_B = A.union(B)
#  Irisan A dan B
A_n_B = A.intersection(B)
# Selisih A dan B
A_min_B = A - B
# Selisih B dan A
B_min_A = B - A

print(f"Gabungan : {A_u_B}")
print(f"irisan : {A_n_B}")
print(f"Selisih A - B : {A_min_B}")
print(f"Selisih B - A : {B_min_A}")
