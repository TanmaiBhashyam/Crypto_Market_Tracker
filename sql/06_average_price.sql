SELECT symbol,
    AVG(price_usd) AS average_price,
    MIN(price_usd) AS minimum_price,
    MAX(price_usd) AS maximum_price
FROM crypto_market_history
GROUP BY symbol
ORDER BY average_price DESC;