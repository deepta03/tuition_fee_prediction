# Tuition Fee Prediction
## Introduction
This project aims to predict future tuition fees for international undergrad students at the University of Manitonba using machine larning. A manually curated dataset based on the information from the University of Manitoba website was used for the prediction. The dataset was represented in a scatterplot capitalizing on Python's matplotlib library. Later, the linear regression model from Python’s machine learning library, scikit-learn was applied to predict the tuition fees for 2024, 2025 and 2026. To facilitate the application of the model, the values were rounded up in Excel.
## Dataset
For simplification, the dataset used in this project was manually curated and based on the information from the University of Manitoba website. The dataset contains tuition rates per 3-credit-hour science courses for international students from 2012 to 2023. The original tuition fee values were rounded up in MS Excel 2013 to ensure that the linear regression model fits on the dataset. The dataset was read using Pandas library.
## Visualization
Matplotlib library was used to visualise the dataset. The scatter plot shows the tuition fees for international students from 2012 to 2023. The x-axis represents the year, and the y-axis represents the tuition fee. The scatter plot shows an increasing trend in tuition fees for international students over the years.

![Scatterplot](https://user-images.githubusercontent.com/102154139/225447627-4f4355b0-8236-4469-b5f3-7a264107eb5f.JPG)


## Machine Learning Model
The tuition fees for 2024, 2025, and 2026 were predicted using the linear regression model from Scikit-learn library. Linear regression is a statistical method that allows the study of the relationship between two continuous variables. In this case, the relationship between the year and tuition fees was studied. The fit() method was used to fit the model on the dataset, and the predict () method was used to predict tuition fees for future years.
## Results
The predicted tuition fees for international undergraduate students at the University of Manitoba for the years 2024, 2025, and 2026 are as follows:

![Results](https://user-images.githubusercontent.com/102154139/225447141-df1ec4d4-a95b-4725-8edb-6c06613dabab.JPG)


## Implementation
Python 3.10, Pandas, Matplotlib, and Scikit-learn libraries were used to implement this project. The original tuition fee values were rounded up in MS Excel 2013. The project was implemented as follows:
- Rounding up the original tuition fee values in MS Excel 2013
- Reading the dataset using Pandas library
- Visualizing the dataset using Matplotlib library
- Fitting the linear regression model on the dataset
- Predicting tuition fees for 2024, 2025, and 2026 
## Conclusion
In this project, the tuition fees for international undergraduate students at the University of Manitoba were predicted using machine learning. This project can help students who are planning to study at the University of Manitoba and want to have an idea of the tuition fees in future years.


