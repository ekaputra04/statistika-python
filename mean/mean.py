def hitung_mean(data):
    return sum(data) / len(data)

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan data (atau ketik 'end' untuk menghitung mean): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan data numerik atau 'end' untuk menghitung mean.")

    if data:
        mean = hitung_mean(data)

        print("=============================================")
        print("Data :")
        print("---------------------------------------------")

        for i in range(len(data)):
          print(data[i])

        print("---------------------------------------------")
        print("Mean dari data adalah:", mean)
        print("=============================================")
    else:
        print("Tidak ada data untuk dihitung mean.")

if __name__ == "__main__":
    main()
