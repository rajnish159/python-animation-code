from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("enter the amount : "))
from_currency = input("from Currency: ").upper()
to_currency = input("To currency: ").upper()
print(from_currency, " to ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)