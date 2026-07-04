import numpy as np


def calculate_daily_returns(price_series):
    return price_series.pct_change().dropna()


def calculate_var(returns, confidence_level=0.95):
    return np.percentile(returns, (1 - confidence_level) * 100)


def calculate_sharpe_ratio(returns, risk_free_rate=0.02, trading_days=252):
    annual_return = returns.mean() * trading_days
    annual_volatility = returns.std() * np.sqrt(trading_days)

    if annual_volatility == 0:
        return np.nan

    return (annual_return - risk_free_rate) / annual_volatility