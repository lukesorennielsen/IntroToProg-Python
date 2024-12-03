import matplotlib.pyplot as plt
import json

# Extract GPAs from the data
with open("./Demo03-UsingJupyterNotebooks/GPAData.json", "r") as file:
    list_of_dictionary_data = json.load(file)

gpas = [entry["GPA"] for entry in list_of_dictionary_data]

# Count the occurrences of each GPA value
gpa_counts = {gpa: gpas.count(gpa) for gpa in set(gpas)}

# Sort the GPA values for plotting
sorted_gpas = sorted(gpa_counts.keys())

# Corresponding counts for the sorted GPAs
count_values = [gpa_counts[gpa] for gpa in sorted_gpas]

# Create the bar chart
plt.figure(figsize=(6, 4))
plt.barh(sorted_gpas, count_values, align='center', alpha=0.7)  # Use barh for horizontal bars
plt.xlabel('Count')
plt.ylabel('GPA')
plt.title('Distribution of GPAs')
plt.yticks(sorted_gpas)
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Adjust grid for horizontal bars
plt.show()
