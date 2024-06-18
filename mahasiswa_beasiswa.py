import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")

# Hitung frekuensi mahasiswa yang mendapat beasiswa
beasiswa_count = data_mahasiswa['Penerima Beasiswa'].value_counts()

# Plot
plt.figure(figsize=(8, 6))
beasiswa_count.plot(kind='bar', color=['salmon', 'skyblue'])  # Ubah urutan warna
plt.title('Frekuensi Mahasiswa yang Mendapat Beasiswa')
plt.xlabel('Mendapat Beasiswa')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=0)

# Tambahkan total dan persentase di atas setiap bar
for i in range(len(beasiswa_count)):
    plt.text(i, beasiswa_count[i], str(beasiswa_count[i]), ha='center', va='bottom')
    plt.text(i, beasiswa_count[i] / 2, f"{((beasiswa_count[i] / len(data_mahasiswa)) * 100):.2f}%", ha='center', va='bottom')

plt.show()

# Print jumlah dan persentase mahasiswa yang mendapat beasiswa
print("Jumlah Mahasiswa yang Mendapat Beasiswa:")
print(beasiswa_count)
print("\nPersentase Mahasiswa yang Mendapat Beasiswa:")
print((beasiswa_count / len(data_mahasiswa)) * 100)
