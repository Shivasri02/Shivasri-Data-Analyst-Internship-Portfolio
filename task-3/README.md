# 📊 Trader Behavior Analysis Using Market Sentiment

## 📌 Project Overview
This project analyzes the impact of market sentiment (Fear vs Greed) on trader performance and behavior using historical trading data.

## 🎯 Objectives
- Compare performance during Fear and Greed periods  
- Analyze trading behavior (frequency and trade size)  
- Generate actionable trading insights  

## 📂 Datasets

### 1. Fear & Greed Index
- Date  
- Sentiment (Fear, Greed, etc.)  

### 2. Historical Trading Data
- Account  
- Trade Size (USD)  
- Buy/Sell  
- Closed PnL  
- Timestamp  

## ⚙️ Methodology
- Converted timestamps to date format  
- Merged datasets using date  
- Created metrics: win rate, daily PnL  
- Compared performance across sentiments  
- Used visualizations for insights  

## 📊 Key Insights
- Better performance during Greed periods  
- Higher win rate in positive sentiment  
- Increased trading activity during Greed  
- Fear periods show inconsistent results  

## 💡 Strategy Recommendations
- During Fear: reduce trade size and avoid overtrading  
- During Greed: trade actively with risk control  

## 🛠 Tools Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

pip install pandas matplotlib seaborn
python analysis.py
