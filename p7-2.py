stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20,
}
print ("Stock Buku Saat Ini:")
for judul, stok in stok_buku.items():
    print (f"Buku: {judul} - Stok: {stok}")

judul_baru = input ("\nMasukkan Judul buku: ")
stok_baru = int(input("Masukkan Jumlah Stok Buku: "))
                
stok_buku [judul_baru] = stok_baru
print (f"\nBuku {judul_baru} berhasil ditambahkan dengan stok {stok_baru}")

print ("\nStock Buku Saat Ini:")
for judul, stok in stok_buku.items():
    print (f"Buku: {judul} - Stok: {stok}")