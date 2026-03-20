# ============================================================================
# List – akses & manipulasi
# ============================================================================

data_list = ["Hello", 24, 24.5, True, "AI", 99]

# Elemen pertama & terakhir
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])

# Slicing
print("Slicing [1:5:2]:", data_list[1:5:2])

# Sebelum manipulasi
print("\nSebelum manipulasi:", data_list)

# append()
data_list.append("Baru")
print("Setelah append:", data_list)

# insert()
data_list.insert(1, "Insert")
print("Setelah insert:", data_list)

# extend()
data_list.extend([100, 200])
print("Setelah extend:", data_list)

# pop()
data_list.pop()
print("Setelah pop:", data_list)

# remove()
data_list.remove("Hello")
print("Setelah remove:", data_list)


# ============================================================================
# Tuple – immutability & unpacking
# ============================================================================

data_tuple = ("Adit", "Asma", "Pekanbaru", 24, "April", 2005)

print("\nPanjang tuple:", len(data_tuple))
print("Akses index ke-2:", data_tuple[1])

# Unpacking
nama, crush, *lainnya = data_tuple
print("Nama:", nama)
print("Crush:", crush)
print("Lainnya:", lainnya)


# ============================================================================
# Set – keunikan & operasi himpunan
# ============================================================================

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Duplikat hilang
duplikat = {1, 2, 2, 3, 3, 4}
print("Set tanpa duplikat:", duplikat)


# ============================================================================
# Dictionary – key/value dasar
# ============================================================================

mahasiswa = {
    "nama": "Adit",
    "nim": 2307110467,
    "angkatan": 2023,
    "kota": "Pekanbaru"
}

# Tambah key
mahasiswa["semester"] = 6

# Ubah nilai
mahasiswa["kota"] = "Jakarta"

# Hapus key
mahasiswa.pop("nama")

print("\nDictionary:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

# Iterasi
for k, v in mahasiswa.items():
    print(f"{k} : {v}")


# ============================================================================
# Nested structures
# ============================================================================

buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun": 1980},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
    {"judul": "Perahu Kertas", "penulis": "Dee Lestari", "tahun": 2009}
]

# Cetak semua judul
print("\nDaftar Judul Buku:")
for b in buku:
    print(b["judul"])

# Filter buku ≥ tahun tertentu
buku_baru = [b for b in buku if b["tahun"] >= 2000]

print("\nBuku terbit >= 2000:")
for b in buku_baru:
    print(b["judul"])


# ============================================================================
# Comprehension & utilitas
# ============================================================================

# List comprehension
genap = [x for x in range(1, 21) if x % 2 == 0]
kuadrat = [x**2 for x in range(1, 21)]

print("\nList genap:", genap)
print("List kuadrat:", kuadrat)

# Dict comprehension
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Mapping genap/ganjil:", mapping)

# Set comprehension
kalimat = "Adit Nugraha"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# ============================================================================
# Keanggotaan & pencarian sederhana
# ============================================================================

buah = ["apel", "jeruk", "mangga"]

# Cek keanggotaan
print("\nCek 'apel' di list:", "apel" in buah)
print("Cek 'pisang' di list:", "pisang" in buah)

# Cari posisi dengan aman
item = "jeruk"
print(f"{item} ada di index {buah.index(item)}" if item in buah else "tidak ditemukan")