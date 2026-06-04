import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
train_df = pd.read_csv('train.csv')

# 1. Create Heatmap
plt.figure(figsize=(10, 8))
corr = train_df.select_dtypes(include=['number']).corr()
sns.heatmap(corr, cmap='coolwarm')
plt.savefig('task3_heatmap.png')
plt.show()

# 2. Create Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='OverallQual', y='SalePrice', data=train_df)
plt.savefig('task3_boxplot.png')
plt.show()