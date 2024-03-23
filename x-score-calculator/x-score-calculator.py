from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# online:
# https://www.calculator.net/z-score-calculator.html

def hitung_x_score(z, μ, σ):
    x = μ + z * σ    
    return x
    
def main():
    z = input("Masukkan nilai z score : ")
    z = float(z)
    μ = input("Masukkan nilai μ : ")
    μ = float(μ)
    σ = input("Masukkan nilai σ : ")
    σ = float(σ)
    x = hitung_x_score(z, μ, σ)
    print("Nilai x :", x)

if __name__ == "__main__":
    main()
