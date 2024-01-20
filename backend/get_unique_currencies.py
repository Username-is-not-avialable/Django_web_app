import csv


def get_unique_currencies():
    with open('cleaned_vacancies.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        currencies = set()
        next(reader)  # skip 1st line with columns names
        for line in reader:
            currencies.add(line[4])
    return currencies


print(get_unique_currencies())
