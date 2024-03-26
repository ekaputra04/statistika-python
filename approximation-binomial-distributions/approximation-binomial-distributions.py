from scipy import stats
import math
import matplotlib.pyplot as plt

def draw_z_score(x, cond, mu=0, sigma=1):
    y = stats.norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, stats.norm.pdf(z, mu, sigma))
    plt.show()

def main():
    n = float(input("Masukkan nilai n : "))
    p = float(input("Masukkan nilai p : "))
    q = 1 - p
    np = n * p
    nq = n * q
    print(f'np = {np} dan nq = {nq}')

    if np < 5 or nq < 5:
        print("Bukan termasuk distribusi normal")
        exit()
    
    mu = np
    sigma = math.sqrt(n * p * q)
    x = float(input("Masukkan nilai x (ingat selisihkan dengan 0.5): "))
    z_score = (x - mu) / sigma
    P = stats.norm.cdf(z_score)
    print(f'P = {P}')

    x = np.arange(-3, 3, 0.001)
    draw_z_score(x, x<z_score)

if __name__ == "__main__":
    main()
