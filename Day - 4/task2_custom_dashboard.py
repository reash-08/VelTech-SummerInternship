import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")
out_path = os.path.join(script_dir, "accident_dashboard(task-2).png")

# Load Dataset
df = pd.read_csv(csv_path)

# -----------------------------
# Dashboard Style
# -----------------------------
plt.style.use("ggplot")

# Create Figure
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# =====================================
# 1. Average Casualties by Road Type
# =====================================

road_avg = (
    df.groupby("Road_Type")["Number_of_Casualties"]
    .mean()
    .sort_values(ascending=False)
)

bars = axes[0,0].bar(
    road_avg.index,
    road_avg.values,
    color="skyblue"
)

axes[0,0].set_title(
    "Average Casualties by Road Type",
    fontsize=12,
    fontweight="bold"
)

axes[0,0].tick_params(
    axis='x',
    rotation=45
)

# Add values on bars
for bar in bars:
    height = bar.get_height()

    axes[0,0].text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

# =====================================
# 2. Severity Distribution
# =====================================

severity_counts = (
    df["Accident_Severity"]
    .value_counts()
)

axes[0,1].pie(
    severity_counts,
    labels=severity_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[0,1].set_title(
    "Accident Severity Distribution",
    fontsize=12,
    fontweight="bold"
)

# =====================================
# 3. Monthly Accident Trend
# =====================================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

monthly = (
    df.groupby(df["Date"].dt.month)
    .size()
)

axes[1,0].plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2
)

axes[1,0].set_title(
    "Monthly Accident Trend",
    fontsize=12,
    fontweight="bold"
)

axes[1,0].set_xlabel("Month")
axes[1,0].set_ylabel("Accident Count")

# =====================================
# 4. Speed Limit Distribution
# =====================================

sns.histplot(
    df["Speed_limit"],
    bins=15,
    kde=True,
    ax=axes[1,1],
    color="orange"
)

mean_speed = df["Speed_limit"].mean()

axes[1,1].axvline(
    mean_speed,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean = {mean_speed:.2f}"
)

axes[1,1].legend()

axes[1,1].set_title(
    "Speed Limit Distribution",
    fontsize=12,
    fontweight="bold"
)

# =====================================
# Dashboard Title
# =====================================

plt.suptitle(
    "Road Accident Analysis Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    out_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Dashboard Created Successfully")