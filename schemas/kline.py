def klineEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "event_type": item["event_type"],
        "event_time": item["event_time"],
        "symbol": item["symbol"],
        "kline_start_time": item["kline_start_time"],
        "kline_close_time": item["kline_close_time"],
        "kline_symbol": item["kline_symbol"],
        "kline_interval": item["kline_interval"],
        "kline_first_trade_id": item["kline_first_trade_id"],
        "kline_last_trade_id": item["kline_last_trade_id"],
        "kline_open_price": item["kline_open_price"],
        "kline_close_price": item["kline_close_price"],
        "kline_high_price": item["kline_high_price"],
        "kline_low_price": item["kline_low_price"],
        "kline_base_asset_volume": item["kline_base_asset_volume"],
        "kline_number_of_trades": item["kline_number_of_trades"],
        "kline_close": item["kline_close"],
        "kline_quote_asset_volume": item["kline_quote_asset_volume"],
        "kline_taker_buy_base_asset_volume": item["kline_taker_buy_base_asset_volume"],
        "kline_taker_buy_quote_asset_volume": item["kline_taker_buy_quote_asset_volume"],
        "kline_ignore": item["kline_ignore"]
    }

def klinesEntity(entity) -> list:
    return [klineEntity(item) for item in entity]