# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print (cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print (cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print (cars[['cars_per_cap', 'country']])