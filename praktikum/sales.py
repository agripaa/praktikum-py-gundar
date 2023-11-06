penjualan = int(input("Masukkan total penjualan rokok: "))


def info_bonus(penjualan):
    total = penjualan * 1000
    bonus = {
        penjualan < 1000: 0,
        penjualan >= 1000: (20 / 100) * total,
        penjualan >= 2000: (25 / 100) * total,
        penjualan >= 3000: (30 / 100) * total,
    }

    return bonus.get(True, 0)


get_bonus = info_bonus(penjualan)
print(f"Bonus yang di dapatkan seles : {get_bonus:,.2f}")
