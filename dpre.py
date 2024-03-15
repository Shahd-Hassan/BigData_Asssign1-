import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.cluster import KMeans

def dpre(df):
    # Data Transformation
    # Convert time to hours
    df['Time'] = df['Time'] / 3600

    # Task 1: Normalize 'Amount' feature
    scaler = StandardScaler()
    df['Amount_normalized'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))

    # Task 2: Convert 'Amount' to logarithmic scale
    df['Amount_log'] = df['Amount'].apply(lambda x: np.log(x + 1))

    # Data Cleaning
    # Task 1: Remove duplicated records
    df.drop_duplicates(inplace=True)

    # Task 2: Handle missing values by imputing with median
    imputer = SimpleImputer(strategy='median')
    df['V1_imputed'] = imputer.fit_transform(df['V1'].values.reshape(-1, 1))

    # Data Reduction
    # Task 1: Perform PCA for dimensionality reduction
    pca = PCA(n_components=10)
    df_reduced = pca.fit_transform(df.drop(['Class'], axis=1))

    # Task 2: Use SelectKBest for feature selection
    selector = SelectKBest(score_func=f_classif, k=5)
    X_selected = selector.fit_transform(df.drop(['Class'], axis=1), df['Class'])

    # Data Discretization
    # Task 1: Apply binning to 'Amount'
    df['Amount_binned'] = pd.qcut(df['Amount'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

    # Task 2: Apply clustering to 'Time' feature
    kmeans = KMeans(n_clusters=4)
    df['Time_cluster'] = kmeans.fit_predict(df[['Time']])

    # Save the resulting data to a new CSV file
    df.to_csv('res_dpre.csv', index=False)
    return df
