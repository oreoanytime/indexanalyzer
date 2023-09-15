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