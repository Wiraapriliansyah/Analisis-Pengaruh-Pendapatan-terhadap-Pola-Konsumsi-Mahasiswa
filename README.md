### README: Analisis Data Mahasiswa

---

#### Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis terhadap data mahasiswa dengan fokus pada hubungan antara Total Uang Saku yang diterima oleh mereka dengan Total Konsumsi yang mereka lakukan. Data yang digunakan berasal dari tiga sumber berbeda: informasi personal mahasiswa (data_mahasiswa.csv), detail uang saku (uang_saku.csv), dan detail konsumsi harian (konsumsi_mahasiswa.csv). Analisis dilakukan untuk memberikan pemahaman yang lebih dalam tentang bagaimana variabel Total Uang Saku berpengaruh terhadap pola Total Konsumsi mahasiswa.

#### Langkah-langkah Analisis

---

1. **Penggabungan Data**

   Data dari tiga file CSV (data_mahasiswa.csv, uang_saku.csv, konsumsi_mahasiswa.csv) digabungkan menggunakan Pandas berdasarkan kolom 'Nama' untuk membentuk satu dataset gabungan. Ini memungkinkan kita untuk menggabungkan informasi personal, finansial, dan konsumsi harian menjadi satu kesatuan yang lebih mudah untuk dianalisis.

   ```python
   data = pd.merge(data_mahasiswa, uang_saku, on='Nama')
   data = pd.merge(data, konsumsi_mahasiswa, on='Nama')
   ```

2. **Informasi Data Gabungan**

   Setelah penggabungan, informasi tentang dataset gabungan ditampilkan untuk memastikan integritas data, jumlah observasi, dan tipe data masing-masing kolom.

   ```python
   print("Informasi Data Gabungan:")
   print(data.info())
   ```

3. **Penanganan Missing Values**

   Langkah ini dilakukan untuk menangani jika terdapat missing values dalam dataset. Pada contoh ini, jika ada missing values, mereka diisi dengan nilai rata-rata dari kolom terkait untuk mempertahankan kelengkapan data.

   ```python
   data = data.fillna(data.mean())
   ```

4. **Statistik Deskriptif**

   Analisis statistik deskriptif dilakukan untuk variabel Total Uang Saku dan Total Konsumsi, termasuk perhitungan mean, median, kuartil, dan range. Ini memberikan gambaran tentang distribusi data dan nilai-nilai tengahnya.

   ```python
   print("\nStatistik Deskriptif:")
   print(data[['Total Uang Saku (Rp)', 'Total Konsumsi (Rp)']].describe())
   ```

5. **Visualisasi Data**

   Visualisasi dilakukan menggunakan histogram untuk mengeksplorasi distribusi dari Total Uang Saku dan Total Konsumsi. Hal ini membantu dalam memahami pola distribusi dan kemungkinan anomali.

   ```python
   plt.figure(figsize=(12, 6))

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
   ```

6. **Model Regresi Linier**

   Variabel Total Uang Saku digunakan sebagai variabel independen (X) dan Total Konsumsi sebagai variabel dependen (y). Model regresi linier dibuat menggunakan metode Ordinary Least Squares (OLS) dari paket statsmodels.

   ```python
   X = data['Total Uang Saku (Rp)']
   y = data['Total Konsumsi (Rp)']

   X = sm.add_constant(X)  # Menambahkan intercept ke model

   model = sm.OLS(y, X).fit()  # Membuat model regresi

   print("\nHasil Regresi:")
   print(model.summary())  # Menampilkan summary hasil regresi
   ```

7. **Interpretasi Hasil Regresi**

   Hasil regresi ditafsirkan berdasarkan nilai-nilai seperti R-squared, Adj. R-squared, F-statistic, koefisien, dan p-value. Ini membantu dalam memahami seberapa baik model dapat menjelaskan variabilitas dalam Total Konsumsi berdasarkan Total Uang Saku.

8. **Visualisasi Hasil Regresi**

   Untuk memvisualisasikan hasil regresi, scatter plot digunakan dengan garis regresi yang menunjukkan hubungan antara Total Uang Saku dan Total Konsumsi. Visualisasi ini membantu dalam mengevaluasi kecocokan model terhadap data observasional.

   ```python
   plt.figure(figsize=(10, 6))
   sns.regplot(x='Total Uang Saku (Rp)', y='Total Konsumsi (Rp)', data=data, line_kws={'color': 'red'})
   plt.title('Regresi Linier Total Uang Saku vs Total Konsumsi')
   plt.xlabel('Total Uang Saku (Rp)')
   plt.ylabel('Total Konsumsi (Rp)')
   plt.show()
   ```

---

#### Kesimpulan

Analisis ini menunjukkan bahwa ada hubungan yang signifikan antara Total Uang Saku yang diterima oleh mahasiswa dengan Total Konsumsi yang mereka lakukan. Meskipun hubungan ini signifikan secara statistik, model hanya menjelaskan sebagian kecil dari variabilitas dalam Total Konsumsi. Variabel lain seperti karakteristik sosial ekonomi atau faktor lain mungkin perlu dipertimbangkan untuk menjelaskan lebih banyak variabilitas.

#### Rekomendasi

Untuk analisis yang lebih mendalam, disarankan untuk mempertimbangkan variabel tambahan seperti pendapatan keluarga, wilayah tempat tinggal, atau kebiasaan konsumsi lainnya yang dapat mempengaruhi Total Konsumsi mahasiswa. Selain itu, memperluas dataset dengan lebih banyak variabel yang relevan dapat meningkatkan prediksi dan interpretasi hasil regresi.

#### Catatan

- Pastikan semua paket Python yang diperlukan telah diinstal sebelum menjalankan script ini.
- Pastikan file data berada di direktori yang tepat atau sesuaikan path jika diperlukan.
- Anda dapat menyesuaikan analisis dan visualisasi lebih lanjut sesuai dengan tujuan spesifik proyek atau pertanyaan riset yang ingin dijawab.

---
