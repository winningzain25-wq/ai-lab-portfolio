# Lab 05 — Titanic Classification

## Contents
- `titanic_classification.ipynb` — fully executed solution (objectives, model comparisons, five exercises and home assignment).
- `sample-data.csv` — copied original 100-row dataset.
- `titanic_best_model.joblib` — tuned, fitted sklearn preprocessing+model pipeline.
- `*_encoder.pkl` — required encoder compatibility artifacts (the five files).
- `figures/roc_curve.png` — ROC curve for the final tuned model.
- `report.md` — lab report with exact measured results.
- `results.json` — machine-readable summary.

## How to open and run
1. Extract the archive. Open your terminal **inside the `lab05` folder**.
2. Install dependencies if needed: `python -m pip install jupyter numpy pandas scikit-learn matplotlib joblib nbformat nbclient`
3. Run `jupyter notebook titanic_classification.ipynb` and use **Kernel → Restart & Run All**.
4. The notebook expects `sample-data.csv` to be in the same working folder.

## How to use the saved model

```python
import joblib
import pickle
import pandas as pd

model = joblib.load("titanic_best_model.joblib")  # only load trusted model files
with open("survived_encoder.pkl", "rb") as f:
    target_encoder = pickle.load(f)  # only load trusted files

passenger = pd.DataFrame([{
    "PClass": "First", "Gender": "Female", "Sibling": "Zero", "Embarked": "Southampton"
}])
encoded_prediction = model.predict(passenger)
print(target_encoder.inverse_transform(encoded_prediction)[0])
```

**Important:** The feature label-encoder `.pkl` files exist to satisfy the lab deliverables and legacy compatibility; the saved pipeline expects *raw category text* and automatically applies its own fitted one-hot encoder. No external `LabelEncoder.transform()` is needed for input.

**Data limitation:** There are only 100 records, balanced 50/50. Real `FamilySize` and `IsAlone` cannot be obtained from the CSV; Exercise 1 uses explicitly labeled sibling-only proxies.
