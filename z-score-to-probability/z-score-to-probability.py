from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# online:
# https://www.calculator.net/z-score-calculator.html

def draw_z_score(x, cond, mu=0, sigma=1):
    y = stats.norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, stats.norm.pdf(z, mu, sigma))
    plt.show()
    
def main():
    z_score = input("Masukkan Z-score : ")
    z_score = float(z_score)
    p = stats.norm.cdf(z_score)
    print("Probability : ", p)
    
    x = np.arange(-3, 3, 0.001)
    draw_z_score(x, x<z_score)

if __name__ == "__main__":
    main()
