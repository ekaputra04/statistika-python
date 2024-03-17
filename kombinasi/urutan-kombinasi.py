import itertools


def main():
    data = ['A', 'B', 'C', 'D', 'E']

    print("kombinasi dengan menyertakan berapa objek:")
    kombinasi = itertools.combinations(data, 3)
    for combination in kombinasi:
        print(combination)

if __name__ == "__main__":
    main()
