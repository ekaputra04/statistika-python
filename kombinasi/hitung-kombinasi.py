import itertools

def main():
    # kombinasi : 
    # nPr => kombinasi r objek dari n objek

    print("kombinasi => nCr => kombinasi r objek dari n objek")

    n = input("Input nilai n : ")    
    r = input("Input nilai r : ")
    n = int(n)
    r = int(r)
    kombinasi = itertools.combinations(range(n), r)
    hasil = len(tuple(kombinasi))
    print("Hasil kombinasi", r, "objek dari", n, "objek :", hasil)

if __name__ == "__main__":
    main()
