def main():
    seconds = int(input("Masukkan jumlah detik: "))

    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    time_units = []

    if days:
        time_units.append(f"{days} hari")
    if hours:
        time_units.append(f"{hours} jam")
    if minutes:
        time_units.append(f"{minutes} menit")
    if seconds:
        time_units.append(f"{seconds} detik")
    else:
        time_units.append(f"0 detik")

    result = " ".join(time_units)
    print(result)


if __name__ == "__main__":
    main()
