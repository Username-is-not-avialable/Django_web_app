import csv

file_name = r"cleaned_vacancies.csv"

with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    line1 = next(reader)
    vacancies_by_years = {i:0 for i in range(2003,2024)}
    for line in reader:
        year = int(line[-1][:4])
        vacancies_by_years[year] += 1
    print(vacancies_by_years)
