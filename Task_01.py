import pandas as pd
from sklearn.linear_model import LinearRegression

# Load datasets
train_df = pd.read_csv(r'C:\Users\BOSS\Desktop\PRODIGY_ML_01\Dataset\train.csv')
test_df = pd.read_csv(r'C:\Users\BOSS\Desktop\PRODIGY_ML_01\Dataset\test.csv')
sample_submission = pd.read_csv(r'C:\Users\BOSS\Desktop\PRODIGY_ML_01\Dataset\sample_submission.csv')

# Use correct column names from the dataset
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
target = 'SalePrice'

# Drop rows with missing values in selected features or target
train_df.dropna(subset=features + [target], inplace=True)

# Prepare training data
X_train = train_df[features]
y_train = train_df[target]

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Prepare test data 
test_df.fillna(0, inplace=True) 
X_test = test_df[features]

# Predict house prices
predictions = model.predict(X_test)

# Prepare submission
submission = sample_submission.copy()
submission['SalePrice'] = predictions

# Save the output
submission.to_csv(r'C:\Users\BOSS\Desktop\PRODIGY_ML_01\Dataset\predicted_prices.csv', index=False)
print(" Prediction file saved as 'predicted_prices.csv'")
