from scipy import stats
import math
import matplotlib.pyplot as plt


def main():
    c = float(input("Masukkan nilai Level of Confidence (c) : "))
    sigma = float(input("Masukkan nilai Sigma : "))
    n = float(input("Masukkan banyak data (n) : "))
    x_bar = float(input("Masukkan rata-rata sampel (x bar) : "))
    
    sigma_x_bar = sigma / math.sqrt(n)
    confidence_interval = stats.norm.interval(c, loc=x_bar, scale=sigma_x_bar)
    print(f'Confidence interval = {confidence_interval}')

if __name__ == "__main__":
    main()
