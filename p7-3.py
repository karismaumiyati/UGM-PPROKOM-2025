print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba": 85,
    "Abi": 90,
    "Abu": 78,
}
print(nilai_mahasiswa)

print("\nMenambahkan Nilai Abe:")
nilai_mahasiswa["Abe"] = 88
print(nilai_mahasiswa)

print("\nMengupdate Nilai Abu:")
nilai_mahasiswa.update["Abe"]=87
print (nilai_mahasiswa)

print("\nMencetak Semua Nilai:")
for nama, nilai in nilai_mahasiswa.items():
    print(f"Nilai {nama} adalah {nilai}")