def hitung_distribusi_frekuensi(data, lebar_kelas):
    # Menghitung nilai minimum dan maksimum dari data
    nilai_min = min(data)
    nilai_max = max(data)
    
    # Menghitung jumlah kelas
    jumlah_kelas = int((nilai_max - nilai_min) / lebar_kelas)
    
    # Menghitung frekuensi kemunculan setiap nilai dalam data
    frekuensi = {}
    for nilai in data:
        kelas = int((nilai - nilai_min) // lebar_kelas)
        kelas_bawah = nilai_min + (kelas * lebar_kelas)
        kelas_atas = kelas_bawah + lebar_kelas
        if kelas_bawah in frekuensi:
            frekuensi[kelas_bawah][1] += 1
        else:
            frekuensi[kelas_bawah] = [kelas_atas, 1]
    
    # Memastikan rentang kelas ditulis, bahkan jika frekuensinya adalah 0
    for kelas_bawah in range(int(nilai_min), int(nilai_max), int(lebar_kelas)):
        if kelas_bawah not in frekuensi:
            kelas_atas = kelas_bawah + lebar_kelas
            frekuensi[kelas_bawah] = [kelas_atas, 0]
    
    # Menghitung midpoint (MP), relative frequency (RF), dan cumulative frequency (CF)
    total_data = len(data)
    distribusi_frekuensi = []
    cumulative_frequency = 0
    for kelas_bawah, (kelas_atas, freq) in sorted(frekuensi.items()):
        mp = (kelas_bawah + kelas_atas) / 2
        rf = freq / total_data
        cumulative_frequency += freq
        cf = cumulative_frequency
        distribusi_frekuensi.append((kelas_bawah, kelas_atas, freq, mp, rf, cf))
    
    return distribusi_frekuensi

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan angka (atau ketik 'end' untuk menghitung distribusi frekuensi): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan angka atau 'end' untuk menghitung distribusi frekuensi.")
    
    lebar_kelas = float(input("Masukkan lebar kelas: "))

    if data:
        distribusi_frekuensi = hitung_distribusi_frekuensi(data, lebar_kelas)
        print("================================================================================")
        print("                           Tabel Distribusi Frekuensi                           ")
        print("================================================================================")
        print("{:<10} {:<10} {:<10} {:<20} {:<10}".format("Kelas", "Frekuensi", "MP", "RF", "CF"))
        print("--------------------------------------------------------------------------------")
        for kelas_bawah, kelas_atas, freq, mp, rf, cf in distribusi_frekuensi:
            print("{:<10} {:<10} {:<10} {:<20} {:<10}".format(f"{kelas_bawah}-{kelas_atas-1}", freq, mp, rf, cf))
        print("================================================================================")                
    else:
        print("Tidak ada data untuk dihitung distribusi frekuensi.")

if __name__ == "__main__":
    main()
