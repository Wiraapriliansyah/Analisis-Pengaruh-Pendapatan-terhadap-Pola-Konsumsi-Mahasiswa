import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Membaca data dari file CSV
data_mahasiswa = pd.read_csv('data_mahasiswa.csv')
uang_saku = pd.read_csv('uang_saku.csv')
konsumsi_mahasiswa = pd.read_csv('konsumsi_mahasiswa.csv')

# Menggabungkan data berdasarkan kolom 'Nama'
data = pd.merge(data_mahasiswa, uang_saku, on='Nama')
data = pd.merge(data, konsumsi_mahasiswa, on='Nama')

# Menampilkan informasi tentang data gabungan
print("Informasi Data Gabungan:")
print(data.info())

# Menampilkan beberapa baris pertama dari data gabungan
print("\nData Gabungan:")
print(data.head())

# Menangani missing values jika ada
# Mengisi missing values hanya pada kolom-kolom numerik dengan nilai rata-rata
numeric_cols = ['Uang Saku Orang Tua (Rp)', 'Uang Saku Beasiswa (Rp)', 'Uang Saku Tambahan (Rp)', 
                'Total Uang Saku (Rp)', 'Konsumsi Makanan (Rp)', 'Konsumsi Transportasi (Rp)', 
                'Konsumsi Hiburan (Rp)', 'Konsumsi Pakaian (Rp)', 'Konsumsi Lainnya (Rp)', 
                'Total Konsumsi (Rp)']
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Memastikan tidak ada missing values setelah penanganan
print("\nMissing Values setelah penanganan:")
print(data.isnull().sum())

# Menampilkan statistik deskriptif
print("\nStatistik Deskriptif:")
print(data[numeric_cols].describe())

# Plot distribusi Total Uang Saku dan Total Konsumsi
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(data['Total Uang Saku (Rp)'], kde=True)
plt.title('Distribusi Total Uang Saku')
plt.xlabel('Total Uang Saku (Rp)')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
sns.histplot(data['Total Konsumsi (Rp)'], kde=True)
plt.title('Distribusi Total Konsumsi')
plt.xlabel('Total Konsumsi (Rp)')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Memisahkan variabel independen (X) dan dependen (y)
X = data['Total Uang Saku (Rp)']
y = data['Total Konsumsi (Rp)']

# Menambahkan konstanta ke model (intercept)
X = sm.add_constant(X)

# Membuat model regresi
model = sm.OLS(y, X).fit()

# Menampilkan ringkasan hasil regresi
print("\nHasil Regresi:")
print(model.summary())

# Visualisasi hasil regresi
plt.figure(figsize=(10, 6))
sns.regplot(x='Total Uang Saku (Rp)', y='Total Konsumsi (Rp)', data=data, line_kws={'color': 'red'})
plt.title('Regresi Linier Total Uang Saku vs Total Konsumsi')
plt.xlabel('Total Uang Saku (Rp)')
plt.ylabel('Total Konsumsi (Rp)')
plt.show()
