import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
os.makedirs('/mnt/data/', exist_ok=True)


# Task data for SHEMS UI development
tasks = [
    ("Requirements Gathering", "All", 0, 1),
    ("Wireframing", "Isha", 1, 2),
    ("Interactive Prototyping", "Isha", 2, 3),
    ("Dashboard UI", "Zainab", 2, 4),
    ("Control Panel UI", "Saad", 3, 5),
    ("Reports & Analytics UI", "Ali", 4, 6),
    ("UI Testing", "All", 6, 7),
    ("Feedback Integration", "All", 7, 8),
]

# Mapping names to colors
colors = {
    "Isha": "#4F81BD",
    "Zainab": "#C0504D",
    "Saad": "#9BBB59",
    "Ali": "#8064A2",
    "All": "#F79646"
}

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
yticks = []
yticklabels = []

for i, (task, person, start, end) in enumerate(reversed(tasks)):
    y = i
    ax.barh(y, end - start, left=start, height=0.5, color=colors[person])
    yticks.append(y)
    yticklabels.append(task)

# Formatting
ax.set_yticks(yticks)
ax.set_yticklabels(reversed(yticklabels))
ax.set_xticks(range(9))
ax.set_xticklabels([f"Week {i+1}" for i in range(8)] + [""])
ax.set_xlabel("Timeline")
ax.set_title("SHEMS UI Development - Gantt Chart")

# Legend
patches = [mpatches.Patch(color=color, label=name) for name, color in colors.items()]
ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
file_path = "/mnt/data/SHEMS_UI_Gantt_Chart.png"
plt.savefig(file_path)
file_path
plt.show()
