import csv

with open(r"C:\Users\Minty\Downloads\vacancies.csv", 'r', encoding='utf-8-sig') as file:
    with open("1C-vacancies.csv", 'w', encoding='utf-8', newline='') as output:
        reader = csv.reader(file)
        writer = csv.writer(output)
        writer.writerow(next(reader))

with open(r"C:\Users\Minty\Downloads\vacancies.csv", 'r', encoding='utf-8-sig') as file:
    with open("1C-vacancies.csv", 'a', encoding='utf-8', newline='') as output:
        reader = csv.reader(file)
        writer = csv.writer(output)
        vac_names = []
        for row in reader:
            name = row[0].lower()
            if '1c' in name or '1с' in name or '1-c' in name or '1-с' in name:
                row[1] = row[1].replace('\n', '|')
                writer.writerow(row)

with open("1C-vacancies.csv", 'r', encoding='utf-8') as file:
    print(sum(1 for line in file))
