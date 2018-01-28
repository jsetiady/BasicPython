# Program Tip Calculator
# Copy-Paste dan Edit Program Ini

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

# Tulis kodemu disini
# Hitung harga bruto meal (harga netto meal + harga netto * tax)
meal = meal + meal * tax

# Hitung total transaksi (harga bruto meal + harga bruto meal * tip)
total = meal + meal * tip


print ("%.2f" % total)
