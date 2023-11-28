from websocket import WebSocketApp
import json
from winotify import Notification
from pyttsx3 import init
import requests

class Currency_Listener():
     def __init__(self,currency,interval):
          self.currency = currency
          self.interval = interval
          pass

currency="wldusdt" 
interval="5m"
stream_name = f"{currency}@kline_{interval}"
raw_stream = f"/ws/{stream_name}"
person = init()
person.say("Hello: hurry up, lets trade")
person.runAndWait()

def on_mesagge(ws,msg):
    tick = json.loads(msg)
    id = "id"
    event_type = str(tick['e'])
    event_time = str(tick['E'])
    symbol = str(tick["s"])
    kline_start_time = str(tick['k']['t'])
    kline_close_time = str(tick['k']['T'])
    kline_symbol = str(tick['k']['s'])
    kline_interval = str(tick['k']['i'])
    kline_first_trade_id = str(tick['k']['f'])
    kline_last_trade_id = str(tick['k']['L'])
    kline_open_price = str(tick['k']['o'])
    kline_close_price = str(tick['k']['c'])
    kline_high_price = str(tick['k']['h'])
    kline_low_price = str(tick['k']['l'])
    kline_base_asset_volume = str(tick['k']['v'])
    kline_number_of_trades = str(tick['k']['n'])
    kline_close = str(tick['k']['x'])
    kline_quote_asset_volume = str(tick['k']['q'])
    kline_taker_buy_base_asset_volume = str(tick['k']['V'])
    kline_taker_buy_quote_asset_volume = str(tick['k']['Q'])
    kline_ignore = str(tick['k']['B'])
    candle_close = tick["k"]["x"]
    kline = {
         "id": id,
         "event_type": event_type,
         "event_time": event_time,
         "symbol": symbol,
         'kline_start_time': kline_start_time,
         "kline_close_time": kline_close_time,
         "kline_symbol": kline_symbol,
         "kline_interval": kline_interval,
         "kline_first_trade_id": kline_first_trade_id,
         "kline_last_trade_id": kline_last_trade_id,
         "kline_open_price": kline_open_price,
         "kline_close_price": kline_close_price,
         "kline_high_price": kline_high_price,
         "kline_low_price": kline_low_price,
         "kline_base_asset_volume": kline_base_asset_volume,
         "kline_number_of_trades": kline_number_of_trades,
         "kline_close": kline_close,
         "kline_quote_asset_volume": kline_quote_asset_volume,
         "kline_taker_buy_base_asset_volume": kline_taker_buy_base_asset_volume,
         "kline_taker_buy_quote_asset_volume": kline_taker_buy_quote_asset_volume,
         "kline_ignore": kline_ignore
    }
    op = float(tick["k"]["o"])
    cp = float(tick["k"]["c"])
    f_1 = cp * 100 
    f_2 = f_1 / op
    f_3 = 100 - f_2
    f_4 = -1 * f_3
    toast = Notification(
    app_id=f"{symbol}",
    title="Notification",
    msg=f" Variation: {f_4}: interval: {interval}",
    duration="long"
)
    toast.add_actions(label="Go to futures", launch=f"https://www.binance.com/es-AR/futures/{symbol}")
    
    if candle_close: 
         requests.post("http://localhost:8000/generate", json=kline)
         print(f_4)
         """ toast.show() """
""" {
  "e": "kline",         // Event type // event_type
  "E": 1672515782136,   // Event time // event_time
  "s": "BNBBTC",        // Symbol //symbol
  "k": { // kline
    "t": 1672515780000, // Kline start time // kline_start_time
    "T": 1672515839999, // Kline close time // kline_close_time
    "s": "BNBBTC",      // Symbol // kline_symbol
    "i": "1m",          // Interval // kline_interval
    "f": 100,           // First trade ID // kline_first_trade_id
    "L": 200,           // Last trade ID // kline_last_trade_id
    "o": "0.0010",      // Open price // kline_open_price
    "c": "0.0020",      // Close price // kline_close_price
    "h": "0.0025",      // High price // kline_high_price
    "l": "0.0015",      // Low price // kline_low_price
    "v": "1000",        // Base asset volume // kline_base_asset_volume
    "n": 100,           // Number of trades // kline_number_of_trades
    "x": false,         // Is this kline closed? // kline_close
    "q": "1.0000",      // Quote asset volume //kline_quote_asset_volume
    "V": "500",         // Taker buy base asset volume // kline_taker_buy_base_asset_volume
    "Q": "0.500",       // Taker buy quote asset volume // kline_taker_buy_quote_asset_volume
    "B": "123456"       // Ignore // kline_ignore
  }
} """



base_url = f"wss://stream.binance.com:9443{raw_stream}"
ws = WebSocketApp(base_url,on_message=on_mesagge)
ws.run_forever()



toast = Notification(
    app_id="TEST",
    title="Test Title",
    msg="Olis",
    duration="short"
)

toast.add_actions(label="Click Me", launch="https://www.youtube.com/watch?v=5EHEG4gMCNs")

# toast.show()