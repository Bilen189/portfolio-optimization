import yfinance as yf
import pandas as pd


def download_market_data(tickers, start_date, end_date):
    if not tickers:
        raise ValueError("Ticker list cannot be empty.")

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=False
    )

    if data.empty:
        raise ValueError("No data was downloaded. Check tickers or date range.")

    if "Close" not in data.columns:
        raise ValueError("Downloaded data must contain Close prices.")

    close_prices = data["Close"]

    if close_prices.isnull().all().all():
        raise ValueError("Close price data contains only missing values.")

    return close_prices.dropna()