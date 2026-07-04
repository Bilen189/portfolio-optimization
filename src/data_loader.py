import pandas as pd
import yfinance as yf


def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical financial data from Yahoo Finance.
    """
    data = {}

    for ticker in tickers:
        try:
            df = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                progress=False,
                auto_adjust=False
            )

            if df.empty:
                raise ValueError(f"No data returned for {ticker}")

            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.droplevel(1)

            df["Ticker"] = ticker
            data[ticker] = df

        except Exception as error:
            print(f"Error loading {ticker}: {error}")

    return data