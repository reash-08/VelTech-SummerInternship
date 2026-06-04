import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")
charts_dir = os.path.join(script_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(csv_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

sns.set_style("whitegrid")

def save_chart(name):
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, name))
    plt.close()

# ==========================
# 1. Bar Chart
# ==========================
plt.figure(figsize=(8,5))
sns.countplot(x="Accident_Severity", data=df)
plt.title("Accident Severity Distribution")
save_chart("01_bar_chart.png")

# ==========================
# 2. Pie Chart
# ==========================
plt.figure(figsize=(7,7))
df["Urban_or_Rural_Area"].value_counts().plot.pie(
    autopct="%1.1f%%"
)
plt.title("Urban vs Rural")
plt.ylabel("")
save_chart("02_pie_chart.png")

# ==========================
# 3. Histogram
# ==========================
plt.figure(figsize=(8,5))
plt.hist(df["Speed_limit"], bins=15)
plt.title("Speed Limit Distribution")
save_chart("03_histogram.png")

# ==========================
# 4. Line Chart
# ==========================
monthly = df.groupby(df["Date"].dt.month).size()

plt.figure(figsize=(8,5))
monthly.plot(marker="o")
plt.title("Monthly Accident Trend")
save_chart("04_line_chart.png")

# ==========================
# 5. Scatter Plot
# ==========================
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Number_of_Vehicles",
    y="Number_of_Casualties",
    data=df.sample(5000)
)
plt.title("Vehicles vs Casualties")
save_chart("05_scatter_plot.png")

# ==========================
# 6. Box Plot
# ==========================
plt.figure(figsize=(8,5))
sns.boxplot(
    x="Accident_Severity",
    y="Speed_limit",
    data=df
)
plt.title("Severity vs Speed")
save_chart("06_box_plot.png")

# ==========================
# 7. Violin Plot
# ==========================
plt.figure(figsize=(8,5))
sns.violinplot(
    x="Accident_Severity",
    y="Speed_limit",
    data=df
)
plt.title("Violin Plot")
save_chart("07_violin_plot.png")

# ==========================
# 8. Heatmap
# ==========================
numeric = df.select_dtypes(include="number")

plt.figure(figsize=(12,8))
sns.heatmap(
    numeric.corr(),
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
save_chart("08_heatmap.png")

# ==========================
# 9. Count Plot
# ==========================
plt.figure(figsize=(10,5))
sns.countplot(
    y="Weather_Conditions",
    data=df,
    order=df["Weather_Conditions"].value_counts().index[:10]
)
plt.title("Weather Conditions")
save_chart("09_countplot.png")

# ==========================
# 10. KDE Plot
# ==========================
plt.figure(figsize=(8,5))
sns.kdeplot(
    df["Speed_limit"],
    fill=True
)
plt.title("Speed Density")
save_chart("10_kde_plot.png")

# ==========================
# 11. Area Chart
# ==========================
yearly = df.groupby("Year").size()

plt.figure(figsize=(8,5))
plt.fill_between(
    yearly.index,
    yearly.values
)
plt.title("Yearly Accidents Area Chart")
save_chart("11_area_chart.png")

# ==========================
# 12. Hexbin Plot
# ==========================
plt.figure(figsize=(8,5))
plt.hexbin(
    df["Number_of_Vehicles"],
    df["Number_of_Casualties"],
    gridsize=25
)
plt.colorbar()
plt.title("Hexbin Plot")
save_chart("12_hexbin_plot.png")

# ==========================
# 13. Strip Plot
# ==========================
plt.figure(figsize=(8,5))
sns.stripplot(
    x="Accident_Severity",
    y="Speed_limit",
    data=df.sample(5000)
)
plt.title("Strip Plot")
save_chart("13_strip_plot.png")

# ==========================
# 14. Swarm Plot
# ==========================
plt.figure(figsize=(8,5))
sns.swarmplot(
    x="Accident_Severity",
    y="Speed_limit",
    data=df.sample(1000)
)
plt.title("Swarm Plot")
save_chart("14_swarm_plot.png")

# ==========================
# 15. ECDF Plot
# ==========================
plt.figure(figsize=(8,5))
sns.ecdfplot(
    data=df,
    x="Speed_limit"
)
plt.title("ECDF Plot")
save_chart("15_ecdf_plot.png")

print("="*50)
print("15 DIFFERENT VISUALIZATIONS CREATED")
print("Saved inside charts folder")
print("="*50)