from datascrape import scrape_data
import pandas as pd
import matplotlib.pyplot as plt

data = scrape_data()

df = pd.DataFrame(data[1:], columns=data[0])

def cal_returns(df, return_type):
    df['Date'] = pd.to_datetime(df['Date']) #Convert 'Date' column to datetime
    
    new_df= df.set_index('Date') #Set 'Date' as the index
    
    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    new_df[numeric_columns] = new_df[numeric_columns].apply(pd.to_numeric, errors='coerce') #Convert numeric columns to float # for multiple columns
    
    new_df['Daily_Return'] = new_df['Close'].pct_change() #Calculate daily returns
    daily_returns = new_df['Daily_Return']
    
    weekly_returns = daily_returns.resample('W').sum() #resampling the data to a weekly frequency and summing the daily returns within each week
    
    if return_type == 'daily':
          return daily_returns
    elif return_type == 'weekly':
          return weekly_returns
    
    return daily_returns, weekly_returns #return 2 series; daily returns, weekly returns as columns

# print(cal_returns(df,'weekly').head())

def cal_moving_average(df, col_name, window_size):  
    df[col_name] = pd.to_numeric(df[col_name], errors='coerce') #Convert numeric column to float

    sma = df[col_name].rolling(window=window_size, min_periods=1).mean() #simple moving average
    ema = df[col_name].ewm(span=window_size, adjust= False).mean() #exponential moving average
            
    moving_averages = pd.DataFrame({'Date':df['Date'], 'SMA':sma, 'EMA':ema})

    return moving_averages #returns a dataframe with col 'SMA' and 'EMA'

# print(cal_moving_average(df,'Close', 50).head())

def cal_volatility(df, return_type):
    daily_returns, weekly_returns = cal_returns(df,'')
    daily_volatility = daily_returns.std()
    weekly_volatility = weekly_returns.std()

    if return_type == 'daily':
          return daily_volatility
    elif return_type == 'weekly':
          return weekly_volatility
    
    return daily_volatility, weekly_volatility


         

# # Assuming you have already calculated daily and weekly returns
daily_returns = cal_returns(df, return_type='daily')
weekly_returns = cal_returns(df, return_type='weekly')

# Plot daily returns
plt.figure(figsize=(10, 6))
plt.plot(daily_returns.index, daily_returns, label='Daily Returns', color='blue')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.title('Daily Returns')
plt.legend()

# Plot weekly returns
plt.figure(figsize=(10, 6))
plt.plot(weekly_returns.index, weekly_returns, label='Weekly Returns', color='green')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.title('Weekly Returns')
plt.legend()

plt.show()
      

# print(cal_volatility(df))
