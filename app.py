from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates


app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
app.jinja_env.filters['zip'] = zip

c = CurrencyRates()
currency = ['GBP', 'HKD', 'IDR', 'ILS', 'DKK', 'INR', 'CHF', 'MXN', 'CZK', 'SGD', 'THB', 'HRK', 'EUR', 'MYR', 'NOK', 'CNY', 'BGN', 'PHP', 'PLN', 'ZAR', 'CAD', 'ISK', 'BRL', 'RON', 'NZD', 'TRY', 'JPY', 'RUB', 'KRW', 'USD', 'AUD', 'HUF', 'SEK']

currency_fullforms = ["Great Britain Pound", "Hong Kong Dollar", "Indonesian rupiah","Israeli New Shekel", "Danish Krone", "Indian Rupee", "Swiss Franc", "Mexican Peso", "Czech Koruna", "Singapore Dollar", "Thai Onshore Baht", "Croatian Kuna", "Euro", "Malaysian Ringgit", "Norwegian Krone", "Chinese Yuan Renminbi", "Bulgarian Lev", "Philippine Peso", "Polish Zloty", "South African Rand", "Canadian Dollar", "Iceland Krona", "Brazilian Real", "Romanian New Leu", "New Zealand Dollar", "Turkish Lira", "Japanese Yen", "Russian Ruble", "Korean Won", "United States Dollar", "Australian Dollar", "Hungarian Forint", "Swedish Krona"]
tup1 = tuple(currency)
tup2 = tuple(currency_fullforms)

@app.route('/')
def home():
	return render_template('index.html', currency=currency, shortForm=currency, fullForm=currency_fullforms)

@app.route('/', methods=['GET', 'POST'])
def converter():
	if request.method == "POST":
		dd_1 = request.form["dd-1"]
		dd_2 = request.form["dd-2"]
		value = request.form["number"]

		
		if dd_1 == "null" or dd_2 == "null":
			return render_template('index.html', error = "Select A Currency For Conversion", currency=currency, shortForm=currency, fullForm=currency_fullforms)
		try:
			num = float(value)
			given_curr = c.get_rates(dd_1)
			required_curr = num * given_curr[dd_2]
			msg = value + " " + dd_1 + " = " + str(required_curr) + " " + dd_2
			print(len(currency))
			print(len(currency_fullforms))

			

			return render_template('index.html', msg = msg, currency=currency, shortForm=currency, fullForm=currency_fullforms)
		except ValueError:
			return render_template('index.html', error = "Please Enter A Valid Number", currency=currency, shortForm=currency, fullForm=currency_fullforms)
		except:
			return render_template('index.html', error = "Please Check Your Internet Connection And Try Again", currency=currency, shortForm=currency, fullForm=currency_fullforms)

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)