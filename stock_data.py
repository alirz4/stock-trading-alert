import requests


def get_stock_data(stock_name, api_key):
    """

    :param stock_name:
    :param api_key:
    :return: [ (PERCENTAGE) of price in yesterday and the day before yesterday ,
     (VALUE) of price in yesterday and the day before yesterday]
    """
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stock_name,
        'apikey': api_key
    }

    stock_endpoint = requests.get("https://www.alphavantage.co/query", params=params)
    stock_endpoint.raise_for_status()
    days = stock_endpoint.json()['Time Series (Daily)']
    days_list = [value for (key, value) in days.items()]

    yesterday = days_list[0]
    yesterday_closing_price = yesterday['4. close']

    day_before_yesterday = days_list[1]
    day_before_yesterday_closing_price = day_before_yesterday['4. close']

    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    # print(difference)
    diff_percentage = round((difference / float(yesterday_closing_price)) * 100)
    # print(diff_percentage)
    return [diff_percentage, difference]
