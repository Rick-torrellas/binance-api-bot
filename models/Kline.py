from typing  import Optional,Dict
from pydantic import BaseModel

class Kline(BaseModel):
    id: Optional[str] = None
    event_type: str
    event_time: str
    symbol: str
    kline_start_time: str
    kline_close_time: str
    kline_symbol: str
    kline_interval: str
    kline_first_trade_id: str
    kline_last_trade_id: str
    kline_open_price: str
    kline_close_price: str
    kline_high_price: str
    kline_low_price: str
    kline_base_asset_volume: str
    kline_number_of_trades: str
    kline_close: str
    kline_quote_asset_volume: str
    kline_taker_buy_base_asset_volume: str
    kline_taker_buy_quote_asset_volume: str
    kline_ignore: str
""" a = User(event_time="d",event_type="asd",symbol="dasda",kline={
    'a': {
        "interval": "dasd",
        "first_trade_id": "dasd",
        "last_trade_id": "dasd",
        "open_price": "dasd",
        "close_price": "dasd",
        "high_price": "dasd",
        "low_price": "dasd",
        "base_asset_volume": "dasd",
        "number_of_trades": "dasd",
        "kline_close": "dasd",
        "quote_asset_volume": "dasd",
        "taker_buy_base_asset_volume": "dasd",
        "taker_buy_quote_asset_volume": "dasd"
    }
}) # type: ignore

print(a.model_dump()) """