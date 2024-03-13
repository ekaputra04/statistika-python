import numpy as np

def hitung_kuartil(data):
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    return q1, q2, q3

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan angka (atau ketik 'end' untuk menentukan kuartil): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan angka atau 'end' untuk menentukan kuartil.")
    
    if data:        
        data_urut = sorted(data)
        q1, q2, q3 = hitung_kuartil(data)
        print("================================================================================")
        print("                                   Kuartil                                      ")
        print("================================================================================")
        print("Data Terurut:", data_urut)        
        print("\nKuartil 1 (Q1):", q1)
        print("Kuartil 2 (Q2):", q2)
        print("Kuartil 3 (Q3):", q3)
    else:
        print("Tidak ada data untuk dihitung kuartil.")

if __name__ == "__main__":
    main()
