## Production Readiness Improvements

Based on interim feedback, the project was improved by moving reusable logic into the `src/` folder:

- `src/data_loader.py`: handles Yahoo Finance data extraction with error handling
- `src/risk_metrics.py`: calculates daily returns, VaR, and Sharpe Ratio
- `src/model_utils.py`: contains forecasting evaluation and LSTM sequence preparation utilities

This improves maintainability, reduces repeated notebook code, and makes the workflow closer to a production-ready analytical pipeline.