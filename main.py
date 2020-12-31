from flask import Flask, jsonify
from tradingview_ta import TA_Handler, Interval


app = Flask(__name__)


@app.route('/<stock>/<exchange>/<country>')
def indicators_data(stock, exchange, country):
    handler = TA_Handler()
    handler.set_symbol_as(stock)
    handler.set_exchange_as_crypto_or_stock(exchange)
    handler.set_screener_as_stock(country)
    handler.set_interval_as(Interval.INTERVAL_1_WEEK)
    analysis_one = handler.get_analysis()
    all_indicators = analysis_one.indicators
    json_file = {'query': all_indicators}
    return jsonify(json_file)


if __name__ == '__main__':
    app.run()
