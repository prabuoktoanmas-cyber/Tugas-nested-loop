belanja = int(input("Masukkan Belanja: "))

if belanja >= 400000:
    print("Mendapatkan Gratis Ongkir 100% ")
elif belanja >= 250000:
    print("Mendapatkan Potongan Ongkir 75% ")
elif belanja >= 150000:
    print("Mendapatkan Potongan Ongkir 50% ")
else:
    print("Tidak ada potongan ongkir")
