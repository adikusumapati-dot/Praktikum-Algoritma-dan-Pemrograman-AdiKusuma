Indomie_tersedia = ["Biasa", "Aceh", "Rendang", "Cabe ijo", "Ayam bawang"]
Indomie_order = []
total_price = 0

print("Haloo, dibawah ini merupakan menu toko ini :")

# Menampilkan menu
for i, Indomie in enumerate(Indomie_tersedia):
    print(str(i) + ". " + Indomie)

continue_ordering = True
while continue_ordering:
    answer = input("\nApakah kamu ingin membeli Indomie (y/t)? ").lower()
    
    if answer == "y":
        valid_Indomie_choice = False
        
        while not valid_Indomie_choice:
            try:
                Indomie_choice = int(input("Indomie apa yang diinginkan? (angka saja) "))
                
                # Validasi pilihan menu
                if 0 <= Indomie_choice < len(Indomie_tersedia):
                    Indomie_order.append(Indomie_tersedia[Indomie_choice])
                    print("Menambahkan Indomie " + Indomie_tersedia[Indomie_choice] + " ke dalam pesanan.")
                    total_price += 10000  # Disesuaikan dengan asumsi nominal harga Rp 10.000
                    valid_Indomie_choice = True
                else:
                    print("Tolong masukkan angka yang tertera dalam menu.")
            except ValueError:
                print("Input harus berupa angka!")
                
    elif answer == "t":
        continue_ordering = False
    else:
        print("Pilihan tidak valid, ketik 'y' untuk ya atau 't' untuk tidak.")

# Memeriksa apakah ada pesanan sebelum memproses pembayaran
if Indomie_order:
    print("\nKamu memesan: " + ", ".join(Indomie_order))
    print("Kamu harus membayar " + str(total_price) + " Rupiah.")

    valid_tip = False
    while not valid_tip:
        try:
            tip = float(input("\nBerapa tip yang ingin ditinggalkan (0-25%)? "))
            if 0 <= tip <= 25:
                valid_tip = True
            else:
                print("Tolong masukkan angka antara 0-25.")
        except ValueError:
            print("Input harus berupa angka!")

    total_price += total_price * tip / 100
    print(f"\nTerima kasih! Total harga: {total_price:,.0f} Rupiah. Indomie otw!")
else:
    print("\nTidak ada pesanan. Terima kasih sudah berkunjung!")