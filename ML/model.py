import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


data = {
    'area': [1400, 1600, 1700, 1885, 1100, 1550, 2350, 2450, 1425, 1700],
    'bedrooms': [3, 3, 3, 2, 2, 3, 4, 4, 3, 3],
    'age': [10, 15, 20, 10, 5, 7, 20, 20, 6, 8],
    'price': [24500, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000]
}

df = pd.DataFrame(data)

X = df[['area', 'bedrooms', 'age']]
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open('house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)