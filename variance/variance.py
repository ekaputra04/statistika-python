def hitung_varian(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    varian = sum(squared_diff) / len(data)
    return varian, squared_diff

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan angka (atau ketik 'end' untuk menghitung varian): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan angka atau 'end' untuk menghitung varian.")
    
    if data:
        print("================================================================================")
        print("                          Variant & Standar Deviation                           ")
        print("================================================================================")
        print("{:<10} {:<10} {:<15} {:<20} {:<10}".format("Data", "Mean","(Data-Mean)", "(Data-Mean)^2", "Squared Diff"))
        mean = sum(data) / len(data)
        for i, x in enumerate(data):
            squared_diff = (x - mean) ** 2
            print("{:<10} {:<10.2f} {:<15.2f} {:<20.2f} {:<10.2f}".format(x, mean, (x-mean), squared_diff, squared_diff))
        
        varian, squared_diff = hitung_varian(data)
        print("--------------------------------------------------------------------------------")
        print("SUM : {:>58.2f}".format(sum(squared_diff)))
        print("--------------------------------------------------------------------------------")
        print("Banyak Data :", len(data))
        print(sum(squared_diff), "/", len(data))
        print("Varian :", varian)
        print("Standar Deviasi :", varian**0.5)
        print("================================================================================")
    else:
        print("Tidak ada data untuk dihitung varian.")

if __name__ == "__main__":
    main()
