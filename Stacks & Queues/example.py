from collections import deque

# Stacks : Mengeluarkan data yang paling akhir
# Queues: Mengeluarkan data yang paling pertama

# STACKS
data = [1, 2, 3, 4, 5, 6, 7]
print("Data =>", data)
# Menambah data
data.append(8)
print("Menambah data =>", data)
data.append(9)
print("Data masuk lagi =>", data)

# Mengeluarkan data yang paling akhir
dataKeluar = data.pop()
print("Data yang dikeluarkan adalah data ke -", dataKeluar)
print("Data terupdate", data)
# END STACKS

print("="*5)

# QUEUES
data1 = deque([1, 2, 3, 4])
print("Data1 =>", data1)

# Menambah data
data1.append(5)
print("Data masuk =>", data1)
data1.append(6)
print("Data masuk lagi =>", data1)

# Mengeluarkan data yang paling pertama
dataYangKeluar = data1.popleft()
print("Data yang keluar adalah", dataYangKeluar)
print("Data terupdate sekarang adalah", data1)
dataKeluarLagi = data1.popleft()
print("Ada data yang di keluarkan lagi, yaitu data ke ->", dataKeluarLagi)
print("Data paling terupdate sekarang adalah", data1)