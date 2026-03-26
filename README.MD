# 📘 Kesimpulan Tugas 4, 5, dan 6

> **Nama:** Adit Nugraha  
> **Asal:** AI - Universitas Riau

---

## Tugas 4 — Struktur Data Python

**File:** `tugas4.py`

Tugas ini mempelajari empat struktur data utama di Python beserta operasinya:

| Struktur Data  | Konsep yang Dipelajari                                                                      |
| -------------- | ------------------------------------------------------------------------------------------- |
| **List**       | Akses elemen, slicing, dan manipulasi (`append`, `insert`, `extend`, `pop`, `remove`)       |
| **Tuple**      | Sifat immutable dan teknik unpacking                                                        |
| **Set**        | Keunikan elemen & operasi himpunan (union, intersection, difference, symmetric difference)  |
| **Dictionary** | Pasangan key-value, CRUD data, serta iterasi menggunakan `.keys()`, `.values()`, `.items()` |

Selain itu, tugas ini juga mencakup:

- **Nested structures** — List berisi dictionary untuk merepresentasikan data buku.
- **Comprehension** — List, dict, dan set comprehension untuk pemrosesan data yang ringkas.
- **Pengecekan keanggotaan** — Operator `in` untuk pencarian elemen di dalam list.

### 🔑 Kesimpulan

Pemahaman struktur data sangat krusial karena menjadi fondasi dalam menyimpan, mengorganisasi, dan memanipulasi data. Setiap struktur data memiliki kelebihan masing-masing: **List** fleksibel dan terurut, **Tuple** aman dari perubahan, **Set** menjamin keunikan, dan **Dictionary** optimal untuk pencarian berbasis key.

---

## Tugas 5 — Function dan Object-Oriented Programming (OOP)

**File:** `tugas5.py`

Tugas ini berfokus pada dua pilar penting pemrograman Python:

### Functions

- **`greet(nama)`** — Mengembalikan string sapaan (konsep return value & type hint).
- **`tambah(a, b)`** — Penjumlahan dengan parameter default (`b=0.0`).
- **`rata_rata(angka)`** — Menghitung rata-rata list dengan penanganan list kosong (defensive programming).

### Class `Student`

- **Constructor (`__init__`)** — Inisialisasi atribut `nama`, `nim`, `nilai` dengan validasi `None`.
- **Method `tambah_nilai()`** — Menambah skor ke list nilai (mutability).
- **Method `rata_nilai()`** — Memanggil ulang fungsi `rata_rata()` (code reuse).
- **Method `status()`** — Menentukan kelulusan berdasarkan threshold.
- **`__str__()`** — Representasi objek yang informatif saat di-print.

### 🔑 Kesimpulan

Function memungkinkan kode yang modular dan reusable, sedangkan OOP memungkinkan pengelompokan data dan perilaku ke dalam satu entitas (class). Kombinasi keduanya menghasilkan kode yang lebih terstruktur, mudah dibaca, dan mudah di-maintain. Konsep **encapsulation** terlihat jelas pada class `Student` yang membungkus data mahasiswa beserta operasinya.

---

## Tugas 6 — NumPy, Pandas, File I/O, dan OOP Lanjutan

**File:** `tugas6.py`

Tugas ini mengintegrasikan beberapa library dan konsep sekaligus:

### NumPy

- Konversi list ke array NumPy untuk komputasi numerik yang efisien.
- Fungsi statistik: `np.mean()`, `np.std()`, `np.median()`, `np.max()`, `np.min()`.
- Penggunaan `np.random.seed(42)` untuk reproducibility.

### Pandas DataFrame

- Pembuatan DataFrame dari dictionary.
- Perhitungan statistik pada kolom DataFrame.
- Penambahan kolom baru (`status`) berdasarkan logika kondisional (LULUS / TIDAK LULUS).

### File I/O

- Menulis hasil analisis ke file teks (`ringkasan_tugas6.txt`) menggunakan context manager (`with open`).
- Mode `'w'` untuk penulisan awal dan `'a'` untuk append dari class.

### OOP — Class `GradeBook`

- Menerima DataFrame sebagai parameter (integrasi Pandas + OOP).
- Method `average()` dan `pass_rate()` untuk analisis nilai.
- Method `save_summary()` untuk menyimpan ringkasan ke file.
- `__str__()` menampilkan ringkasan objek secara ringkas.

### 📊 Hasil Output (`ringkasan_tugas6.txt`)

| Metrik                | Nilai |
| --------------------- | ----- |
| Rata-rata nilai ujian | 80.0  |
| Standar deviasi       | 8.28  |
| Nilai tertinggi       | 92    |
| Nilai terendah        | 66    |
| Jumlah LULUS          | 4     |
| Jumlah TIDAK LULUS    | 1     |
| Pass Rate             | 80%   |

### 🔑 Kesimpulan

Tugas ini menunjukkan bagaimana berbagai komponen Python — library numerik (NumPy), analisis data (Pandas), file handling, dan OOP — dapat diintegrasikan untuk membangun pipeline analisis data sederhana. Ini merupakan fondasi penting sebelum melangkah ke machine learning dan data science.

---

## 🎯 Kesimpulan Keseluruhan

Ketiga tugas ini membentuk **learning path** yang progresif:

```
Tugas 4 (Struktur Data) → Tugas 5 (Function & OOP) → Tugas 6 (Library & Integrasi)
```

1. **Tugas 4** membangun pondasi penyimpanan dan manipulasi data.
2. **Tugas 5** mengajarkan modularitas kode melalui function dan OOP.
3. **Tugas 6** mengaplikasikan semua konsep sebelumnya dengan library NumPy & Pandas untuk analisis data nyata.

Secara keseluruhan, ketiga tugas ini membekali pemahaman fundamental Python yang solid — mulai dari **struktur data**, **pemrograman berorientasi objek**, hingga **analisis data** — yang semuanya merupakan skill esensial dalam bidang **Artificial Intelligence** dan **Machine Learning**.
