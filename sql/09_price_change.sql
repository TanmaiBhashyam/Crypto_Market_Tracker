SELECT symbol, extracted_at, price_usd,
    LAG(price_usd) OVER (
        PARTITION BY symbol
        ORDER BY extracted_at
    ) AS previous_price

FROM crypto_market_history
ORDER BY symbol, extracted_at;