import numpy as np
import pandas as pd


def calculate_returns(close_prices):
    if close_prices is None or close_prices.empty:
        raise ValueError("Close prices cannot be empty.")

    returns = close_prices.pct_change().dropna()

    if returns.empty:
        raise ValueError("Returns could not be calculated from close prices.")

    return returns


def calculate_portfolio_return(returns, weights):
    if returns.empty:
        raise ValueError("Returns data cannot be empty.")

    weights = np.array(weights)

    if len(weights) != returns.shape[1]:
        raise ValueError("Number of weights must match number of assets.")

    if not np.isclose(weights.sum(), 1):
        raise ValueError("Portfolio weights must sum to 1.")

    return returns.dot(weights)


def calculate_max_drawdown(cumulative_returns):
    if cumulative_returns.empty:
        raise ValueError("Cumulative returns cannot be empty.")

    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - running_max) / running_max

    return drawdown.min()