# Linear Regression - House Price Prediction

A supervised machine learning task: predict house prices from property
features using scikit-learn's Linear Regression.

## Files
- `house_data.csv` — dataset (200 houses, 5 features + price)
- `linear_regression.py` — loads data, trains the model, evaluates it, saves outputs
- `predictions.csv` — test set predictions vs actual prices
- `house_price_prediction.png` — actual vs predicted scatter plot + feature coefficients
- `Report.docx` — write-up of objective, methodology, results, and conclusion

## How to run
```bash
pip install pandas numpy matplotlib scikit-learn
python linear_regression.py
```

## What it does
1. Loads `house_data.csv` and checks for missing values
2. Splits data into 80% training / 20% test sets
3. Trains a `LinearRegression` model on: Area_SqFt, Bedrooms, Bathrooms,
   Age_Years, Distance_From_City_KM
4. Evaluates the model with MAE, RMSE, and R² score
5. Saves test-set predictions to `predictions.csv`
6. Generates `house_price_prediction.png` (actual vs predicted + feature coefficients)
7. Predicts the price of a sample house as a demo

## Results
- **R² Score:** 0.9966 (explains ~99.7% of price variance on unseen data)
- **MAE:** ~Rs. 1,30,000
- **RMSE:** ~Rs. 1,55,000

Bedrooms and Bathrooms have the strongest positive effect on price; Age and
Distance from city center have a negative effect, as expected.
