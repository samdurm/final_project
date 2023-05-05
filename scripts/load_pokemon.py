from pokemon.models import Pokemon
import csv 

# Cite: https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
def run(): 
	with open("pokemon.csv") as pokemon_csv: 
		reader = csv.reader(pokemon_csv) 
		next(reader) 
		
		Pokemon.objects.all().delete()
		
		for row in reader: 
			print(row) 

			pokemon = Pokemon(against_bug=row[0],
							against_dark=row[1],
							against_dragon=row[2],
							against_electric=row[3],
							against_fairy=row[4],
							against_fight=row[5],
							against_fire=row[6],
							against_flying=row[7],
							against_ghost=row[8],
							against_grass=row[9],
							against_ground=row[10],
							against_ice=row[11],
							against_normal=row[12],
							against_poison=row[13],
							against_psychic=row[14],
							against_rock=row[15],
							against_steel=row[16],
							against_water=row[17],
							attack=row[18],
							base_total=row[19],
							capture_rate=row[20],
							defense=row[21],
							height_m=row[22],
							hp=row[23],
							name=row[24],
							pokedex_number=row[25],
							sp_attack=row[26],
							sp_defense=row[27],
							speed=row[28],
							type1=row[29],
							type2=row[30],
							weight_kg=row[31],
							is_legendary=row[32]
			)
			pokemon.save()