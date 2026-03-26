import numpy as np
import pandas as pd

# Set seed agar hasil random konsisten
np.random.seed(42)
print(np.random.rand())


# =========================
# NUMPY – DATA & STATISTIK
# =========================

print("\n=== NUMPY (RAW) ===")

nilai_ujian = [78, 85, 90, 66, 74, 88, 92, 70, 81, 76]
print("Tipe list:", type(nilai_ujian))

# Konversi list ke array NumPy
nilai_ujian_arr = np.array(nilai_ujian)
print("Tipe array:", type(nilai_ujian_arr))

print("\nStatistik NumPy:")

# Statistik dasar
rata_rata_nilai_ujian = np.mean(nilai_ujian_arr)
print("Rata-rata nilai ujian:", rata_rata_nilai_ujian)

standar_deviasi_nilai_ujian = np.std(nilai_ujian_arr)
print("Standar deviasi:", standar_deviasi_nilai_ujian)

median_nilai_ujian = np.median(nilai_ujian_arr)
print("Median:", median_nilai_ujian)

max_nilai_ujian = np.max(nilai_ujian_arr)
print("Nilai ujian tertinggi:", max_nilai_ujian)

min_nilai_ujian = np.min(nilai_ujian_arr)
print("Nilai ujian terendah:", min_nilai_ujian)


# =========================
# PANDAS – DATAFRAME
# =========================

print("\n=== PANDAS (DATAFRAME) ===")

# Data mahasiswa
data_mahasiswa = {
    "nama": ["Adit", "Budi", "Citra", "Dina", "Eko"],
    "nim": ["2307110467", "2307110468", "2307110469", "2307110470", "2307110471"],
    "nilai": [78, 85, 90, 66, 74]
}

# Membuat DataFrame
df = pd.DataFrame(data_mahasiswa)

# Statistik dari DataFrame
rata_rata_data_mahasiswa = np.mean(df['nilai'])
median_data_mahasiswa = np.median(df['nilai'])
standar_deviasi_data_mahasiswa = np.std(df['nilai'])
min_data_mahasiswa = np.min(df['nilai'])
max_data_mahasiswa = np.max(df['nilai'])

# Menentukan status lulus/tidak
status = []
for i in df['nilai']:
    if i >= 70:
        status.append('LULUS')
    else:
        status.append('TIDAK LULUS')

# Menambahkan kolom status ke DataFrame
df['status'] = status

print("\nData mahasiswa (head):")
print(df.head())


# =========================
# FILE I/O – SIMPAN KE TXT
# =========================

with open('ringkasan_tugas6.txt', 'w') as file:
    file.write(f"===== LUAR CLASS =====\n")
    file.write(f"Rata-rata nilai ujian: {rata_rata_nilai_ujian}\n")
    file.write(f"Standar deviasi nilai ujian: {standar_deviasi_nilai_ujian}\n")
    file.write(f"Nilai ujian tertinggi: {max_nilai_ujian}\n")
    file.write(f"Nilai ujian terendah: {min_nilai_ujian}\n")
    file.write(f"Data mahasiswa:\n{df}\n")

    # Informasi tambahan DataFrame
    file.write(f"Jumlah kolom: {len(df.columns)}\n")
    file.write(f"Jumlah baris: {len(df.index)}\n")
    file.write(f"Jumlah LULUS: {(df['status'] == 'LULUS').sum()}\n")
    file.write(f"Jumlah TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}\n")


# =========================
# OOP – CLASS GRADEBOOK
# =========================

class GradeBook:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return np.mean(self.df['nilai'])

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = self.df['nilai'] >= threshold
        return np.mean(lulus) * 100

    def save_summary(self, path):
        with open(path, 'a') as file:
            file.write("\n")
            file.write(f"===== DALAM CLASS =====\n")
            file.write(f"Rata-rata nilai ujian: {self.average()}\n")
            file.write(f"Pass rate: {self.pass_rate()}\n")
            file.write(f"Data mahasiswa:\n{self.df}\n")

    def __str__(self):
        return (
            f"GradeBook(jumlah_data={len(self.df)}, "
            f"average={self.average():.2f}, "
            f"pass_rate={self.pass_rate():.2f})"
        )


# =========================
# MAIN PROGRAM (DEMO)
# =========================

if __name__ == '__main__':
    grd = GradeBook(df)

    print("\n=== OOP OBJECT ===")
    print(grd)

    print("\n=== NUMPY ===")
    print("Rata-rata nilai:", rata_rata_data_mahasiswa)
    print("Median nilai:", median_data_mahasiswa)
    print("Standar deviasi:", standar_deviasi_data_mahasiswa)
    print("Nilai minimum:", min_data_mahasiswa)
    print("Nilai maksimum:", max_data_mahasiswa)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    print("Average:", grd.average())
    print("Pass rate:", grd.pass_rate())

    # Menyimpan hasil dari class
    grd.save_summary('ringkasan_tugas6.txt')