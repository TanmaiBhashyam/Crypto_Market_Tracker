SELECT
    COUNT(DISTINCT symbol) AS total_coins,
    SUM(market_cap_b) AS total_market_cap_b,
    SUM(volume_24h) AS total_volume_24h,
    AVG(change_24h_pct) AS average_change_24h_pct
FROM crypto_market_history
WHERE extracted_at = (
    SELECT MAX(extracted_at)
    FROM crypto_market_history
);