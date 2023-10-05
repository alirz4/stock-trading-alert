import smtplib
import os

from news_data import get_news_data
from stock_data import get_stock_data

YOUR_EMAIL = os.environ.get('EMAIL_STOCK')
YOUR_PASSWORD = os.environ.get('E_PASSWORD_STOCK')
COMPANY_NAME = os.environ.get('COMPANY_NAME')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
STOCK = os.environ.get('STOCK')
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')

diff_perc = get_stock_data(api_key=STOCK_API_KEY, stock_name=STOCK)[0]
if diff_perc > 5:
    data = get_news_data(company_name=COMPANY_NAME, api_key=NEWS_API_KEY)
    message = f'{diff_perc}\n'
    for text in data:
        message += f'{text[0]}: {text[1]}\n'
    print(message)
    with smtplib.SMTP('YOUR EMAIL PROVIDER SMTP SERVER ADDRESS') as conn:
        conn.starttls()
        conn.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
        conn.sendmail(from_addr=YOUR_EMAIL,
                      to_addrs=YOUR_EMAIL,
                      msg=message)
