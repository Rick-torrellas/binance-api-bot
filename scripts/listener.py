from websocket import WebSocketApp
import json
from winotify import Notification
from pyttsx3 import init

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
    symbol = tick["s"]
    candle_close = tick["k"]["x"]
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
         print(f_4)
         toast.show()
""" {
  "e": "kline",         // Event type // event_type
  "E": 1672515782136,   // Event time // event_time
  "s": "BNBBTC",        // Symbol //symbol
  "k": { // kline
    "t": 1672515780000, // Kline start time // kline_start_time
    "T": 1672515839999, // Kline close time // kline_close_time
    "s": "BNBBTC",      // Symbol // symbol
    "i": "1m",          // Interval // interval
    "f": 100,           // First trade ID // first_trade_id
    "L": 200,           // Last trade ID // last_trade_id
    "o": "0.0010",      // Open price // open_price
    "c": "0.0020",      // Close price // close_price
    "h": "0.0025",      // High price // high_price
    "l": "0.0015",      // Low price // low_price
    "v": "1000",        // Base asset volume // base_asset_volume
    "n": 100,           // Number of trades // number_of_trades
    "x": false,         // Is this kline closed? // kline_close
    "q": "1.0000",      // Quote asset volume //quote_asset_volume
    "V": "500",         // Taker buy base asset volume // taker_buy_base_asset_volume
    "Q": "0.500",       // Taker buy quote asset volume // taker_buy_quote_asset_volume
    "B": "123456"       // Ignore // ignore
  }
} """



base_url = f"wss://stream.binance.com:9443{raw_stream}"
ws = WebSocketApp(base_url,on_message=on_mesagge)
# ws.run_forever()



toast = Notification(
    app_id="TEST",
    title="Test Title",
    msg="Olis",
    duration="short"
)

toast.add_actions(label="Click Me", launch="https://www.youtube.com/watch?v=5EHEG4gMCNs")

# toast.show()