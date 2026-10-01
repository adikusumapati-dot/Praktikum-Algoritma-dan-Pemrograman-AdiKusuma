import time


def perkalian(angka1, angka2):
  return angka1 * angka2


def pembagian(angka1, angka2):
  return angka1 / angka2


def pertambahan(angka1, angka2):
  return angka1 + angka2


def pengurangan(angka1, angka2):
  return angka1 - angka2


hasil = 0
sistemUtama = True

while sistemUtama:
  print("selamat datang di kalkulator berbasis console")
  time.sleep(2)
  print("setelah ini bisa masukkan 2 angka kemudian pilih jenis operasinya")
  time.sleep(2)

  angka1 = float(input("masukkan angka ke-1: "))
  angka2 = float(input("masukkan angka ke-2: "))

  jenisOperasi = int(
      input(
          "pilih jenis operasi (1 untuk perkalian, 2 untuk pembagian, 3 untuk pertambahan, 4 untuk pengurangan): "
      ))

  if jenisOperasi == 1:
    hasil = perkalian(angka1, angka2)

  elif jenisOperasi == 2:
    if angka2 == 0:
      print("pembagian dengan angka 0 tidak terdefinisi")
      break

    hasil = pembagian(angka1, angka2)

  elif jenisOperasi == 3:
    hasil = pertambahan(angka1, angka2)

  elif jenisOperasi == 4:
    hasil = pengurangan(angka1, angka2)

  else:
    print("maaf kamu salah memasukkan angka pilihan jenis operasi")

  print(f"hasil kalkulator kamu yaitu: {hasil}")

  stop = input("apakah ingin melanjutkan? (y/t) ")

  if stop == "t":
    sistemUtama = False
  elif stop == "y":
    sistemUtama = True
  else:
    print("maaf kesalahan huruf, jadi kalkulator harus berhenti")
    sistemUtama = False