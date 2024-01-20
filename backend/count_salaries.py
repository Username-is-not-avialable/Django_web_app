import csv, requests
from xml.dom import minidom
import datetime
import time


def get_salary_mean(line: list[str]) -> float:
    return (float(line[2]) + float(line[3])) / 2


def have_salary(line: list[str]) -> bool:
    try:
        return line[2] != '' and line[3] != ''
    except:
        print("Incorrect line!")
        print(line)


def get_year(line):
    return int(line[-1][:4])


def format_date(str_date):
    date = datetime.datetime.strptime(str_date, '%Y-%m')
    return date.strftime('%m/%Y')


def get_exchange_rate(currency: str, date: str, dom: minidom) -> float:
    CURRENCY_NAME_TO_ID = {
        'EUR': 'R01239',
        'UAH': "R01720",
        'USD': "R01235",
        'KZT': "R01335",
        'AZN': "R01020A",
        "UZS": "R01717",
        "BYR": "R01090",
        "KGS": "R01370",
        'GEL': "R01210"
    }
    if currency in ['', 'RUR']: return 1
    currency_id = CURRENCY_NAME_TO_ID[currency]

    valutes = dom.getElementsByTagName('Valute')
    for valute in valutes:
        if valute.getAttribute('ID') == currency_id:
            exchangeRate = float(valute.childNodes[4].firstChild.nodeValue.replace(',', '.')) / float(
                valute.childNodes[2].firstChild.nodeValue.replace(',', '.'))
    if 'exchangeRate' not in locals():  # если валюты не оказалось в ответе сервера, то она не определена -> примем exRate=1
        exchangeRate = 1
        print(currency, date)
    return exchangeRate


def get_currencies_by_date(date: str) -> minidom:
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/' + date
    response = requests.get(URL)
    try:
        dom = minidom.parseString(response.content)
    except SyntaxError:
        time.sleep(2)
        dom = minidom.parseString(response.content)
    return dom


def get_currency_story():
    CURRENCIES = ['', 'EUR', 'RUR', 'GEL', 'UAH', 'USD', 'KZT', 'AZN', 'UZS', 'BYR', 'KGS']
    exchange_rates = {cur: dict() for cur in CURRENCIES}
    for year in range(2003, 2024):
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            date = f'{date:%m/%Y}'
            dom = get_currencies_by_date(date)
            for currency in CURRENCIES:
                exchange_rates[currency][date] = get_exchange_rate(currency, date, dom)
    return exchange_rates


with open("1C-vacancies.csv", 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    sum_salaries_by_years = {year: 0 for year in range(2003, 2024)}
    count_salaries_by_years = {year: 0 for year in range(2003, 2024)}
    EXCHANGE_RATES = get_currency_story()
    for line in reader:
        if have_salary(line):
            salary_mean = get_salary_mean(line)
            currency = line[4]
            salary_mean_rub = salary_mean * EXCHANGE_RATES[currency][format_date(line[-1][:7])]
            sum_salaries_by_years[get_year(line)] += salary_mean_rub
            count_salaries_by_years[get_year(line)] += 1

mean_salaries_by_year = dict()
for year in range(2005, 2024):
    mean_salaries_by_year[year] = sum_salaries_by_years[year] / count_salaries_by_years[year]
print(mean_salaries_by_year)


