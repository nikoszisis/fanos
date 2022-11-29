from flask import Flask
import pandas as pd
import yfinance as yf
from datetime import datetime
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings as warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

today = datetime.today().strftime('%Y-%m-%d')
start_date = '2016-01-01'
eth_df = yf.download('ETH-USD', start_date, today)

eth_df.reset_index(inplace=True)

df = eth_df[["Date", "Open"]]
new_names = {
    "Date": "ds",
    "Open": "y",
}
df.rename(columns=new_names, inplace=True)

# plot the open price

x = df["ds"]
y = df["y"]

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y))

# Set title
fig.update_layout(
    title_text="Time series plot of Ethereum Open Price",
)

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
        rangeslider=dict(visible=True),
        type="date",
    )
)

m = Prophet(
    seasonality_mode="multiplicative"
)
m.fit(df)

future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)

plot = plot_plotly(m, forecast)
componentsPlot = plot_components_plotly(m, forecast)

plot.show()

app = Flask(__name__)
componentsPlot.show()


@app.route('/')
def home():
    return "Homepage"


@app.route('/fanos')
def components():
    return "Fanos"
