import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sp500 = yf.Ticker("^GSPC")
df = sp500.history(start="2010-01-01", end="2025-07-03")[["Close"]].dropna()
df.index = pd.to_datetime(df.index).tz_localize(None)
all_bd = pd.date_range(df.index.min(), df.index.max(), freq="B")
df = df.reindex(all_bd)
df["Close"].ffill(inplace=True)

# plot train and test data with differnt color and dash line between
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(df.index, df["Close"], label="Close price", color="black")

# Year 2017
ax.axvline(x=pd.to_datetime("2017-01-01"),
           color="green",
           linestyle="--",
           linewidth=1,
           label="Year 2017")
ax.axvline(x=pd.to_datetime("2018-01-01"),
           color="green",
           linestyle="--",
           linewidth=1)
ax.plot(df.loc["2017-01-01":"2018-01-01", "Close"].index, df.loc["2017-01-01":"2018-01-01", "Close"], color='green')

# Year 2023 - 2024
ax.axvline(x=pd.to_datetime("2023-01-01"),
           color="orange",
           linestyle="--",
           linewidth=1,
           label="Year 2023-24")
ax.axvline(x=pd.to_datetime("2025-01-01"),
           color="orange",
           linestyle="--",
           linewidth=1)
ax.plot(df.loc["2023-01-01":"2025-01-01", "Close"].index, df.loc["2023-01-01":"2025-01-01", "Close"], color='orange')

# back test
ax.axvline(x=pd.to_datetime("2016-01-01"),
           color="red",
           linestyle=":",
           linewidth=1,
           label="Backtest start")

ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
ax.set_title("Sp500 Data with testing sections")
ax.legend()
plt.show()