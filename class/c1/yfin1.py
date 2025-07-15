import yfinance as yf
start_date='2022-01-01'
end_date='2022-04-03'
# Get the data
data = yf.download(ticker, start_date, end_date)
# Print 5 rows
data.tail()
# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()
# Import matplotlib for plotting
import matplotlib.pyplot as plt
%matplotlib inline
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
import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

# Customize the layout
fig.update_layout(
    title='Candlestick Chart for %s' % ticker,
    xaxis_title='Date',
    yaxis_title='Price',
    template='plotly_dark'  # You can change the template if you prefer a different style
)

# Show the chart
fig.show()
