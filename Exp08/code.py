import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate Wine Quality Dataset
def generate_wine_quality_data(num_samples=1000):
    np.random.seed(0)
    data = {
        'fixed acidity': np.random.uniform(4, 15, num_samples),
        'volatile acidity': np.random.uniform(0, 2, num_samples),
        'citric acid': np.random.uniform(0, 1, num_samples),
        'residual sugar': np.random.uniform(0, 10, num_samples),
        'chlorides': np.random.uniform(0, 0.2, num_samples),
        'free sulfur dioxide': np.random.uniform(1, 50, num_samples),
        'total sulfur dioxide': np.random.uniform(6, 100, num_samples),
        'density': np.random.uniform(0.99, 1.04, num_samples),
        'pH': np.random.uniform(2.8, 4, num_samples),
        'sulphates': np.random.uniform(0.3, 1.5, num_samples),
        'alcohol': np.random.uniform(8, 15, num_samples),
        'quality': np.random.randint(3, 9, num_samples),
        'Id': range(num_samples)
    }
    df = pd.DataFrame(data)
    df.to_csv('wine_quality.csv', index=False)
    print("Dataset generated and saved as 'wine_quality.csv'")

# Exploratory Data Analysis (EDA)
def explore_wine_quality_data():
    # Load the dataset
    df = pd.read_csv('wine_quality.csv')

    # Basic data overview
    print(df.head())
    print(df.describe())
    print(df.info())

    # Histograms
    fig, axs = plt.subplots(4, 4, figsize=(20, 15))  # Adjusted to 4x4 grid
    axs = axs.flatten()  # Flatten the axes array for easier iteration
    for i, col in enumerate(df.columns):
        df[col].hist(bins=15, ax=axs[i])
        axs[i].set_title(col)
    plt.tight_layout()
    plt.show()


    # Boxplots
    plt.figure(figsize=(12, 6))
    df.drop('Id', axis=1).boxplot()
    plt.xticks(rotation=45)
    plt.title('Boxplot of Wine Quality Variables')
    plt.show()

    # Scatter Plots
    sns.pairplot(df[['alcohol', 'volatile acidity', 'sulphates', 'quality']])
    plt.show()

    # Bar Plot
    plt.figure(figsize=(8, 4))
    sns.countplot(x='quality', data=df)
    plt.title('Distribution of Wine Quality Ratings')
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Wine Quality Variables')
    plt.show()

    # Summary Statistics
    print(df.groupby('quality').mean())

# Generate Wine Quality Dataset
generate_wine_quality_data()

# Explore Wine Quality Dataset
explore_wine_quality_data()
