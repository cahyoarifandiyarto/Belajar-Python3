# Fungsi tanpa parameter
def printMessage():
    print("Selamat belajar python!!")

# Fungsi dengan parameter
def sayHello(name):
    printMessage() # Memanggil fungsi di dalam fungsi
    print("Semangat belajar nya ya", name, "!!!")

# Memanggil Fungsi
sayHello("Cahyo Arif Andiyarto")

# Fungsi dengan return value
def kuadrat(x):
    hasil = x**2
    print("Nilai kuadrat dari", x, "adalah", hasil)
    return hasil # Mengembalikan nilai

a = kuadrat(2)
print(a)

# Fungsi dengan return value dan multiple arguments/parameter
def penjumlahan(x, y):
    hasil = x + y
    print("Hasil penjumlahan dari", x, "+", y, "=", hasil)
    return hasil
b = penjumlahan(2, 2)
print(b)