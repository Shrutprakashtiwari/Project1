# 📊 Customer Churn Prediction

## 🚀 What this project is about

This project focuses on predicting whether a customer will churn or not. But instead of just building a model and reporting accuracy, the goal here was to understand how different models behave and how their predictions can be used in real-world decision making.

---

## 🧠 My Approach

I didn’t rely on a single model. I experimented with multiple models to understand their strengths and weaknesses:

* Logistic Regression → good for understanding patterns
* Random Forest → balanced performance
* XGBoost → aggressive prediction of churn
* Ensemble Model → combines strengths of all models

---

## ⚙️ What I did differently

Instead of stopping at model accuracy, I focused on:

* Comparing multiple models
* Understanding precision vs recall trade-off
* Applying threshold tuning to control predictions
* Building an ensemble model for better stability

This helped me move from just “training models” to actually thinking about how predictions are used in practice.

---

## 📊 Results

| Model               | Recall   | Precision |
| ------------------- | -------- | --------- |
| Logistic Regression | 0.83     | 0.48      |
| Random Forest       | 0.59     | 0.56      |
| XGBoost             | 0.86     | 0.46      |
| Ensemble (Final)    | **0.76** | **0.50**  |

---

## 🎯 Key Insight

There is no single best model.

* High recall models catch more churners but create false alarms
* High precision models are safer but miss customers

The final model balances both, depending on business needs.

---

## 💡 What I learned

* Model selection is not the most important part
* Threshold tuning can completely change results
* Ensemble models provide more stable predictions
* Real-world ML is about trade-offs, not perfect accuracy

---

## 📌 Conclusion

Most churn projects stop at building a model.
This project goes a step further by focusing on decision-making and practical application.

---

## 🛠️ Tech Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* SVM
* Logistic Regression
* Ensemble Learning
* Voting Classifier

---
