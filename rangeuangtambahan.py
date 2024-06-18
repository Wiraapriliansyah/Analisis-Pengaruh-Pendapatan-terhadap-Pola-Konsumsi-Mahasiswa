import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_uang_saku = pd.read_csv("uang_saku.csv")

# Membuat range uang saku tambahan per bulan
bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, float('inf')]
labels = ['< 1jt', '1jt - 2jt', '2jt - 3jt', '3jt - 4jt', '4jt - 5jt', '> 5jt']
data_uang_saku['Range Uang Saku Tambahan (per bulan)'] = pd.cut(data_uang_saku['Uang Saku Tambahan (Rp)'], bins=bins, labels=labels, right=False)

# Visualisasi
range_uang_saku_tambahan_count = data_uang_saku['Range Uang Saku Tambahan (per bulan)'].value_counts().sort_index()
total_mahasiswa = range_uang_saku_tambahan_count.sum()
range_uang_saku_tambahan_percentage = (range_uang_saku_tambahan_count / total_mahasiswa) * 100

plt.figure(figsize=(10, 6))
range_uang_saku_tambahan_count.plot(kind='bar', color='lightgreen')
plt.title('Distribusi Range Uang Saku Tambahan per Bulan Mahasiswa')
plt.xlabel('Range Uang Saku Tambahan (per bulan)')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

for i in range(len(range_uang_saku_tambahan_count)):
    plt.text(i, range_uang_saku_tambahan_count[i] + 0.1, f"{range_uang_saku_tambahan_count[i]} ({range_uang_saku_tambahan_percentage.iloc[i]:.1f}%)", ha='center')

plt.show()
