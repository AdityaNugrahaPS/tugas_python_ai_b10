# =========================
# FUNCTIONS
# =========================

def greet(nama: str) -> str:
    """Mengembalikan sapaan ke user"""
    return f'Halo, {nama}'


def tambah(a: float, b: float = 0.0) -> float:
    """Menjumlahkan dua angka (b default = 0)"""
    return a + b


def rata_rata(angka: list[float]) -> float:
    """Menghitung rata-rata list angka, return 0 jika kosong"""
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# =========================
# CLASS
# =========================

class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float]):
        """Inisialisasi data mahasiswa"""
        self.nama = nama
        self.nim = nim
        
        if nilai is None:
            self.nilai = []
        else:
            self.nilai = nilai

    def tambah_nilai(self, skor: float):
        """Menambahkan satu nilai ke list"""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Mengembalikan rata-rata nilai"""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Menentukan status kelulusan berdasarkan threshold"""
        if self.rata_nilai() >= threshold:
            return 'LULUS'
        else:
            return 'TIDAK LULUS'

    def __str__(self):
        """Representasi string object"""
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai():.2f}, status={self.status()})"
        )


# =========================
# MAIN PROGRAM (DEMO)
# =========================

if __name__ == '__main__':
    
    # ===== FUNCTIONS =====
    print('=== FUNCTIONS ===')
    print(greet('Arifian'))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    # ===== CLASS STUDENT =====
    print('\n=== CLASS STUDENT ===')

    # Mahasiswa 1
    mahasiswa1 = Student('Adit', '2307110467', [90.5, 100.0, 80.5])
    mahasiswa1.tambah_nilai(97.5)

    print(mahasiswa1)
    print(mahasiswa1.rata_nilai())
    print(mahasiswa1.status())

    print('---')

    # Mahasiswa 2
    mahasiswa2 = Student('Budi', 'A123', [70.0, 65.5])
    mahasiswa2.tambah_nilai(75.0)

    print(mahasiswa2)
    print(mahasiswa2.rata_nilai())
    print(mahasiswa2.status())