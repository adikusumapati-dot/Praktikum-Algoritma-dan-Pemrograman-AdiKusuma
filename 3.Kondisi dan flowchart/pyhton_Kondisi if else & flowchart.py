negara = input("dimana kamu ingin mengemudi? (Afrika Selatan, Prancis,Jepang,Meksiko,Indonesia,) ")
usia = int(input("berapa usiamu? "))

# jika memilih afrika selatan
if negara == "Afrika Selatan":
    if usia >= 17:
        print("kamu boleh mengemudi")
    else:
        print("kamu tidak boleh mengemudi")

# jika memilih Prancis
elif negara == "Prancis":
    if usia >= 18:
        print("kamu boleh mengemudi")
    elif usia >= 15:
        print("kamu boleh mengemudi dengan pengawasan")
    else:
        print("kamu tidak boleh mengemudi")

# jika memilih Jepang
elif negara == "Jepang":
    if usia >= 18:
        print("kamu boleh mengemudi")
    elif usia >= 16:
        print("kamu boleh mengemudi dengan izin orang tua")
    else:
        print("kamu tidak boleh mengemudi")

# jika memilih meksiko
elif negara == "Meksiko":
    if usia >= 18:
        print("kamu boleh mengemudi")
    elif usia >= 16:
        print("kamu boleh mengemudi dengan izin orang tua")
    elif usia >= 15:
        print("kamu boleh mengemudi dengan pengawasan orang tua")
    else:
        print("kamu tidak boleh mengemudi")

# jika memilih indonesia
elif negara == "Indonesia":
    if usia >= 18:
      print("kamu boleh mengemudi")
    else:
      print("kamu tidak boleh mengemudi")
else:
    print("Data tidak tersedia untuk negara ini")