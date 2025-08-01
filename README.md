# PRODIGY_ML_01
# 🏡 House Price Prediction Model

This project is part of the **PRODIGY ML Internship** and demonstrates a basic machine learning pipeline to predict house prices based on features such as square footage, number of bedrooms, and number of bathrooms using **Linear Regression**.

---

## 📁 Project Structure

PRODIGY_ML_01/
│
├── Dataset/
│   ├── train.csv               # Training dataset
│   ├── test.csv                # Test dataset
│   ├── sample_submission.csv   # Sample submission format
│   └── data_description.txt    # Dataset feature descriptions
│
├── Task_01.py                  # Python script for house price prediction
├── predicted_prices.csv        # Output predictions generated from the model
├── README.md                   # Project documentation (you're reading it!)
│
└── .gitignore                  # Files/folders ignored by Git (if any)



---

## 🧠 Problem Statement

Given housing data, predict the sale price of a house using key features:
- `GrLivArea` — above ground living area (square feet)
- `BedroomAbvGr` — number of bedrooms
- `FullBath` — number of full bathrooms

---

## 🚀 Technologies Used

- Python 🐍
- pandas
- scikit-learn
- Git & GitHub

---

## 📈 Model

**Algorithm**: Linear Regression  
**Target variable**: `SalePrice`

The model is trained on `train.csv` and generates predictions for the `test.csv` file. The results are formatted according to `sample_submission.csv` and saved as `predicted_prices.csv`.

---

## 🛠 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Yash-Sharma1511-ji/PRODIGY_ML_01.git
cd PRODIGY_ML_01
