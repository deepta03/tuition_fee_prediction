import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df=pd.read_csv('Tuition fees international students.csv')
plt.scatter(df.year, df.tuition)
plt.show()

model = LinearRegression().fit(df[['year']].values, df['tuition'].values)

y= model.predict([[2024], [2025], [2026]])

print("Predicted tuition rate for 2024 is", y[0])
print("Predicted tuition rate for 2025 is", y[1])
print("Predicted tuition rate for 2026 is", y[2])



