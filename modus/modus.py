from collections import Counter

def hitung_modus(data):
    # Menghitung frekuensi kemunculan setiap nilai dalam data
    frekuensi = Counter(data)
    # Mencari nilai dengan frekuensi tertinggi (modus)
    modus_frekuensi = max(frekuensi.values())
    modus = [k for k, v in frekuensi.items() if v == modus_frekuensi]
    return modus, modus_frekuensi

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan data (atau ketik 'end' untuk menghitung modus): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan data numerik atau 'end' untuk menghitung modus.")

    if data:
        sorted_data = sorted(data)
        modus, frekuensi = hitung_modus(sorted_data)

        print("=============================================")
        print("Data Terurut :")
        print("---------------------------------------------")

        for i in range(len(data)):
            print(sorted_data[i])

        print("---------------------------------------------")
        print("Modus dari data adalah : ", modus)
        print("Frekuensi data adalah  : ", frekuensi)
        print("=============================================")
    else:
        print("Tidak ada data untuk dihitung modus.")

if __name__ == "__main__":
    main()
