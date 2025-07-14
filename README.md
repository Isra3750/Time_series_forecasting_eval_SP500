# S&P 500 Time Series Forecasting

**Ten models, one index.**  
Simple experiments comparing classical statistics, probabilistic, machine learning and deep learning approaches for long-term S&P 500 price forecasting.

All 10 models are implemented with the Darts library for a consistent API and evaluation protocol.

Three evaluation approach:
- Pre-Covid: train 2010-16, test 2017
- Post-Covid: train 2012-22, test 2023-24
- Walk-forward 2024: rolling 1-week-ahead back-test

Metrics: MAE, RMSE, MAPE.

Hyper-parameters kept minimal (defaults + season_length = 52) so results reflect baseline behaviour.
