import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set seed for reproducibility
np.random.seed(42)

# Sample weather data
data = {
    'MinTemp': np.random.uniform(10, 25, 100),
    'MaxTemp': np.random.uniform(28, 40, 100),
    'Humidity': np.random.uniform(40, 90, 100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("Sample Weather Data:")
print(df.head())

# Define features and target
X = df[['MinTemp', 'Humidity']]  # Features
y = df['MaxTemp']                # Target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# Plot Actual vs Predicted
plt.scatter(y_test, y_pred, color='red')
plt.xlabel('Actual MaxTemp')
plt.ylabel('Predicted MaxTemp')
plt.title('Actual vs Predicted MaxTemp')
plt.grid(True)
plt.show()
