# Dictionary : Tipe data key value pair

biodata = {
    "ID": 1,
    "Nama": "Cahyo Arif Andiyarto",
    "Domisili": "Sleman",
    "Pekerjaan": "Mahasiswa",
    "Semester": 2
}

print(biodata)

# Mengakses nilai di dictionary yaitu menggunakan key
id = biodata["ID"]
print("ID ->", id)
nama = biodata["Nama"]
print("ID ->", id, "Nama ->", nama)

# Merubah nilai pada dictionary
print("Sebelum terjadi perubahan ->", biodata["Domisili"])
biodata["Domisili"] = "Sidoarjo"
print("Sesudah terjadi perubahan ->", biodata["Domisili"])