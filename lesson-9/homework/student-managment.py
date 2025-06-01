import csv

READ = "/media/asadbek/D/maab/new/python-homeworks/lesson-9/homework/grades.csv"
WRITE = "/media/asadbek/D/maab/new/python-homeworks/lesson-9/homework/average_grades.csv"
def main():
    with open(READ) as f:
        data = csv.DictReader(f, delimiter=',')

        scores = dict()
        for row in data:
            if not row['Subject'] in scores:
                scores[row['Subject']] = [int(row['Grade'])]
            else:
                scores[row['Subject']].append(int(row['Grade']))
        averages = dict()
        for sbj, gr in scores.items():
            averages[sbj] = sum(gr) / len(gr)
    headers = ['Subject', "Average Grade"]
    with open(WRITE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for sbj, gr in averages.items():
            writer.writerow({"Subject" : sbj, "Average Grade" : str(gr)})


main()