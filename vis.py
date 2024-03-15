import matplotlib.pyplot as plt
import pandas as pd

def vis(df):
    # Filter fraudulent and non-fraudulent transactions
    fraudulent = df[df['Class'] == 1]
    non_fraudulent = df[df['Class'] == 0]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(non_fraudulent['Time'], non_fraudulent['Amount'], color='blue', alpha=0.5, label='Non-Fraudulent')
    plt.scatter(fraudulent['Time'], fraudulent['Amount'], color='red', alpha=0.5, label='Fraudulent')
    plt.xlabel('Time')
    plt.ylabel('Transaction Amount')
    plt.title('Scatter Plot of Transaction Amount vs Time')
    plt.legend()
    plt.grid(True)

    plt.savefig('scatter_plot.png')


