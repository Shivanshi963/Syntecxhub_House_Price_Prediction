from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Load dataset
housing = fetch_california_housing(as_frame=True)

df = housing.frame

# Features (Input)
X = df.drop("MedHouseVal", axis=1)

# Target (Output)
y = df["MedHouseVal"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# R² Score
r2 = r2_score(y_test, y_pred)

print("\nRMSE:", rmse)
print("R2 Score:", r2)
print("\nFeature Coefficients:")

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)
import joblib

joblib.dump(model, "models/house_price_model.pkl")

print("\nModel saved successfully!")
sample_house = [[
    8.0,     # MedInc
    25,      # HouseAge
    6.0,     # AveRooms
    1.0,     # AveBedrms
    3000,    # Population
    4.0,     # AveOccup
    37.0,    # Latitude
    -122.0   # Longitude
]]

prediction = model.predict(sample_house)

print("\nPredicted House Price:", prediction[0])