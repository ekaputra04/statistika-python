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
    probability = input("Masukkan Probability : ")
    probability = float(probability)
    μ = input("Masukkan nilai μ : ")
    μ = float(μ)
    σ = input("Masukkan nilai σ : ")
    σ = float(σ)
    z_score = stats.norm.ppf(probability)
    x_score = μ + z_score * σ  
    print("Z Score : ", z_score)
    print("X Score : ", x_score)
    
    x = np.arange(-3, 3, 0.001)
    draw_z_score(x, x<z_score)

if __name__ == "__main__":
    main()
