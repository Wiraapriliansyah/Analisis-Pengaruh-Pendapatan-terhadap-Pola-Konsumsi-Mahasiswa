import pandas as pd

# Load data
data_uang_saku = pd.read_csv("uang_saku.csv")

# Menghitung total uang saku orang tua per mahasiswa
data_uang_saku['Total Uang Saku Orang Tua (Rp)'] = data_uang_saku['Uang Saku Orang Tua (Rp)'] + data_uang_saku['Uang Saku Beasiswa (Rp)'] + data_uang_saku['Uang Saku Tambahan (Rp)']

# Membuat range uang saku orang tua per bulan
bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, float('inf')]
labels = ['< 1jt', '1jt - 2jt', '2jt - 3jt', '3jt - 4jt', '4jt - 5jt', '> 5jt']
data_uang_saku['Range Uang Saku Orang Tua (per bulan)'] = pd.cut(data_uang_saku['Total Uang Saku Orang Tua (Rp)'], bins=bins, labels=labels, right=False)

# Menghitung jumlah mahasiswa untuk setiap range uang saku orang tua
range_uang_saku_count = data_uang_saku['Range Uang Saku Orang Tua (per bulan)'].value_counts().sort_index()

# Menghitung persentase mahasiswa untuk setiap range uang saku orang tua
total_mahasiswa = range_uang_saku_count.sum()
range_uang_saku_percentage = (range_uang_saku_count / total_mahasiswa) * 100

# Membuat visualisasi
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
range_uang_saku_count.plot(kind='bar', color='salmon')
plt.title('Distribusi Range Uang Saku Orang Tua per Bulan Mahasiswa')
plt.xlabel('Range Uang Saku Orang Tua (per bulan)')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Menambahkan total dan persentase di atas bar
for i in range(len(range_uang_saku_count)):
    plt.text(i, range_uang_saku_count.iloc[i] + 0.1, f"{range_uang_saku_count.iloc[i]} ({range_uang_saku_percentage.iloc[i]:.1f}%)", ha='center')

plt.show()
