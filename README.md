# Basic Python dan Implementasinya untuk Analisis Data

Materi workshop **Basic Python dan Implementasinya untuk Analisis Data** untuk acara **LPDP ITB SmartWeekend** 27-28 Januari 2018. 

*Workshop material of **Basic Python dan Implementasinya untuk Analisis Data** for event **LPDP ITB SmartWeekend** January 27-28th 2018.* 

## Apa saja yang dibutuhkan?

 - Python versi 3, atau (*alternatif jika tidak sempat install Python 3*) akun di Kaggle.com)
 - (optional) Pycharm versi terbaru dan stable, atau IDE lain sesuai preferensi

# Intro
 
 Python, dan Javascript adalah bahasa pemrograman yang *trending** di akhir 2017 / awal 2018
\* *banyak dicari di stackoverflow*

![Growth of Major Programming Language (2012-2018)](http://news.codecademy.com/content/images/2018/01/growth_major_languages-1-1400x1200.png)
*source: Stack Overflow*

Peningkatan jumlah orang yang mempelajari Python di tahun 2017 (codeacademy).
![enter image description here](http://news.codecademy.com/content/images/2018/01/02-last-year-v02a-FULL.jpg)


**Motivasi untuk Mempelajari Python**
Berdasarkan artikel [1] : Meningkatnya minat pada bahasa pemrograman Python terasosiasi dengan peningkatan minat terhadap *data science*. Popularitas Python pada *data science* dan *machine learning* ikut mendukung peningkatan minat untuk mempelajari Python.

Mengapa banyak orang memilih Python? Padahal masih ada SQL dan R yang juga menunjang *data science*.

Salah satu faktornya adalah *versatility** dari Python. Ada lebih dari 125.000 Python *Libraries* [3], yang menyebabkan bahasa pemorgraman Python dapat bermanfaat untuk tujuan spesifik, seperti *web development*, *text processing*, hingga *machine learning*. 
*versatility* = kemampuan / kepandaian yang beraneka ragam

**Python untuk Analisis Data?**
Python telah menjadi bahasa pemrograman populer untuk analisis data. Dengan dukungan *libraries* seperti panda, NumPy, dan matplotlib, siapa pun yang mengenal sintaks dan aturan Python dapat menerapkannya untuk memproses, memanipulasi, dan memvisualisasikan data.

**Read more:**
 1. Robinson, David. 2017. The Incredible Growth of Python. https://stackoverflow.blog/2017/09/06/incredible-growth-python/
 2. Robinson, David. 2017. Why is Python Growing . https://stackoverflow.blog/2017/09/06/incredible-growth-python/
 3. Strong, Alexus. 2018. Why I’m Learning Python in 2018. http://news.codecademy.com/why-learn-python/?utm_source=customer.io&utm_medium=email&utm_campaign=fortnightly_1-12-18&utm_content=why-learn-python
 4. Johnson, Phil. 2014. Python squeezes out JavaScript, C as best starter programming language. https://www.itworld.com/article/2693392/python-squeezes-out-javascript-c-as-best-starter-programming-language.html


## Python Essential Libraries untuk Analisis Data

### NumPy
`NumPy`, singkatan dari Numerical Python, adalah package dasar untuk scientific computing dengan Python. `NumPy` menyediakan:
 - Multidimensional array object (*ndarray*)
 - Fungsi-fungsi untuk melakukan komputasi berbasis elemen dengan array atau operasi matematis antar array
 - Tools untuk membaca dan menulis datasets berbasis array
 - Operasi aljabar linear, transformasi Foirier, dan random number generation
 - Tools untuk mengintegrasikan kode C, C++, dan kode Fortean ke Python

Selain kemampuan pemrosesan array-nya, kegunaan utama `NumPy` terkait analisis data adalah sebagai container untuk data agar bisa dilewatkan ke berbagai algoritma. Untuk data numerik, array `NumPy` lebih efisien dibandingkan dengan array yang built-in pada struktur data Python.


### pandas
Nama `pandas`  diturunkan dari panel data, yaitu economic term untuk multidimensional structured data sets. Nama `pandas` juga mengandung makna *Python data analysis*.
`pandas` menyediakan struktur data dan fungsi yang dirancang agar menganalisis data yang terstruktur menjadi lebih cepat dan mudah. pandas adalah salah satu komposisi utama yang membuat Python menjadi bahasa pemrograman yang powerful untuk analisis data.
Objek utama `pandas` yang digunakan pada workshop ini adalah DataFrame, yaitu sebuah struktur data dua dimensi, tabular, dan column-oriented, dengan label pada baris dan kolomnya. Contoh DataFrame adalah sebagai berikut:

     >>> frame
	    total_bill	tip		sex		smoker	day	time	size
    1	16.99		1.01	Female	No		Sun	Dinner	2
    2	10.34		1.66	Male	No		Sun	Dinner	3
    3	21.01		3.5		Male	No		Sun	Dinner	3
    4	23.68		3.31	Male	No		Sun Dinner	2
    5	24.59		3.61	Female	No		Sun Dinner	4
    6	25.29		4.71	Male	No		Sun Dinner	4
    7	8.77		2		Male	No		Sun Dinner	2
    8	26.88		3.12	Male	No		Sun Dinner	4
    9	15.04		1.96	Male	No		Sun Dinner	2
    10	14.78		3.23	Male	No		Sun Dinner	2

`pandas` juga punya kemampuan manipulasi data dari spreadsheets dan basis data relasional (seperti SQL). 

### matplotlib
`matplotlib` adalah librari Python yang populer untuk menghasilkan plots dan visualisasi data 2D. `matplotlib` menyediakan fitur untuk dapat secara interaktif (plot) menggambar data, dan melakukan eksplorasi.

### SciPy
`SciPy` adalah koleksi dari package-package untuk permasalahan standar di scientific computing. Beberapa package pada SciPy termasuk:
- `scipy.integrate`: integrasi numerik dan solvers untuk numerical integration routines and solvers untuk masalah persamaan differensial
- `scipy.linalg`: aljabar linear dan dekomposisi matriks
- `scipy.optimize`: fungsi optimisasi dan algoritma pencarian akar  
- `scipy.signal`: tools untuk pemrosesan signal
- `scipy.sparse`: sparse matrices and sparse linear system solvers
- `scipy.stats`: distribusi kontinyu dan diskrit standar (density functions, samplers, continuous distribution functions), dan bermacam-macam pengujian statistik
- `scipy.weave`: tool untuk menggunakan fitur inline kode C++ untuk mengakselerasi komputasi array

# Basic Python
## Instalasi
 1. Kunjungi https://www.python.org/downloads/
 2. Pilih latest version sesuai dengan OS Anda
 Versi Python yang digunakan pada workshop ini adalah Python 3.X.X
3. Install IDE PyCharm Community Edition. Unduh lewat https://www.jetbrains.com/pycharm/download/#section=mac

## Python Syntax
 - Variable dan tipe data
```
nama = "Joko Widodo"
umur = 23
umur_dalam_hexadesimal = 0x17
diskon = 0.15
is_mahasiswa = True
```
 - Whitespace: pemisah antar statement
 - Comments
```
# Komentar dalam satu baris

'''
komentar dalam beberapa baris
'''
```
 - Operasi aritmatika, termasuk +, -, *, /, **, dan %
 ```
total_bayar = harga_total - (harga_total * diskon)
```

### (Sebagian) Coding Best Practices and Conventions

 - Indentasi
 Gunakan 4 spasi untuk setiap level indentasi
 ```
 def long_function_name(
        var_one, var_two, var_three,
        var_four):
     print(var_one)
 ```

Quoted from Pep 0008:
> Tabs or Spaces? Spaces are the preferred indentation method.
> 
> Tabs should be used solely to remain consistent with code that is
> already indented with tabs.
> 
> Python 3 disallows mixing the use of tabs and spaces for indentation.
> 
> Python 2 code indented with a mixture of tabs and spaces should be
> converted to using spaces exclusively.

- Blank lines
Two blank lines between top-level definitions, one blank line between method definitions.

 - Imports
 Imports should usually be on separate lines, e.g.:
```
Yes: import os
     import sys
```
```
No:  import sys, os
```
 - Naming
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.


Read more:
https://www.python.org/dev/peps/pep-0008/
https://google.github.io/styleguide/pyguide.html

## String and Console Input

 - 3 cara untuk membuat string
```
'Alpha'
"Bravo"
str(3)
```
 - String method:
```
len("Charlie")
"Delta".upper()
"Echo".lower()
```
 - Print a string
```
print "Hello World"
```

 - Advance printing technique
```
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)
```

Contoh program: Tip Calculator
```
meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
```

- Date and Time
```
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
```

## Conditional and Control Flow
- Comparators
```
3 < 4
5 >= 5
10 == 10
12 != 13
```
- Boolean operators
```
True or False 
(3 < 4) and (5 >= 5)
this() and not that()
```
- Conditional statements
```
if this_might_be_true():
  print "This really is true."
elif that_might_be_true():
  print "That is true."
else:
  print "None of the above."
```

## Functions
```
def is_numeric(num):
    return type(num) == int or type(num) == float:

is_numeric(7) # int
is_numeric(7.5) # float
is_numeric("word") # False

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2

```

## Lists and Dictionary
### Lists
`Lists` adalah sebuah tipe data. Kamu bisa menyimpan koleksi dari beberapa bagian informasi sebagai sequence dalam satu variable. (Contoh tipe data lain yang sudah kamu pelajari: string, numbers, boolean)

Kamu bisa meng-*assign* items ke sebuah list dengan ekspresi berikut: 

    list_name = [item_1, item_2]

item-item diletakan didalam tanda kurung [] 
List juga bisa kosong:

    empty_list = []


#### Mengakses List berdasarkan index
Kamu bisa mengakses item pada list lewat index-nya. Index adalah alamat yang mengidentifikasi item yang terletak pada list.
List index dimulai dari 0. Jadi, kamu bisa mengakses item pertama dari list dengan cara berikut:

    list_name[0]

    zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

    zoo_animals[0]

    zoo_animals[2] = "hyena"

#### List Length
Sebuah list tidak harus punya panjang yang tetap. Kamu bisa menambahkan item ke list kapan saja.
```
letters = [‘a’, ‘b’, ‘c’]
letters.append(‘d’)
print len(letters)	# 4
print letters		# ['a', 'b', 'c', 'd']
```

#### List Slicing
Kadang-kadang kita hanya ingin mengakses sebagian dari list
```
letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice		# ['b', 'c']
print letters	# ['a', 'b', 'c', 'd', 'e']
```
Pada contoh diatas, mula-mula kita membuat list dengan nama letters. Kemudian, kita mengambil sebagian dari list tersebut, dan disimpan dalam variable list `slice`.  Kita mulai dari index 1, dan berlanjut hingga sebelum index ke 3.

#### Slicing Lists and Strings
Kamu dapat men-`slice` sebuah string sama seperti sebuah list. String dapat diumpamakan sebagai list of characters: setiap karakter pada string adalah sebuah item pada list, mulai dari index 0.
```
my_list = "Hello"
print my_list[:2] # Mengambil 2 item pertama --> He
print my_list[3:] # Mengambil item ke-empat hingga ke item terakhir --> lo
```
Jadi, jika list slice yang ingin kamu ambil termasuk item pertama atau terakhir, index nya tidak perlu disebutkan (cukup ":" saja)

#### Maintaining Order
Kadang-kadang kamu harus mencari item dalam sebuah list. Method `index` mengembalikan posisi index suatu item pada list
```
animals = ["ant", "bat", "cat"]
print animals.index("bat")
```

Kita juga dapat menyisipkan item dalam sebuah list
```
animals.insert(1, "dog")
print animals		# ["ant", "dog", "bat", "cat"]
```

#### For One and All
Jika kamu ingin melakukan sesuatu yang berlaku untuk semua item pada list, kamu bisa menggunakan `loop`.

```
for variable in list_name:
    # Do stuff!
```
Variable akan mengikuti *for* (semoga ngga bingung). Jadi si variable akan diassign dengan value setiap item pada list.

perintah `for` diakhiri dengan sebuah titik dua (:), dan kode berikutnya yang diberikan indentasi adalah kode yang dieksekusi satu kali per item dalam list

Method sort() digunakan untuk mengurutkan isi list
```
animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal
```
#### Menghapus item dalam List
```
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
```


### Dictionary
Sebuah dictionary mirip dengan list, namun kamu dapat mengakses value dalam list bukan dengan `index`, namun menggunakan `key`
Sebuah `key` dapat berupa `string` atau `number`
Sebuah dictionary dibuat dalam tanda kurung berikut `{` `}`

    d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

```
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # 104

print residents['Sloth']  # 105
print residents['Burmese Python']  # 106
```

#### Menambah, Mengubah, atau Menghapus Item pada Dictionary
Kita bisa menambahkan pasangan key/value baru pada dictionary setelah dictionary diciptakan:

    dict_name[new_key] = new_value

empty dictionary

    dict_name = {}

len() dari dictionary adalah jumlah pasangan key-value pada dictionary tersebut. Setiap pasang hanya dihitung satu, meskipun valuenya adalah list.

Item dapat dihapus dari dictionary dengan menggunakan perintah `del`

    del dict_name[key_name]
perintah tersebut akan menghapus key dengan nama key_name dan menghapus nilai yang berasosiasi dengannya.

Value yang baru dapat diasosiasikan dengan key dengan meng-assign value ke key, seperti:

    dict_name[key] = new_value

#### Dictionary dengan banyak value list
```
my_dictionary = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}

print my_dictionary["fish"][0] # c
```
Pada contoh diatas, kita membuat dictionary yang berisi beragam tipe
key "fish" isinya list
key "cash" isinya int
key "luck" isinya string

Pada baris akhir, dicetak ke layar karakter "c". Kita mengakses dictionary pada key "fish" yang berisi list, kemudian kita dapat akses ke value pada index 0 pada list yang disimpan dalam key "fish"

## Loops


## Class
## File input/output


# Analisis Data dengan Python

## Visualisasi Data dengan Matplotlib
Membuat grafik dengan Matplotlib untuk menyajikan data atau temuan hasil analisis data

## Data Analysis with Pandas
Melakukan load data, menginspeksi, dan memodifikasi data dengan Pandas. Melakukan data analisis.


## Basic Statistics with Numpy
Melakukan eksplorasi statistik dasar

## Comparative Statistics with Scipy
Merancang A/B testing, dan menunjukkan perbandingan data (dasar untuk data driven decisions)




