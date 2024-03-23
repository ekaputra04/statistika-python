from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# online:
# https://www.calculator.net/z-score-calculator.html

def hitung_z_score(x, μ, σ):
    z_score = (x - μ) / σ    
    return z_score
    
def main():
    x = input("Masukkan nilai X : ")
    x = float(x)
    μ = input("Masukkan nilai μ : ")
    μ = float(μ)
    σ = input("Masukkan nilai σ : ")
    σ = float(σ)
    z_score = hitung_z_score(x, μ, σ)
    print("Nilai Z Score :", z_score)

if __name__ == "__main__":
    main()
