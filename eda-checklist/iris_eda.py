# iris_eda.py

# Import libraries
import pandas as pd
import plotly.express as px

# Step 1: Load dataset
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(data_url)

# -------------------------------
# Basic understanding of dataset
# -------------------------------
print("Preview of dataset:\n")
print(iris_df.head())

print("\nShape of dataset (rows, columns):")
print(iris_df.shape)

print("\nColumn names:")
print(list(iris_df.columns))

# Observation:
# The dataset has 150 records and 5 columns (4 numerical + 1 categorical target)

# -------------------------------
# Data types and missing values
# -------------------------------
print("\nDetailed info:\n")
iris_df.info()

print("\nChecking for null values:\n")
print(iris_df.isna().sum())

# Observation:
# No missing values detected. Data is clean.

# -------------------------------
# Unique categories in target
# -------------------------------
print("\nSpecies distribution:\n")
print(iris_df["species"].value_counts())

# Observation:
# All three species have equal number of samples (balanced dataset)

# -------------------------------
# Distribution of petal_length
# -------------------------------
petal_len_plot = px.histogram(
    iris_df,
    x="petal_length",
    color="species",
    title="Petal Length Distribution Across Species",
    nbins=25
)
petal_len_plot.show()

# Observation:
# Clear grouping:
# - Setosa: very small petals
# - Versicolor: mid-range
# - Virginica: larger petals

# -------------------------------
# Outlier check using box plot
# -------------------------------
petal_box = px.box(
    iris_df,
    y="petal_length",
    color="species",
    title="Petal Length Spread (Box Plot)"
)
petal_box.show()

# Observation:
# Very few extreme values. Overall data looks consistent.

# -------------------------------
# Relationship between features
# -------------------------------
scatter_plot = px.scatter(
    iris_df,
    x="petal_length",
    y="petal_width",
    color="species",
    title="Petal Length vs Petal Width"
)
scatter_plot.show()

# Observation:
# Strong linear relationship.
# Setosa is completely separated from the others.
# Slight overlap between versicolor and virginica.

# -------------------------------
# Correlation check
# -------------------------------
corr_vals = iris_df.corr(numeric_only=True)

heatmap_plot = px.imshow(
    corr_vals,
    text_auto=True,
    title="Feature Correlation Matrix"
)
heatmap_plot.show()

# Observation:
# Petal length and width are highly correlated.
# Sepal features are less correlated comparatively.

# -------------------------------
# Aggregated statistics by species
# -------------------------------
print("\nAverage feature values by species:\n")
print(iris_df.groupby("species").mean())

# Observation:
# Petal dimensions increase from setosa -> versicolor -> virginica
# Sepal width behaves slightly differently (setosa tends to have wider sepals)

# -------------------------------
# Extra check (optional but useful)
# -------------------------------
pair_plot = px.scatter_matrix(
    iris_df,
    color="species",
    title="Pairwise Feature Relationships"
)
pair_plot.show()

# Observation:
# Petal features provide better separation than sepal features.

# -------------------------------
# Final thoughts
# -------------------------------
# 1. Dataset is clean and balanced
# 2. Petal features are most useful for classification
# 3. Setosa is easily distinguishable
# 4. Some overlap exists between versicolor and virginica