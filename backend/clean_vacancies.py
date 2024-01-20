# rewriting vacancies to new file without broken lines
import csv

with open(r"C:\Users\Minty\Downloads\vacancies.csv", 'r', encoding='utf-8-sig') as file:
    with open("cleaned_vacancies.csv", 'w', encoding='utf-8', newline='') as output:
        reader = csv.reader(file)
        writer = csv.writer(output)
        for line in reader:
            if len(line) == 7:
                writer.writerow(line)
            else:
                print(line)
