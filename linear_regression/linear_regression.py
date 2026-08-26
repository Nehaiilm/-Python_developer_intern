"""
Linear Regression - House Price Prediction
---------------------------------------------
Trains a linear regression model to predict house prices from features
like area, bedrooms, bathrooms, age, and distance from city center.
Evaluates the model and visualizes actual vs predicted prices.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ----------------------------------------------------------------------
# 1. Load the dataset
# ----------------------------------------------------------------------
df = pd.read_csv("house_data.csv")
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values per column:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe())

# ----------------------------------------------------------------------
# 2. Split features and target
# ----------------------------------------------------------------------
features = ["Area_SqFt", "Bedrooms", "Bathrooms", "Age_Years", "Distance_From_City_KM"]
target = "Price"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}, Test samples: {len(X_test)}")

# ----------------------------------------------------------------------
# 3. Train the model
# ----------------------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel coefficients:")
for feat, coef in zip(features, model.coef_):
    print(f"  {feat}: {coef:.2f}")
print(f"  Intercept: {model.intercept_:.2f}")

# ----------------------------------------------------------------------
# 4. Predict and evaluate
# ----------------------------------------------------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nModel Evaluation on Test Set:")
print(f"  MAE  : Rs. {mae:,.2f}")
print(f"  RMSE : Rs. {rmse:,.2f}")
print(f"  R2 Score: {r2:.4f}")

# ----------------------------------------------------------------------
# 5. Save predictions
# ----------------------------------------------------------------------
results = X_test.copy()
results["Actual_Price"] = y_test.values
results["Predicted_Price"] = y_pred.round(0).astype(int)
results["Error"] = (results["Actual_Price"] - results["Predicted_Price"]).round(0)
results.to_csv("predictions.csv", index=False)
print("\nSaved predictions to predictions.csv")

# ----------------------------------------------------------------------
# 6. Visualization -> house_price_prediction.png
# ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# (a) Actual vs Predicted scatter
axes[0].scatter(y_test, y_pred, alpha=0.6, color="#4C72B0", edgecolor="k")
min_val, max_val = y_test.min(), y_test.max()
axes[0].plot([min_val, max_val], [min_val, max_val], "r--", label="Perfect Prediction")
axes[0].set_xlabel("Actual Price (Rs.)")
axes[0].set_ylabel("Predicted Price (Rs.)")
axes[0].set_title("Actual vs Predicted House Prices")
axes[0].legend()
axes[0].ticklabel_format(style="plain")

# (b) Feature importance (coefficients)
axes[1].barh(features, model.coef_, color="#55A868")
axes[1].set_title("Feature Coefficients (Impact on Price)")
axes[1].set_xlabel("Coefficient Value")
axes[1].axvline(0, color="black", linewidth=0.8)

plt.tight_layout()
plt.savefig("house_price_prediction.png", dpi=150)
print("Saved chart to house_price_prediction.png")

# ----------------------------------------------------------------------
# 7. Predict a new sample house
# ----------------------------------------------------------------------
sample_house = pd.DataFrame([{
    "Area_SqFt": 2000,
    "Bedrooms": 3,
    "Bathrooms": 2,
    "Age_Years": 5,
    "Distance_From_City_KM": 8.0
}])
predicted_price = model.predict(sample_house)[0]
print(f"\nSample prediction for a 2000 sqft, 3BHK, 5-year-old house "
      f"8km from city center: Rs. {predicted_price:,.0f}")
