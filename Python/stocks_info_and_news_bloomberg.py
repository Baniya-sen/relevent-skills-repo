import requests
from datetime import datetime, timedelta
import smtplib
from sys import exit

# Change stock and company name for related info
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."

# Website data API
ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API = "YOUR_NEWSAPI_API_KEY"


def get_stock():
    """Gets info on the stock"""
    alpha_vantage_url = (f"https://www.alphavantage.co/query?"
                         f"function=TIME_SERIES_DAILY&"
                         f"symbol={STOCK}&"
                         f"apikey={ALPHA_VANTAGE_API_KEY}")

    response = requests.get(alpha_vantage_url)
    response.raise_for_status()
    return response.json()


def get_news():
    """Gets news related to parent stock company"""
    newsapi_url = (f'https://newsapi.org/v2/everything?'
                   f'q={COMPANY_NAME}&'
                   f'from={yesterday_date}&'
                   f'sortBy=popularity&'
                   f'apiKey={NEWS_API}')

    response = requests.get(newsapi_url)
    response.raise_for_status()
    return response.json()['articles']


def send_email(change_in_stock, news_data):
    """Sends emails, 1 for sudden price change, and 3 for related news article for that stock"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="YOUR_EMAIL_ADDRESS", password="YOUR_PASSWORD")

        message = (f"Subject: Your stock price just {change_in_stock.split(' ')[1]}!\n\n"
                   f"Your stock '{STOCK}' has a {change_in_stock.split(' ')[0]} "
                   f"of {price_change_percent:,.2}% in a single-intraday.\n"
                   f"Take some time and review your stock for sudden change!")
        connection.sendmail(
            from_addr="YOUR_EMAIL_ADDRESS",
            to_addrs="RECEIVERS_EMAIL",
            msg=message.encode("utf-8")
        )

        for index in range(3):
            # Sends 3 news article to email
            message = (f"Subject: {STOCK}: {change_in_stock.split(' ')[0]}\n\n"
                       f"Headlines: {news_data[index]['title']}\n\n"
                       f"Brief: {news_data[index]['description']}")
            connection.sendmail(
                from_addr="YOUR_EMAIL_ADDRESS",
                to_addrs="RECEIVERS_EMAIL",
                msg=message.encode("utf-8")
            )


# Stock info, yesterday's price
yesterday = 1
stock_info = get_stock()

while True:
    # Get yesterday's and day before yesterday date
    yesterday_date = (datetime.now() - timedelta(days=yesterday)).strftime('%Y-%m-%d')
    day_before_yesterday_date = (datetime.now() - timedelta(days=yesterday+1)).strftime('%Y-%m-%d')

    # Get closing price for both previous days, if fails, shift a day to before
    try:
        previous_day_stock_price = float(
            stock_info["Time Series (Daily)"][yesterday_date]["4. close"]
        )
        day_before_previous_stock_price = float(
            stock_info["Time Series (Daily)"][day_before_yesterday_date]["4. close"]
        )
    except KeyError:
        # If no data available., then print response.json() info and exit
        if "Information" in stock_info:
            print(f"ERROR_INFO: {stock_info['Information']}")
            exit(1)
        else:
            yesterday += 1
            continue

    price_change = previous_day_stock_price - day_before_previous_stock_price
    price_change_percent = (price_change / previous_day_stock_price) * 100
    break

# If percent change is 5% up or below, send email alert
if 0 < price_change > previous_day_stock_price * 0.05:
    change = "🔺 went-up"
    send_email(change, get_news())
elif 0 > price_change < -previous_day_stock_price * 0.05:
    change = "🔻 went-down"
    send_email(change, get_news())
