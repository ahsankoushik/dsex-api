# importing the libraries
from bs4 import BeautifulSoup as bs
import requests


def stocks_details_dic() -> list:
    '''Returns the contents of dsex in list'''

    url="https://dsebd.org/dseX_share.php"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = bs(html_content, "lxml")

    table_of_content = soup.find('div',{'class':'table-responsive'})

    table_list = [] 

    headers = ['ID','Code','ltp','high','low','closep*','ycp*','change','trade','value(mm)','volume']

    for row in table_of_content('tr'):
        table_list += [{}]
        header = 0
        for cell in row('td'):
            table_list[-1][headers[header]]= cell.text.strip()
            header += 1
    table_list.pop(0)

    return table_list











