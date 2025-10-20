buah_buahan = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000,
}
print ("Harga jeruk: Rp", buah_buahan.get["Jeruk"])

buah_buahan["Mangga"]=12000
print ("\nBuah-buahan:", (buah_buahan))

buah_buahan["Anggur"]=20000
print ("\nBuah-buahan:", (buah_buahan))

del buah_buahan["Jeruk"]
print ("\nBuah-buahan:", (buah_buahan))