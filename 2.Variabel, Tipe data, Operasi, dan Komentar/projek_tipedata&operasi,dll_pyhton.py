# langkah 1
jamtidur = float(input("jumlah jam tidur? "))
jamkerja = float(input("jumlah jam kerja? "))
jamsantai = float(input("jumlah jam santai? "))

jamtersedia = 24.0 - jamtidur - jamkerja - jamsantai - 3.0
print(f" {jamtersedia}")

# langkah 2
jamsantaiWeekday = float(input("jam santai waktu hari biasa? "))
jamsantaiWeekend = float(input("jam santai waktu akhir pekan? "))

tersediaWeekday = 24.0 - jamtidur - jamkerja - jamsantaiWeekday - 3.0
tersediaWeekend = 24.0 - jamtidur - jamsantaiWeekend - 3.0

totaljamTersediaMingguan = 5 * tersediaWeekday + 2 * tersediaWeekend

print(f"jumlah total tersedia mingguan : {totaljamTersediaMingguan}")
