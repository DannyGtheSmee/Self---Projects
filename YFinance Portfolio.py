#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
pandas._version


# In[ ]:





# In[2]:


import pandas as pd
import yfinance as yf  # Yahoo Finance API

# Fetch historical stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2023-01-01', end='2023-11-01')

# Display data
print(data.head())

# Perform analysis (e.g., calculate moving averages)
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Stock Price')
plt.plot(data['SMA_50'], label='50-day SMA')
plt.plot(data['SMA_200'], label='200-day SMA')
plt.legend()
plt.show()


# In[5]:


pip install yfinance


# In[8]:


import pandas as pd
import yfinance as yf  # Yahoo Finance API

# Fetch historical stock data
ticker = 'NKE'
data = yf.download(ticker, start='2023-01-01', end='2023-11-01')

# Display data
print(data.head())

# Perform analysis (e.g., calculate moving averages)
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Stock Price')
plt.plot(data['SMA_50'], label='50-day SMA')
plt.plot(data['SMA_200'], label='200-day SMA')
plt.legend()
plt.show()


# In[ ]:




