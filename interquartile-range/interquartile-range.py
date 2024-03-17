import numpy as np

def hitung_kuartil(data):
    sorted_data = sorted(data)
    q1 = np.percentile(sorted_data, 25)
    q3 = np.percentile(sorted_data, 75)
    iqr = q3 - q1
    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr
    outliers = [x for x in sorted_data if x < batas_bawah or x > batas_atas]
    return q1, q3, iqr, batas_bawah, batas_atas, outliers

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan angka (atau ketik 'end' untuk menentukan interkuartil): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan angka atau 'end' untuk menentukan interkuartil.")
    
    if data:
        print("================================================================================")
        print("                                Interkuartil                                    ")
        print("================================================================================")
        q1, q3, iqr, batas_bawah, batas_atas, outliers = hitung_kuartil(data)
        print("Data yang sudah diurut:", sorted(data))
        print("Kuartil 1 (Q1):", q1)
        print("Kuartil 3 (Q3):", q3)
        print("Interkuartil Range (IQR):", iqr)
        print("Batas Bawah Outlier:", batas_bawah)
        print("Batas Atas Outlier:", batas_atas)
        print("Data Outlier:", outliers)
        print("================================================================================")
    else:
        print("Tidak ada data untuk dihitung interkuartil.")

if __name__ == "__main__":
    main()
