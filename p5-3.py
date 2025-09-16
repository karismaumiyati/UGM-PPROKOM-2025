jumlah_nilai = int(input("masukkan jumlah nilai:"))

total = 0
for i in range (jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke- {i+1}:"))
    total += nilai

rata= total / jumlah_nilai

print(f"Rata rata {jumlah_nilai} nilai: {rata} ")
