import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data_mahasiswa = pd.read_csv("data_mahasiswa.csv")

# Calculate the frequency of students by semester
semester_count = data_mahasiswa['Semester'].value_counts().sort_index()

# Plot
plt.figure(figsize=(12, 8))  # Increase the figure size
colors = ['lightgreen', 'lightblue', 'orange', 'lightcoral', 'lightpink', 'lightskyblue', 'lightgrey', 'lightyellow']
semester_count.plot(kind='bar', color=colors, width=0.8)  # Adjust the bar width

plt.title('Frequency of Students by Semester', fontsize=16, weight='bold')  # Increase the title font size
plt.xlabel('Semester', fontsize=14)  # Increase the label font size
plt.ylabel('Number of Students', fontsize=14)  # Increase the label font size
plt.xticks(rotation=0, fontsize=12)  # Increase the tick label font size

# Add total and percentage above each bar
total_students = semester_count.sum()
for i, count in enumerate(semester_count):
    percentage = (count / total_students) * 100
    plt.text(i, count + 0.5, f"{count}\n({percentage:.2f}%)", ha='center', va='bottom', fontsize=10, weight='bold')

# Display total number of students
plt.text(7, 35, f"Total Students: {total_students}", ha='right', va='bottom', fontsize=12, weight='bold')  # Adjust position and font size

plt.tight_layout()
plt.show()

# Print the number of students by semester
print("Number of Students by Semester:")
print(semester_count)
