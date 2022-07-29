# importing the libraries
from bs4 import BeautifulSoup as bs
import requests


url="https://dsebd.org/dseX_share.php"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = bs(html_content, "lxml")
# print(type(soup.prettify())) # print the parsed data of html
table_of_content = soup.find('div',{'class':'table-responsive'})

table_list  = [[cell.text.strip() for cell in row('td')] for row in table_of_content('tr')]
table_list.pop(0)
