namaPacar = 'sintya'

def gantiPacar(pacarBaru):
    global namaPacar # Global variable
    namaPacar = pacarBaru
    print("Nama pacar saya sekarang yaitu", namaPacar)

gantiPacar("Billa")
print("Nama pacar saya", namaPacar)