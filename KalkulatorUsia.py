import mytools as mt

riwayat = []

while True:
    mt.bersih()
    mt.cyan("""
                      <<<< --- >>>>
                {==== KALKULATOR USIA ====}
                      <<<< __ >>>>
    """)
    
    if riwayat:
        print("Riwayat sebelumnya:")
        for r in riwayat:
            print(f" - {r}")
        print("-"*30)

    tahun_skr = 2026
    
    try:
        tahun_lhr = int(input("\nMasukan tahun lahirmu (0 buat keluar): "))
    except ValueError:
        input("Eranga tahun lahir goblok! Tekan enter...")
        continue

    if tahun_lhr == 0:
        break

    usia = tahun_skr - tahun_lhr
    print(f"\nUmur mu sekarang adalah {usia} tahun")

    if(usia < 0):
        kategori = "Masih dalam proses"
    elif(usia <= 11):
        kategori = "Masih ngelap ingus di baju wkwkwk"
    elif(usia <= 16):
        kategori = "Masih bocil riapek-rispek..."
    elif(usia == 17):
        kategori = "Udah boleh tuh buat ktp!"
    elif(usia <= 24):
        kategori = "Abang-abangan imo sokk keras!"
    elif(usia <= 30):
        kategori = "Sesepuh tongkrongan iziiiiin..."
    elif(usia <= 42):
        kategori = "Bapak-bapak anak tiga!"
    elif(usia <= 59):
        kategori = "Masa-masa penuaan"
    elif(usia <= 80):
        kategori = "Lansia, normal sih biasanya veteran perang"
    elif(usia <= 99):
        kategori = "Lansia tingkat lanjut, agak ngecit, mulai gak normal"
    elif(usia <= 110):
        kategori = "Udah gak normal jirr seabad lebih loh ya!"
    else:
        kategori = f"Ini sih bukan gak normal lagi, tapi abnormal jiirrrrr, mana ada manusia idup sampe {usia} tahun woilahhhhhhhhhhhh"

    print(f"Kategori: {kategori}")
    riwayat.append(f"{tahun_lhr} -> {usia} thn ({kategori})")

    input("\nTekan enter untuk orang selanjutnya")
    mt.bersih(