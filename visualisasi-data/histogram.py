import matplotlib.pyplot as plt

def main():
    data = [128, 100, 180, 150, 200, 90, 340, 105, 85, 270,
            200, 65, 230, 150, 150, 120, 130, 80, 230, 200,
            110, 126, 170, 132, 140, 112, 90, 340, 170, 190]

    # Mengatur jumlah bin agar histogram lebih informatif
    num_bins = 10

    # Menampilkan histogram
    plt.hist(data, bins=num_bins, edgecolor='black')

    # Menampilkan ogive
    # plt.hist(data, cumulative=True, edgecolor='black')

    plt.title('Histogram Data')
    plt.xlabel('Nilai')
    plt.ylabel('Frekuensi')
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
