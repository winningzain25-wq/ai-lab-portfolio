# Lab 01 Report — Environment Setup and Dataset Inspection

## 1. Environment Setup

A Conda environment named `ai-lab` was created using Python 3.11.

The Jupyter kernel was registered as `Python (ai-lab)` and used for the laboratory notebook.

## 2. Jupyter Notebook

The notebook was named `lab01_setup.ipynb`.

The required Python test was executed successfully:

```text
Hello, Introduction to Artificial Intelligence

Pandas was installed and its version was checked successfully.

3. Titanic Dataset Inspection

The Titanic dataset was loaded from the provided public CSV URL.

Dataset shape:

(891, 15)

The dataset was inspected using:

df.head()
df.info()
df.describe()
Missing-value counts and percentages
Missing Values

The three columns with the largest missing-value counts were:

Column	Missing Values
deck	688
age	177
embarked	2

The deck column has the largest amount of missing data, with approximately 77.22% missing values. The age column has approximately 19.87% missing values.

Numeric Variability

The coefficient abs(std / mean) was calculated for the numeric columns.

The largest value was for:

parch = 2.112344

This indicates that parch has the largest relative variability among the numeric columns considered. Its standard deviation is more than twice its mean, showing substantial variation relative to its average value.

4. Dataset Inspection Script

A reusable Python script named inspect.py was created.

The script reports:

Source
Dataset shape
Data types
Missing-value counts
Missing-value percentages
Numeric summary statistics

The script was tested successfully using the Titanic dataset.

5. Reproducibility

The project includes:

requirements.txt
.gitignore
Jupyter notebook
Dataset inspection script
Lab report

These files help make the work easier to reproduce and maintain.
