def hitung_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan data (atau ketik 'end' untuk menghitung median): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan data numerik atau 'end' untuk menghitung median.")

    if data:
        sorted_data = sorted(data)
        median = hitung_median(sorted_data)

        print("=============================================")
        print("Data Terurut :")
        print("---------------------------------------------")

        for i in range(len(data)):
            print(sorted_data[i])

        print("---------------------------------------------")
        print("Median dari data adalah:", median)
        print("=============================================")
    else:
        print("Tidak ada data untuk dihitung median.")

if __name__ == "__main__":
    main()
