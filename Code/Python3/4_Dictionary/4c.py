prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}

stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}

for x in prices:
  print (x)
  print ("price:%s" % prices[x])
  print ("stock:%s" % stock[x])

print "======="
print "Latihan"

# Latihan
# Tambahkan key "watermelon" pada prices dan stock. Isi value bebas
prices["watermelon"] = 3
stock["watermelon"] = 3

# Ubah value stock apple dengan 5
stock["apple"] = 5

# Print hasilnya (copy line 11)
for x in prices:
  print (x)
  print ("price:%s" % prices[x])
  print ("stock:%s" % stock[x])
