import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")

# Buat plot untuk frekuensi jenis kelamin
plt.figure(figsize=(8, 6))
jenis_kelamin_counts = data_mahasiswa['Jenis Kelamin'].value_counts()
jenis_kelamin_counts.plot(kind='bar', color=['skyblue', 'salmon'])

# Tambahkan jumlah dan persentase di atas setiap batang
for i, count in enumerate(jenis_kelamin_counts):
    plt.text(i, count + 0.1, f"{count} ({count / len(data_mahasiswa) * 100:.1f}%)", ha='center')

plt.title('Frekuensi Mahasiswa Berdasarkan Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Frekuensi')
plt.xticks(rotation=0)
plt.show()
