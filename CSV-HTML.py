import pandas as pd

file_path = "assets/cities.csv"
csv_reader = pd.read_csv(file_path)

html = csv_reader.to_html()

cities_html = open("source_data.html", "w")
cities_html.write(html)
cities_html.close()