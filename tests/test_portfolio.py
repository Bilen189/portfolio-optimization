import pytest
import pandas as pd
import numpy as np

from src.portfolio import (
    calculate_returns,
    calculate_portfolio_return,
    calculate_max_drawdown
)


def test_calculate_returns_not_empty():
    prices = pd.DataFrame({
        "SPY": [100, 101, 102],
        "BND": [80, 81, 82]
    })

    returns = calculate_returns(prices)

    assert not returns.empty


def test_portfolio_weights_sum_to_one():
    returns = pd.DataFrame({
        "SPY": [0.01, 0.02],
        "BND": [0.005, 0.003]
    })

    weights = [0.6, 0.4]

    portfolio_returns = calculate_portfolio_return(returns, weights)

    assert len(portfolio_returns) == len(returns)


def test_invalid_weights_raise_error():
    returns = pd.DataFrame({
        "SPY": [0.01, 0.02],
        "BND": [0.005, 0.003]
    })

    weights = [0.7, 0.7]

    with pytest.raises(ValueError):
        calculate_portfolio_return(returns, weights)


def test_max_drawdown_calculation():
    cumulative_returns = pd.Series([1.0, 1.2, 0.9, 1.1])

    max_drawdown = calculate_max_drawdown(cumulative_returns)

    assert max_drawdown < 0