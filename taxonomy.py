import csv
f = open('Taxonomy.csv')
csv_f = csv.DictReader(f)

for row in csv_f:
	print row
