import itertools


def main():
    data = ['A', 'B', 'C', 'D']

    print("Permutasi tanpa menyertakan berapa objek:")
    permutasi = itertools.permutations(data)
    for permutation in permutasi:
        print(permutation)

    print("Permutasi dengan menyertakan berapa objek:")
    permutasi = itertools.permutations(data, 2)
    for permutation in permutasi:
        print(permutation)

if __name__ == "__main__":
    main()
