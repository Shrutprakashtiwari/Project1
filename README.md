#  Customer Churn Prediction: Model optimized for high recall to ensure maximum identification of potential churn customers, even at the cost of precision

##  Overview

This project focuses on predicting customer churn for a telecom company using machine learning techniques.
The goal is to identify customers who are likely to leave so that the business can take proactive retention actions.
This is made specially to focus on the people churning out.
I did it without using pipeline.

##  Problem Statement

Customer churn leads to significant revenue loss.
This project aims to build a predictive model that can:

* Identify customers likely to churn
* Help businesses reduce customer loss
* Support data-driven decision making

##  Dataset

* Telecom Customer Churn Dataset (~7000 customers)
* Features include:

  * Demographics (gender, senior citizen, etc.)
  * Account information (tenure, contract type)
  * Billing details (monthly charges, total charges)
  * Services used (internet, streaming, etc.)


##  Exploratory Data Analysis (EDA)

Key insights discovered:

*  Customers with **low tenure** are more likely to churn
*  Higher **monthly charges** are associated with higher churn
*  **Month-to-month contracts** have the highest churn rate
*  Long-term contracts significantly reduce churn


##  Data Preprocessing

* Converted categorical Yes/No values → 0/1
* Handled missing values in `TotalCharges`
* Applied **One-Hot Encoding** for categorical features
* Removed irrelevant columns (e.g., customerID)


##  Models Used

### 1. Logistic Regression

* Baseline model
* Tuned using class weights and threshold adjustment

### 2. Random Forest (Best Performing)

* Provided balanced performance
* Captured non-linear relationships effectively

### 3. XGBoost

* Tested with hyperparameter tuning
* Performance similar to Random Forest


##  Model Performance

| Model               | Accuracy   | Recall (Churn) | Precision (Churn) |
| ------------------- | ---------- | -------------- | ----------------- |
| Logistic Regression | ~0.68–0.79 | up to 0.86     | ~0.45–0.62        |
| Random Forest       | ~0.77      | ~0.58          | ~0.56             |
| XGBoost             | ~0.69      | ~0.86          | ~0.46             |


##  Key Takeaways

* There is a **trade-off between recall and precision**
* High recall helps capture more churners but increases false positives
* Random Forest provided the **best balance for practical use**
* Feature understanding is as important as model selection



##  Business Impact

Using this model, a company can:

* Identify high-risk customers early
* Offer targeted retention strategies (discounts, support, etc.)
* Reduce churn and improve revenue


##  Technologies Used

* Python
* Pandas, NumPy
* Seaborn, Matplotlib
* Scikit-learn
* XGBoost


##  Future Improvements

* Feature engineering (e.g., usage patterns, customer behavior)
* Hyperparameter tuning for advanced models
* Deployment as a web app or API
* Use of ensemble techniques


##  Conclusion

This project demonstrates an end-to-end machine learning pipeline, from data preprocessing to model evaluation and business interpretation.
The focus is not just on accuracy, but on making **practical, data-driven decisions**.


##  Author

Shrut
