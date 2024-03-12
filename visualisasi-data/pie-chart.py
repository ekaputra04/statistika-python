import pandas as pd
import matplotlib.pyplot as plt

def main():
    kopi_data = {
        'jenis_kopi': [
            'Latte',
            'Cappuccino',
            'Americano',
            'Espresso'
        ],
        'total_omset':[
            942,
            1716,
            731,
            220
        ]
    }

    kopi_df = pd.DataFrame(kopi_data)
    
    plt.figure(figsize=(12, 8))
    plt.pie(kopi_df['total_omset'], labels=kopi_df['jenis_kopi'], autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart Omset Jenis Kopi')
    plt.axis('equal')  # Untuk memastikan pie chart berbentuk lingkaran
    plt.show()

if __name__ == "__main__":
    main()
