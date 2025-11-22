import numpy as np
import requests
import json

with open("tools/instruments.json") as f:
    instruments = json.load(f)

class GetValues:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "<GetValues – type obj.help() for usage>"
    
    def get_isin(self, symbol):
        for instrument in instruments:
            if instrument['trading_symbol'] == symbol:
                return instrument['isin']
        return "Instrument not found"
    
    def get_instrument_name(self, isin):
        for instrument in instruments:
            if instrument['isin'] == isin:
                return instrument['name']
        return "Instrument not found"

    def get_readings(self, instrument, period, interval, trade_type, start_date, end_date):
        self.instrument = instrument
        self.interval = interval
        self.period = period
        self.interval = interval
        self.trade_type = trade_type
        self.start_date = start_date
        self.end_date = end_date
        self.url = self.construct_url()
        self.headers = {'Accept': 'application/json'}
        if self.trade_type == "historical" and (self.start_date == "YYYY-MM-DD" or self.end_date == "YYYY-MM-DD"):
            return {"status": "error", "message": "For historical trade type, start_date and end_date must be provided."}
        self.candles_array = self.fetch_data()
        return self.candles_array

    @staticmethod
    def help():
        get_readings_args = {
            '   --instrument': 'The instrument token or symbol (e.g., INE560A01023).',
            '   --period    ': 'The time period for the data (e.g., "minutes", "days").',
            '   --interval  ': 'The interval for the data (e.g., 1 for 1-minute candles).',
            '   --trade_type': 'Type of trade data: "intraday" or "historical".',
            '   --start_date': 'Start date for historical data (YYYY-MM-DD). Enter None for intraday.',
            '   --end_date  ': 'End date for historical data (YYYY-MM-DD). Enter None for intraday.'
        }
        print("\nGetValues Class - Implementation using Upstox API")
        print("\nDocumentation Link: https://upstox.com/developer/api-documentation/v3/get-historical-candle-data")
        print("\nMethods:\n\n  Arguments:\n")
        for key, value in get_readings_args.items():
            print(f"{key} \t\t {value}")
        print("\n")

    def construct_url(self):
        base_url = 'https://api.upstox.com/v3/historical-candle/'
        if self.trade_type == "intraday":
            return f"{base_url}intraday/NSE_EQ%7C{self.instrument}/{self.period}/{self.interval}"
        else:
            return f"{base_url}NSE_EQ%7C{self.instrument}/{self.period}/{self.interval}/{self.end_date}/{self.start_date}"

    def fetch_data(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            candles_data = np.array(response.json()['data']['candles'])
            dtype = [('timestamp', 'U25'), ('open', float), ('high', float), 
                    ('low', float), ('close', float), ('volume', int), ('open_interest', int)]
            output = np.array([tuple(candle) for candle in candles_data], dtype=dtype)
            out = [ {col: row[col] for col in output.dtype.names} for row in output ]
            return out
        else:
            status_code = response.status_code
            if response.text:
                op = response.json()
                op['status_code'] = status_code
                return op
            else:
                return {'status_code': status_code, 'message': 'No response text'}