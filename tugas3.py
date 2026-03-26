# 1. Deklarasi Variabel dan Tipe Data
print("\n" + "="*50)
print("1. Deklarasi Variabel dan Tipe Data")
print("="*50)

var_string = 'Hello world!'
var_integer = 24
var_float = 24.5
var_boolean = True
var_list = [var_string,var_integer,var_float,var_boolean]

for var in var_list:
	print(type(var))
print(type(var_list))


# 2. Manipulasi String
print("\n" + "="*50)
print("2. Manipulasi String")
print("="*50)

# ================================
# BASIC STRING
# ================================

print("\n--- BASIC STRING ---")

string_1 = 'Adit'
string_2 = 'Ganteng'

print(f"string_1: {string_1}")
print(f"string_2: {string_2}")

print(f"Gabung: {string_1 + ' ' + string_2}")
print(f"Panjang string_1: {len(string_1)}")
print(f"Panjang string_2: {len(string_2)}")

print(f"Lower string_1: {string_1.lower()}")
print(f"Upper string_1: {string_1.upper()}")


# ================================
# SLICING
# ================================

print("\n--- SLICING ---")

print(f"string_1[0:2]: {string_1[0:2]}")
print(f"string_2[:2]: {string_2[:2]}")

print(f"string_1[2:]: {string_1[2:]}")
print(f"string_2[2:]: {string_2[2:]}")

print(f"string_1[-2:]: {string_1[-2:]}")
print(f"string_2[-2:]: {string_2[-2:]}")

print(f"string_1[-4:-2]: {string_1[-4:-2]}")
print(f"string_2[-4:-2]: {string_2[-4:-2]}")


# ================================
# STRING CLEANING
# ================================

print("\n--- STRING CLEANING ---")

string_3 = 'Adit Ganteng '

print(f"Strip: {string_3.strip()}")

text = string_3
text = text.replace('Adit', 'Aditya')
text = text.replace('Ganteng', 'Ganteng Banget')

print(f"Replace: {text}")


# ================================
# SPLIT & JOIN
# ================================

print("\n--- SPLIT & JOIN ---")

text = "Adit Ganteng"

words = text.split()
print(f"Split: {words}")

print(f"Join: {' '.join(words)}")


# ================================
# FIND
# ================================

print("\n--- FIND ---")

text = "Adit Ganteng"

print(f"Find 'Ganteng': {text.find('Ganteng')}")


# ================================
# CEK STRING
# ================================

print("\n--- CEK STRING ---")

text = "Adit123"

print(f"isalpha: {text.isalpha()}")
print(f"isdigit: {text.isdigit()}")
print(f"isalnum: {text.isalnum()}")


# ================================
# STARTSWITH & ENDSWITH
# ================================

print("\n--- STARTSWITH & ENDSWITH ---")

text = "Adit Ganteng"

print(f"startswith 'Adit': {text.startswith('Adit')}")
print(f"endswith 'Ganteng': {text.endswith('Ganteng')}")


# ================================
# FORMAT STRING
# ================================

print("\n--- FORMAT STRING ---")

nama = "Adit"
umur = 20

print(f"Format: Nama aku {nama}, umur {umur}")


# ================================
# REPLACE LIMIT
# ================================

print("\n--- REPLACE LIMIT ---")

text = "Adit Adit Adit"

print(f"Replace 1x: {text.replace('Adit', 'Aditya', 1)}")


# ================================
# CASE CONVERSION
# ================================

print("\n--- CASE CONVERSION ---")

text = "adit ganteng banget"

print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")


# ================================
# REMOVE SPACE
# ================================

print("\n--- REMOVE SPACE ---")

text = "Adit Ganteng Banget"

print(f"No space: {text.replace(' ', '')}")


# 3. Operasi Matematika Sederhana
print("\n" + "="*50)
print("3. Operasi Matematika Sederhana")
print("="*50)

a = 10
b = 3

print(f"Penjumlahan (a + b): {a + b}")
print(f"Pengurangan (a - b): {a - b}")
print(f"Perkalian (a * b): {a * b}")
print(f"Pembagian (a / b): {a / b}")
print(f"Pembagian bulat (a // b): {a // b}")
print(f"Sisa bagi (a % b): {a % b}")

# 4. List dan Akses Elemen
print("\n" + "="*50)
print("4. List dan Akses Elemen")
print("="*50)

# List sekarang sudah 5 item
list_1 = ['apel', 'pisang', 'mangga', 'nanas', 'melon']
list_2 = ['jeruk', 'kelengkeng', 'semangka', 'anggur', 'pepaya']

list_1.extend(list_2)
print(f"Extend (gabung list): {list_1}")

list_1.remove('apel')
print(f"Remove 'apel': {list_1}")

list_1.pop()
print(f"Pop terakhir: {list_1}")


print("\n--- TAMBAHAN LIST ---")

# List minimal 5 item
list_1 = ['apel', 'pisang', 'mangga', 'nanas', 'melon']

list_1.append('jeruk')
print(f"Append 1 item: {list_1}")

list_1.extend(['anggur', 'pepaya'])
print(f"Extend: {list_1}")

list_1.insert(1, 'semangka')
print(f"Insert index 1: {list_1}")

print(f"Index 0: {list_1[0]}")
print(f"Index -1: {list_1[-1]}")


print("\n--- SLICING LIST ---")

print(f"Slice [1:3]: {list_1[1:3]}")
print(f"Slice [:2]: {list_1[:2]}")
print(f"Slice [2:]: {list_1[2:]}")


print("\n--- INFO LIST ---")

print(f"Panjang list: {len(list_1)}")
print(f"Ada 'apel'?: {'apel' in list_1}")
print(f"Index 'pisang': {list_1.index('pisang')}")


print("\n--- SORT & REVERSE ---")

# List angka minimal 5 item
list_angka = [5, 2, 9, 1, 7]

list_angka.sort()
print(f"Sort ascending: {list_angka}")

list_angka.reverse()
print(f"Reverse: {list_angka}")


print("\n--- COPY & CLEAR ---")

copy_list = list_1.copy()
print(f"Copy list: {copy_list}")

list_1.clear()
print(f"Clear list: {list_1}")

# 5. Penggunaan Input dari User
print("\n" + "="*50)
print("5. Penggunaan Input dari User")
print("="*50)

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

print(f"Halo, nama saya {nama} dan umur saya {umur} tahun.")