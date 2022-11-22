# Fanos

Fanos, at the moment, is an Ethereum price prediction tool written in Python.
<br>
<br>
<a href="https://facebook.github.io/prophet/" target="_blank">Prophet</a> is open source software for forecasting time series data,
<br>released by Facebook’s Core Data Science team.
<br>
<br>
To get the data on Ethereum prices, we’ll be using the <a href="https://pypi.org/project/yfinance/" target="_blank">yfinance</a> library,
<br>
which is a Yahoo! Finance market data downloader.

## Installation

Use the package manager <a href="https://pip.pypa.io/en/stable/" target="_blank">pip</a> to install the necessary packages for Fanos.


```bash
pip install -r requirements.txt
```

## Usage

Run the app(CMD + R) and it will open two ports in your localhost.
<br>
<br>
One includes the prediction from today to a year based on the current trend,
<br>
yeap I know not very sophisticated at the moment...
<br>
<br>
And the other model, includes growth curve trend, weekly seasonal, and yearly seasonal components.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)