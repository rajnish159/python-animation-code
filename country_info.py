from countryinfo import CountryInfo
count = input("Enter your Country Name : ")
country = CountryInfo(count)
print("capital is : ", country.capital())
print("currencies is : ", country.currencies())
print("language is : ", country.languages())
print("borders is : ", country.borders())
print("others name is : ", country.alt_spellings())
