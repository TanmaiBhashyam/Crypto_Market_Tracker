-- Top cryptocurrencies by 24-hour percentage gain

SELECT name, symbol, price_usd, change_24h_pct, market_cap_b
FROM crypto_market_history
WHERE extracted_at = (
    SELECT MAX(extracted_at)
    FROM crypto_market_history
)
ORDER BY change_24h_pct DESC
LIMIT 10;