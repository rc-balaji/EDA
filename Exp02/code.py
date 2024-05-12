import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('email_categories_dataset.csv')

# Display the first few rows of the dataframe
print(df.head())

# Basic statistics about the dataset
print(df.describe())

# Count the number of emails in each category
email_counts = df['category'].value_counts()
print(email_counts)

# Visualize the distribution of emails across categories
sns.barplot(x=email_counts.index, y=email_counts.values)
plt.title('Distribution of Emails by Category')
plt.xlabel('Category')
plt.ylabel('Number of Emails')
plt.xticks(rotation=45)

# Annotate each bar with its respective count
for index, value in enumerate(email_counts.values):
    plt.text(index, value, str(value), ha='center', va='bottom')

plt.show()
