import pandas as pd
import seaborn as sns

# Q1
df = pd.read_csv('virus_data.csv')
print(len(df))
print(len(df.columns))

# Q2
print(df['num_of_siblings'].value_counts())

# Q8

# add state
df['address'] = df['address'].fillna('\n,')
print(df['address'].head())
df['state'] = df['address'].apply(lambda x: (x.split('\n')[1].split(',')[0]))


def plot_hist(col_name, df, kde=True):
    pass
