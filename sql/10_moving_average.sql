SELECT symbol, extracted_at, price_usd,
    AVG(price_usd) OVER (
        PARTITION BY symbol
        ORDER BY extracted_at
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3

FROM crypto_market_history
ORDER BY symbol, extracted_at;