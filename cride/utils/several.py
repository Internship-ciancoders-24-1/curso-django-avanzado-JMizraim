import csv
from cride.circles.models import Circle

file_path = "circles.csv"

def load_data():
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                Circle.objects.create(**row)
        print("Datos cargados correctamente")
    except Exception as e:
        print("Algo salió mal :(", e)