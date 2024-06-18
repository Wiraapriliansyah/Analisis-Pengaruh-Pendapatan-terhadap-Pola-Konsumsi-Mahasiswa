import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_uang_saku = pd.read_csv("uang_saku.csv")

# Menghitung total uang saku dari beasiswa per mahasiswa
data_uang_saku['Total Uang Saku Beasiswa (Rp)'] = data_uang_saku['Uang Saku Beasiswa (Rp)'] + data_uang_saku['Uang Saku Tambahan (Rp)']

# Membuat range uang saku dari beasiswa per bulan
bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, float('inf')]
labels = ['< 1jt', '1jt - 2jt', '2jt - 3jt', '3jt - 4jt', '4jt - 5jt', '> 5jt']
data_uang_saku['Range Uang Saku Beasiswa (per bulan)'] = pd.cut(data_uang_saku['Total Uang Saku Beasiswa (Rp)'], bins=bins, labels=labels, right=False)

# Visualisasi
range_uang_saku_beasiswa_count = data_uang_saku['Range Uang Saku Beasiswa (per bulan)'].value_counts().sort_index()
total_mahasiswa = range_uang_saku_beasiswa_count.sum()
range_uang_saku_beasiswa_percentage = (range_uang_saku_beasiswa_count / total_mahasiswa) * 100

plt.figure(figsize=(10, 6))
range_uang_saku_beasiswa_count.plot(kind='bar', color='skyblue')
plt.title('Distribusi Range Uang Saku dari Beasiswa per Bulan Mahasiswa')
plt.xlabel('Range Uang Saku Beasiswa (per bulan)')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

for i in range(len(range_uang_saku_beasiswa_count)):
    plt.text(i, range_uang_saku_beasiswa_count[i] + 0.1, f"{range_uang_saku_beasiswa_count[i]} ({range_uang_saku_beasiswa_percentage.iloc[i]:.1f}%)", ha='center')

plt.show()
