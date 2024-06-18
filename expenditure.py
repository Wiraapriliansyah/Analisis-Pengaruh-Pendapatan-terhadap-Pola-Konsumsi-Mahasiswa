import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")
konsumsi_mahasiswa = pd.read_csv("konsumsi_mahasiswa.csv")

# Combine data
combined_data = pd.merge(data_mahasiswa, konsumsi_mahasiswa, on="Nama")

# Define bin edges for expenditure categories
bin_edges = [0, 200000, 400000, 600000, 800000, 1000000, float('inf')]
bin_labels = ['200rb', '400rb', '600rb', '800rb', '1jt', '> 1jt']

# Calculate category percentages
category_percentages = {}
for category in konsumsi_mahasiswa.columns[1:]:
    category_counts = pd.cut(konsumsi_mahasiswa[category], bins=bin_edges, labels=bin_labels, right=False).value_counts().sort_index()
    total_students = category_counts.sum()
    category_percentage = (category_counts / total_students) * 100
    category_percentages[category] = category_percentage

# Plotting
plt.figure(figsize=(10, 6))

colors = plt.cm.tab10(range(len(konsumsi_mahasiswa.columns[1:])))
bottom = None
for i, category in enumerate(konsumsi_mahasiswa.columns[1:]):
    category_percentage = category_percentages[category]
    plt.bar(bin_labels, category_percentage, label=category, color=colors[i], bottom=bottom)
    if bottom is None:
        bottom = category_percentage
    else:
        bottom += category_percentage

plt.title('Distribusi Konsumsi Mahasiswa berdasarkan Kategori')
plt.xlabel('Range Pengeluaran')
plt.ylabel('Persentase Mahasiswa (%)')
plt.xticks(rotation=45)
plt.legend(title='Kategori Konsumsi', loc='upper right')
plt.tight_layout()

plt.show()
