angka = 0

# Selama nilai nya kurang dari 11 maka print secara terus menerus
while angka < 11:
    print("Nilai sekarang adalah:", angka)
    angka = angka + 1


# Selama nilai nya true maka lakukan perulangana secara terus menerus
number = 0
start = True

while start:
    print("While teruss selama", number)
    if number is 20: # Jika sudah sampai 20
        start = False # Maka variable start di update menjadi False
        print("STOP Di Angka", number) # Print STOP
    number += 1 # 0 = 0 + 1 -> 1 = 1 + 1 (Melakukan perulangan secara terus menerus)

# While dengan keywords break
mulai = 0
while mulai < 10:
    print("While selama", mulai)
    if (mulai is 6):
        print("Stop diangka", mulai)
        break
    mulai += 1