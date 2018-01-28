my_file = open("output.txt", "r+")

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for value in my_list:
  my_file.write(str(value) + "\n")
  
my_file.close()
