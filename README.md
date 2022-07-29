# stocks
### A Custom made api build using web scraping.
Tool Used <br>
* BeautifulSoup 
* flask
* requests
* gunicorn (For hosting on Heroku)

This app shows the stocks value from [DSEX](https://dsebd.org/dseX_share.php)(Dhaka Stock Exchange)

**It Has a limited amount of delay**
The values are in the time range of you hiting the api and you getting the values.<br>
[live demo](https://dsex-api.herokuapp.com)


**Screenshots**
![API main page](/screenshoots/main_page.png "Main Page")
![API ALL](/screenshoots/api_all.png "All Stocks")
![Search by id](screenshoots/search_by_id.png "search using id")
![Search by code](screenshoots/search_by_code.png "Search using code")

### Devolopment
install the requiremnets
```
pip install -r requirements.txt
python3 app.py
```


