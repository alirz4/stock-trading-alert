import requests


def get_news_data(company_name, api_key):
    """

    :param company_name:
    :param api_key:
    :return: top 5 articles and news about company
    """
    message_list = []
    params = {
        'q': company_name,
        'apiKey': api_key
    }
    news_endpoint = requests.get("https://newsapi.org/v2/everything", params=params)
    news_endpoint.raise_for_status()
    head_line_list = news_endpoint.json()['articles']
    for i in range(5):
        message_list.append((head_line_list[i]['source']['name'], head_line_list[i]['title']))

    return message_list
