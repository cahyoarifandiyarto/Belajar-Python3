fruits = ["Apel", "Nanas", "Alpukat", "Jeruk", "Pepaya", "Semangka"]
print("Daftar buah-buahan", fruits)

# Akses List dengan index
print("Saya suka buah", fruits[3])

# Memotong List
print("Buah favorite", fruits[1:5]) # -> Index ke 1 sampai dengan index sebelum 5

# Merubah nilai List
print("Sebelum terjadi perubahan =>", fruits)
fruits[2] = "Anggur"
print("Setelah terjadi perubahan =>", fruits)

# NB : Terjadi perubahan pada variable asli, karena kita tidak meng-copy nilai nya

# Copy list ke variable baru
print("Sebelum di copy =>", fruits)
oldFruits = fruits[:]
oldFruits[1] = "Rambutan"
print("Sesudah di copy dan terjadi perubahan =>", oldFruits)
print("Variable asli =>", fruits)

# NB : Variable yang lama tidak terjadi perubahan, perubahan hanya terjadi pada variable yang di copy

# Methods untuk menambahkan nilai baru ke List
print("Sebelum di append =>", fruits)
fruits.append("Pisang")
print("Sesudh di append =>", fruits)

# Function untuk menghitung nilai yang ada pada list
nilaiList = len(fruits)
print("Panjang nilai yang ada di list berjumlah", nilaiList)

# NB : Function len dimulai dihitung dari 1