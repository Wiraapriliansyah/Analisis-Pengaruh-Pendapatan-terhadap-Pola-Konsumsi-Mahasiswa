import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV file
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")

# Ambil daftar unik jurusan
jurusan_unik = data_mahasiswa['Jurusan'].unique()

# Buat palet warna yang berbeda untuk setiap jurusan
colors = plt.cm.tab10(np.linspace(0, 1, len(jurusan_unik)))

# Buat plot untuk frekuensi jurusan dengan warna yang berbeda
plt.figure(figsize=(12, 6))

# Inisialisasi list untuk menyimpan frekuensi total
frekuensi_total = []

for i, jurusan in enumerate(jurusan_unik):
    jurusan_data = data_mahasiswa[data_mahasiswa['Jurusan'] == jurusan]
    frekuensi = len(jurusan_data)
    frekuensi_total.append(frekuensi)
    plt.bar(jurusan, frekuensi, color=colors[i], label=jurusan)
    
    # Tambahkan anotasi untuk frekuensi di atas masing-masing batang
    plt.text(jurusan, frekuensi, str(frekuensi), ha='center', va='bottom')

plt.title('Frekuensi Mahasiswa Berdasarkan Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Frekuensi')
plt.legend(title='Jurusan', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Tampilkan frekuensi total untuk setiap jurusan
frekuensi_total_df = pd.DataFrame({'Jurusan': jurusan_unik, 'Frekuensi': frekuensi_total})
print(frekuensi_total_df)
