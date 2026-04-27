import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from src.data_loader import load_data
from src.preprocessing import clean_data

# -------------------------------
# Load & Clean Data
# -------------------------------
df = load_data("data/flight_data.csv")
df = clean_data(df)

# -------------------------------
# Feature Selection
# -------------------------------
features = [
    "DAY_OF_WEEK",
    "DEP_DELAY",
    "DISTANCE"
]

target = "ARR_DEL15"

# Drop missing values
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# -------------------------------
# Train/Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Model Performance ---")
print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -------------------------------
# Feature Importance
# -------------------------------


importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance = importance.sort_values(by="Coefficient", ascending=False)

print("\n--- Feature Importance ---")
print(importance)