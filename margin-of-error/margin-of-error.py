from scipy import stats
import math
import matplotlib.pyplot as plt


def main():
    c = float(input("Masukkan nilai Level of Confidence (c) : "))
    sigma = float(input("Masukkan nilai Sigma : "))
    n = float(input("Masukkan banyak data (n) : "))
    p = 1 - ((1-c) / 2)

    z_score = stats.norm.ppf(p)

    E = z_score * sigma / math.sqrt(n)
    print(f'E = {E}')

if __name__ == "__main__":
    main()
