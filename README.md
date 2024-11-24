# Industrial Copper Modeling: Predicting Sales Status and Selling Price

This project focuses on analyzing sales data from the copper industry to predict two critical outcomes:


1.Sales Status (Won or Lost) using classification.

2.Selling Price using regression.

By leveraging machine learning techniques, the project delivers actionable insights to optimize sales strategies and pricing decisions.


# Objectives

Predict Sales Status:

Classify leads as "Won" or "Lost" based on historical sales data.

Predict Selling Price:

Accurately forecast the selling price for each lead using input features.

Steps Involved

1. Data Cleaning
Processed a dataset of 180,000 rows to handle missing values, remove outliers, and address inconsistencies.
Applied transformations to correct skewed distributions, including logarithmic scaling for numerical features.

2. Data Preprocessing
Categorical Encoding:
Used Ordinal Encoding for structured categorical variables.

3. Scaling:
Standardized numerical features to ensure uniformity.

4. Class Imbalance:
Balanced the target classes (for status prediction) using SMOTE.

5. Exploratory Data Analysis (EDA)
Visualized relationships between features and target variables to uncover patterns and insights.
Identified influential factors impacting selling price and sales status through feature importance analysis.

6. Model Selection and Training
Selling Price Prediction:
Built and trained a Random Forest Regressor, achieving 93% accuracy on the test dataset.
Sales Status Prediction:
Used a Random Forest Classifier to classify leads, achieving 96% accuracy on the test dataset.

9. Model Evaluation
Selling Price:
Evaluated using metrics like Mean Squared Error (MSE) and R² Score.
Sales Status:
Evaluated using metrics such as Accuracy, Precision, and Recall.

Validated both models by predicting sales status and selling price on new input samples.

# Tools and Libraries Used

Programming Language: Python
Libraries:
Data Processing: pandas, numpy
Visualization: matplotlib, seaborn
Machine Learning: scikit-learn, imblearn
Model Evaluation: scikit-learn metrics

# Key Highlights

Data Handling: Processed and cleaned a large dataset of 180,000 rows effectively.
Feature Engineering: Used transformations like log scaling and ordinal encoding for better model performance.
Model Performance:

Selling Price Prediction:

93% Accuracy


Sales Status Prediction:

96% Accuracy

Models Used: Implemented Random Forest Regressor and Random Forest Classifier for accurate and interpretable predictions. 

# Summary
The Industrial Copper Modeling project showcases a robust approach to analyzing and predicting sales outcomes in the copper industry. By combining data preprocessing, feature engineering, and machine learning, the project delivers reliable insights for business optimization and decision-making.
