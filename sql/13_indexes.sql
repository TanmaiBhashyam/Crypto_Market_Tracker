CREATE INDEX IF NOT EXISTS idx_crypto_market_extracted_at
ON crypto_market_history (extracted_at);

CREATE INDEX IF NOT EXISTS idx_crypto_market_symbol_time
ON crypto_market_history (symbol, extracted_at);