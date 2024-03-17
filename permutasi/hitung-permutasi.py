import itertools

def main():
    # Permutasi : 
    # nPr => permutasi r objek dari n objek

    print("Permutasi => nPr => permutasi r objek dari n objek")

    n = input("Input nilai n : ")    
    r = input("Input nilai r : ")
    n = int(n)
    r = int(r)
    permutasi = itertools.permutations(range(n), r)
    hasil = len(tuple(permutasi))
    print("Hasil permutasi", r, "objek dari", n, "objek :", hasil)

if __name__ == "__main__":
    main()
