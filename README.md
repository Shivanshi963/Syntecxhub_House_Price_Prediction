 🏠 House Price Prediction using Machine Learning

 📌 Project Overview

This project predicts house prices using a **Linear Regression Machine Learning model** trained on the California Housing Dataset.

The goal is to analyze housing-related features and estimate the median house value based on factors such as income, house age, number of rooms, population, and geographical location.

 🚀 Features

* Data Loading and Exploration
* Data Analysis using Pandas
* Feature Selection
* Train-Test Data Splitting
* Linear Regression Model Training
* Model Evaluation using RMSE and R² Score
* Feature Coefficient Interpretation
* Model Saving using Joblib
* Sample House Price Prediction

 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib

📂 Project Structure

```text
Syntecxhub_House_Price_Prediction
│
├── dataset
│   └── housing.csv
│
├── models
│   └── house_price_model.pkl
│
├── house_price_prediction.py
├── README.md
└── requirements.txt
```

---

## 📊 Dataset Information

The project uses the California Housing Dataset available through Scikit-Learn.

### Features Used

| Feature    | Description                |
| ---------- | -------------------------- |
| MedInc     | Median Income              |
| HouseAge   | Average House Age          |
| AveRooms   | Average Number of Rooms    |
| AveBedrms  | Average Number of Bedrooms |
| Population | Population in Area         |
| AveOccup   | Average Occupancy          |
| Latitude   | Geographic Latitude        |
| Longitude  | Geographic Longitude       |

### Target Variable

**MedHouseVal** → Median House Value

---

## 🤖 Machine Learning Model

### Algorithm Used

**Linear Regression**

Linear Regression establishes a relationship between the input features and house prices and predicts the expected house value.

---

## 📈 Model Performance

| Metric   | Value  |
| -------- | ------ |
| RMSE     | 0.7456 |
| R² Score | 0.5758 |

### Interpretation

* RMSE measures prediction error.
* R² Score indicates how well the model explains the variance in house prices.
* The model explains approximately **57.58%** of the variation in house values.

---

## 📋 Feature Coefficients

| Feature    | Coefficient |
| ---------- | ----------- |
| MedInc     | 0.448675    |
| HouseAge   | 0.009724    |
| AveRooms   | -0.123323   |
| AveBedrms  | 0.783145    |
| Population | -0.000002   |
| AveOccup   | -0.003526   |
| Latitude   | -0.419792   |
| Longitude  | -0.433708   |

---

## 🔮 Sample Prediction

Example Predicted House Price:

```python
Predicted House Price: 4.2123
```

---
 ▶️ How to Run the Project
 1. Clone Repository

```bash
git clone https://github.com/Shivanshi963/Syntecxhub_House_Price_Prediction.git

2. Navigate to Project Folder

```bash
cd Syntecxhub_House_Price_Prediction
```
3. Install Dependencies

```bash
pip install -r requirements.txt

 4. Run Project

```bash
python house_price_prediction.py

 💾 Model Output

The trained model is saved as:

```text
models/house_price_model.pkl
```

This model can be loaded later without retraining.

🎯 Learning Outcomes

* Data Preprocessing
* Feature Engineering
* Machine Learning Fundamentals
* Linear Regression
* Model Evaluation
* Model Persistence
* Git & GitHub Workflow

👩‍💻 Author
**Shivanshi Singh**

GitHub: https://github.com/Shivanshi963

⭐ Acknowledgements

* Scikit-Learn
* California Housing Dataset

