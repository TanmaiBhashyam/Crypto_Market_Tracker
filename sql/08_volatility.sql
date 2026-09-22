SELECT symbol, STDDEV_SAMP(change_24h_pct) AS change_volatility
FROM crypto_market_history
GROUP BY symbol
ORDER BY change_volatility DESC;