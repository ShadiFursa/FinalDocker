import requests
from flask import Flask


# This is the HTML Template for the web application
template = """<!DOCTYPE html>
<html>
<head>
    <title>Bitcoin</title>
</head>
<body>
<h1 style="text-align:center">Bitcoin Values</h1>
<p>This is a Web Application that shows the bitcoin latest value and average over the last 10 minutes</p>
<h2>The current BTC value in USD:$$replace_this1$$</h2>
<h2>The Average value of BTC over the last 10 minutes in USD: $$replace_this2$$ </h2>
<img src="https://i.ytimg.com/vi/KARxDX5DTgY/maxresdefault.jpg" width="250" height="150">
</body>
</html>"""

app = Flask(__name__)

## the URL for the crypto currency API
URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym={}&limit={}"


# extract the value of bitcoin over the last 10 minutes and calculate average
def get_price(coin,currency,limit):
    sum = 0
    try:
        response = requests.get(URL.format(coin,currency,limit)).json()
        for i in range(10):
            sum += response['Data']['Data'][i]['close']
        # return the current value and the average over the last 10 minutes
        return response['Data']['Data'][9]['close'],sum/10
    except:
        return False


@app.route("/")
def firstpage():
    #grab the data, add them to the inline html file and return the result
    currentprice,average= get_price("BTC","USD","10")
    html_result = template.replace("$$replace_this1$$", str(currentprice))
    html_result = html_result.replace("$$replace_this2$$",str(average))
    return html_result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)