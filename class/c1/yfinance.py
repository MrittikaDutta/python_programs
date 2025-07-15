
# Import yfinance package
import yfinance as yf
# Set the start and end date
start_date = '2022-01-01'
end_date = '2022-04-03'
# Set the ticker
ticker = 'RELIANCE.NS'
# Get the data
data = yf.download(ticker, start_date, end_date)
# Print 5 rows
data.tail()
#install yfinance
wite command on cmd ----- pip install yfinance
# Import yfinance package
import yfinance as yf
# Set the start and end date
start_date = '2022-01-01'
end_date = '2022-04-03'
# Set the ticker
ticker = 'RELIANCE.NS'
# Get the data
data = yf.download(ticker, start_date, end_date)
# Print 5 rows
data.tail()
# Import matplotlib for plotting
import matplotlib.pyplot as plt
%matplotlib inline
# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()
# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.show()
# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()
# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.show()