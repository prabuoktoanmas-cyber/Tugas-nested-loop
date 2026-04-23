cashback = int(input("Masukkan Cashback: "))

if cashback >= 300000:
    print("Mendapatkan Cashback 10% ")
elif cashback >= 250000:
    print("Mendapatkan Cashback 7% ")
elif cashback >= 100000:
    print("Mendapatkan Cashback 5% ")
else :
    print("Tidak ada Cashback")
