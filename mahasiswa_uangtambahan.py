import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")

# Hitung frekuensi mahasiswa yang mendapat uang saku tambahan
uang_saku_count = data_mahasiswa['Penerima Uang Saku Tambahan'].value_counts()

# Plot
plt.figure(figsize=(8, 6))
uang_saku_count.plot(kind='bar', color=['skyblue', 'salmon'])  # Perbaikan urutan warna
plt.title('Frekuensi Mahasiswa yang Mendapat Uang Saku Tambahan')
plt.xlabel('Mendapat Uang Saku Tambahan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=0)

# Tambahkan total dan persentase di atas setiap bar
for i in range(len(uang_saku_count)):
    plt.text(i, uang_saku_count[i], str(uang_saku_count[i]), ha='center', va='bottom')
    plt.text(i, uang_saku_count[i] / 2, f"{((uang_saku_count[i] / len(data_mahasiswa)) * 100):.2f}%", ha='center', va='bottom')

plt.show()

# Print jumlah dan persentase mahasiswa yang mendapat uang saku tambahan
print("Jumlah Mahasiswa yang Mendapat Uang Saku Tambahan:")
print(uang_saku_count)
print("\nPersentase Mahasiswa yang Mendapat Uang Saku Tambahan:")
print((uang_saku_count / len(data_mahasiswa)) * 100)
