from pokemon.models import Trainers
import csv 

# Cite: https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
def run(): 
	with open("trainers.csv") as trainer_csv: 
		reader = csv.reader(trainer_csv) 
		next(reader) 
		
		Trainers().objects.all().delete()
		
		for row in reader: 
			print(row) 

			trainer = Trainer(trainer_class=row[0],
							pokemon1 = row[1],
							pokemon2 = row[2],
							pokemon3 = row[3],
							pokemon4 = row[4],
							pokemon5 = row[5],
							pokemon6 = row[6]
			)
			trainer.save()