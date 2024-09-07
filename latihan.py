nama = "Ahmad Azizul Airf"
nim = 240441100060
ipk = 4.00
mahasiswa = True

print("nama saya adalah", nama)
# Ini adalah forrmat natural (tipe data sama)
print("nim saya adalah", nim)
print("Impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

#ini adalah format string (tipe data diubah menjadi string)
print(f"nama saya adalah {nama}")

# program dinamis string
nama_panjang = str(input("nama saya adalah :"))

# program dinamis integer
nilai = int(input("nilai saya adalah :"))

# nilai
nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

# total
penjumlahan = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f"hasil dari penjumlahan dari nilai matematika dan kimia adalah : {penjumlahan}")
print(f"hasil dari penjumlahan dari nilai matematika dan kimia adalah : {pengurangan}")
print(f"hasil dari penjumlahan dari nilai matematika dan kimia adalah : {perkalian}")
print(f"hasil dari penjumlahan dari nilai matematika dan kimia adalah : {pembagian}")

usia_masuk_kuliah = int(input("Berapa usisa anda waktu masuk kuliah ? "))
lama_kuliah = int(input("Berapa lama anda kuliah ? "))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f"Saat ini, saya {nama} berumur {usia_saat_ini}")
print(f"saya {nama} akan lulus pada tahun {tahun_lulus}")
