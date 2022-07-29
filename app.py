import os
import flask
from flask import request, jsonify,render_template

from getting_values_v2 import stocks_details_dic

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.



@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# A route to return all of the available entries in our catalog.
@app.route('/stocks/all', methods=['GET'])
def api_all():
    return jsonify(stocks_details_dic())

@app.route('/stocks',methods=['GET'])
def api_id():
    if 'code' in request.args:
        return jsonify([stock for stock in stocks_details_dic() if stock['Code'] == request.args['Code']])
    elif 'ID' in request.args:
        return jsonify([stock for stock in stocks_details_dic() if stock['ID'] == request.args['ID']])
    else: return 'This feild of search is not supported by this api'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)