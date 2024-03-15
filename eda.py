def eda(df):
    import numpy as np

    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # Numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    columns = numeric_df.columns
    results = np.zeros((len(columns), len(columns)))

    # Calculate cosine similarity between numeric columns
    for i in range(len(columns)):
        for j in range(len(columns)):
            col1 = numeric_df[columns[i]]
            col2 = numeric_df[columns[j]]
            similarity = cosine_similarity(col1, col2)
            results[i, j] = similarity

    # Insight 1: Cosine similarity between numeric columns
    with open('eda-insight-1.txt', 'w') as f:
        for i in range(len(columns)):
            for j in range(len(columns)):
                f.write(f'Cosine similarity between {columns[i]} and {columns[j]}: {results[i, j]}\n')

    # Insight 2: Summary statistics (mean, median) for numeric columns
    with open('eda-insight-2.txt', 'w') as f:
        for col in columns:
            mean_val = numeric_df[col].mean()
            median_val = numeric_df[col].median()
            f.write(f'{col} has Mean of: {mean_val} and a Median of {median_val}\n')

    # Insight 3: Class distribution (fraudulent vs. non-fraudulent transactions)
    num_fraudulent = df['Class'].sum()
    num_non_fraudulent = len(df) - num_fraudulent
    total_transactions = len(df)
    fraud_percentage = (num_fraudulent / total_transactions) * 100

    with open('eda-insight-3.txt', 'w') as f:
        f.write(f'Number of fraudulent transactions: {num_fraudulent}\n')
        f.write(f'Number of non-fraudulent transactions: {num_non_fraudulent}\n')
        f.write(f'Total transactions: {total_transactions}\n')
        f.write(f'Percentage of fraudulent transactions: {fraud_percentage:.2f}%\n')



