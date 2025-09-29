nilai = set({3,6,9,2,5,7})
print("himpunan awal:", nilai)

nilai.update ({1, 4, 8, 10})
print("setelah penambahan:", nilai)

for i in [1, 3, 4, 5, 7, 8, 10]:
    nilai.remove (i)
print("setelah dihapus:", nilai)

