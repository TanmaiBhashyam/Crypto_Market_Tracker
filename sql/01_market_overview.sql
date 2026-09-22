-- Latest crypto market snapshot

SELECT name, symbol, price_usd, market_cap_b, volume_24h, change_24h_pct, trend, extracted_at
FROM crypto_market_history
WHERE extracted_at = (
    SELECT MAX(extracted_at)
    FROM crypto_market_history
)
ORDER BY market_cap_b DESC;