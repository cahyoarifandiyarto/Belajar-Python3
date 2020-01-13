# For Loop untuk mengeluarkan nilai pada List

fruits = ["Apel", "Nanas", "Jeruk", "Semangka", "Alpukat", "Anggur"]
siswa = ["Mahmud", "Cahyo", "Arif", "Eko", "Ahmad", "Dahlan"]

for fruit in fruits:
    print(fruit)

multiDimensiList = [fruits, siswa]
print("Multi Dimensi List =>",multiDimensiList)

# For Loop multi dimensi pada list
for daftar in multiDimensiList:
    print("Step 1 =>",daftar)
    for nilai in daftar:
        print("Step 2 =>",nilai)


# For else, Range, Break

# Contoh looping dengan range
for i in range(1, 6):
    print("Nilai:",i) # Mencetak angka 1 - 5

# Contoh mencari nilai di looping
number = 15

for i in range(0, 20):
    if i is number:
        print("Angka", number, "ditemukan")
        break # Proses berhenti jika angka ditemukan
else:
    print("Angka", number, "tidak ditemukan")


# Continue

angka = 5
for i in range(1, 11):
    if i is angka:
        print("Angka", angka, "ditemukan")
        continue # Melanjutkan pencarian walaupun sudah ditemukan
else:
    print("Angka tidak ditemukan")

# NB : break (berhenti jika kondisi tercapai), continue (melanjutkan perulangan walaupun kondisi sudah tercapai)