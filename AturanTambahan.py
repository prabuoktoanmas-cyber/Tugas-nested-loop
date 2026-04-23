total_belanja =int(input("Masukkan Total Belanja: "))
ongkir =int(input("Masukkan Ongkir: "))
status_member =input("Apakah Member Premium? True/False: ")
hari =input("Masukkan Hari: ")

status_member = True if status_member == "True" else False 

cashback = 1

if status_member :
    cashback += 5
elif hari.lower() == "Sabtu":
    cashback += 3  
elif cashback > 15:
    cashback = 15
    
total_pembayaran = total_belanja + ongkir
jumlah_cashback = total_pembayaran * cashback / 100

print("Total Pembayaran: ", total_pembayaran)
print("Persentase cashback: ", cashback,"%")
print("Jumlah cashback: ", jumlah_cashback)
