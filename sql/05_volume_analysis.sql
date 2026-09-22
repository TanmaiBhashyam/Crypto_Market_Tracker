-- Cryptocurrencies with the highest 24-hour trading volume

SELECT name, symbol, volume_24h, price_usd, change_24h_pct
FROM crypto_market_history
WHERE extracted_at = (
    SELECT MAX(extracted_at)
    FROM crypto_market_history
)
ORDER BY volume_24h DESC
LIMIT 10;