import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def main():
    iris = load_iris()
    iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
    # print(iris_df)

    plt.figure(2, figsize=(10, 6))
    plt.scatter(data=iris_df, x = 'petal length (cm)', y = 'petal width (cm)')
    plt.xlabel('petal length (cm)')
    plt.ylabel('petal width (cm)')
    plt.show()

if __name__ == "__main__":
    main()
