import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sentiment = pd.read_csv("fear_greed_index.csv")
trades = pd.read_csv("historical_data.csv")

print(sentiment.head())
print(trades.head())

print(sentiment.info())
print(trades.info())

# Convert date
sentiment['date'] = pd.to_datetime(sentiment['date'])
sentiment['date'] = sentiment['date'].dt.date

# Keep only required columns
sentiment = sentiment[['date', 'classification']]

# Convert timestamp (IMPORTANT)
trades['Timestamp'] = pd.to_datetime(trades['Timestamp'], unit='ms')

# Extract date
trades['date'] = trades['Timestamp'].dt.date

# Rename columns (for simplicity)

trades.rename(columns={
    'Account': 'account',
    'Closed PnL': 'closedPnL',
    'Size USD': 'size',
    'Side': 'side',
    'Leverage': 'leverage'
}, inplace=True)

if 'Leverage' not in trades.columns:
    trades['leverage'] = 1  # default value


# Merge datasets on date
df = pd.merge(trades, sentiment, on='date', how='inner')

print(df.head())

df['win'] = df['closedPnL'] > 0
daily_pnl = df.groupby(['date', 'account'])['closedPnL'].sum().reset_index()
win_rate = df.groupby('account')['win'].mean().reset_index()
win_rate.rename(columns={'win': 'win_rate'}, inplace=True)

avg_trade_size = df.groupby('account')['size'].mean().reset_index()
trades_per_day = df.groupby('date').size().reset_index(name='trade_count')

long_short_ratio = df['side'].value_counts(normalize=True)
print(long_short_ratio)

print(df['leverage'].describe())

pnl_by_sentiment = df.groupby('classification')['closedPnL'].mean()
print(pnl_by_sentiment)

win_by_sentiment = df.groupby('classification')['win'].mean()
print(win_by_sentiment)

trade_count_sentiment = df['classification'].value_counts()
print(trade_count_sentiment)

plt.figure()
sns.barplot(x='classification', y='closedPnL', data=df)
plt.title("PnL by Market Sentiment")
plt.xticks(rotation=45)
plt.show()

#win rate
plt.figure()
sns.barplot(x='classification', y='win', data=df)
plt.title("Win Rate by Sentiment")
plt.xticks(rotation=45)
plt.show()

#leverage distribution
plt.figure()
sns.boxplot(x='classification', y='leverage', data=df)
plt.title("Leverage by Sentiment")
plt.xticks(rotation=45)
plt.show()

#Trader Segmentation
df['leverage_type'] = np.where(
    df['leverage'] > df['leverage'].median(),
    'High',
    'Low'
)

print(df['leverage_type'].value_counts())

#frequent vs infrequent traders
trade_counts = df['account'].value_counts()
threshold = trade_counts.median()

df['trader_type'] = df['account'].map(
    lambda x: 'Frequent' if trade_counts[x] > threshold else 'Infrequent'
)
print(df['trader_type'].value_counts())

#output
df.to_csv("final_output.csv", index=False)
