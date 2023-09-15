from datascrape import scrape_data
import pandas as pd

data = scrape_data()

df = pd.DataFrame(data[1:], columns=data[0])

def cal_weekly_returns(df):
    
    df['Date'] = pd.to_datetime(df['Date']) #Convert 'Date' column to datetime
    
    df.set_index('Date', inplace=True) #Set 'Date' as the index
    
    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce') #Convert numeric columns to float # for multiple columns
    
    df['Daily_Return'] = df['Close'].pct_change() #Calculate daily returns
    daily_returns = df['Daily_Return']
    
    weekly_returns = daily_returns.resample('W').sum() #resampling the data to a weekly frequency and summing the daily returns within each week

    return weekly_returns #return a series with date as index and weekly returns as columns


def moving_average(df, col_name, window_size):
        
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce') #Convert numeric column to float

        sma = df[col_name].rolling(window=window_size, min_periods=1).mean() #simple moving average
        ema = df[col_name].ewm(span=window_size, adjust= False).mean() #exponential moving average
              
        moving_averages = pd.DataFrame({'Date':df['Date'], 'SMA':sma, 'EMA':ema})

        return moving_averages #returns a dataframe with col 'SMA' and 'EMA'

print(moving_average(df,'Close', 50).head())
