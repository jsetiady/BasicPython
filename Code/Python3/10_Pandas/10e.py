# Import pandas and cars.csv
import pandas as pd
nilai = pd.read_csv('nilai.csv', index_col = 0)


print (nilai.describe())

