def hitung_standar_deviasi(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    varian = sum(squared_diff) / len(data)
    standar_deviasi = varian ** 0.5
    return standar_deviasi

def main():
    data = []
    while True:
        try:
            input_data = input("Masukkan angka (atau ketik 'end' untuk menghitung coefficient of variation): ")
            if input_data.lower() == 'end':
                break
            data.append(float(input_data))
        except ValueError:
            print("Masukkan angka atau 'end' untuk menghitung coefficient of variation.")
    
    if data:
        mean = sum(data) / len(data)
        print("================================================================================")
        print("                           Coefficient of Variation                             ")
        print("================================================================================")
        print("{:<10} {:<10} {:<15} {:<15} {:<20} {:<20}".format("X", "F", "X * F", "X - Mean", "(X - Mean)^2", "(X - Mean)^2 * F"))
        squared_diff = [(x - mean) ** 2 for x in data]
        for i, x in enumerate(data):
            x_f = x
            x_minus_mean = x - mean
            squared_diff_f = squared_diff[i]
            print("{:<10} {:<10} {:<15} {:<15.2f} {:<20.2f} {:<20.2f}".format(x, 1, x_f, x_minus_mean, squared_diff_f, squared_diff_f))
        print("--------------------------------------------------------------------------------")        
        print("SUM :{:>74}".format(sum(squared_diff)))
        print("Jumlah data :", len(data))
        print("Mean :", mean)
        standar_deviasi = hitung_standar_deviasi(data)
        print("\nStandar deviasi dari data adalah:", standar_deviasi)
        print("Coefficient of variation dari data adalah:", (standar_deviasi / mean) * 100, "%")
        print("================================================================================")
    else:
        print("Tidak ada data untuk dihitung coefficient of variation.")

if __name__ == "__main__":
    main()
