import pandas as pd
df=pd.read_csv("Project1.csv")
df.head()
df.isnull().sum()

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
df = df.dropna()

df = df.replace({"Yes":1, "No":0}).infer_objects(copy=False)

df = df.drop(columns=["customerID"], errors='ignore')
cat_cols = df.select_dtypes(include='object').columns
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# df.head()
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
# plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
x = df.drop(columns=["Churn"])
y=df["Churn"]

model = LogisticRegression(max_iter=1000, class_weight='balanced')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
model.fit(x_train,y_train)
df.info()
y_prob = model.predict_proba(x_test)[:,1]
y_pred = (y_prob > 0.45).astype(int)
print(y_pred)
print(accuracy_score(y_test,y_pred))
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=200, random_state=42,class_weight='balanced')


model.fit(x_train, y_train)
y_prob = model.predict_proba(x_test)[:,1]
y_pred = (y_prob > 0.40).astype(int)
print(y_pred)
print(accuracy_score(y_test,y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
from xgboost import XGBClassifier
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=4,
    scale_pos_weight=3,   
    eval_metric='logloss',
    random_state=42
)
model.fit(x_train, y_train)
y_prob = model.predict_proba(x_test)[:,1]
y_pred = (y_prob > 0.40).astype(int)
print(y_pred)
print(accuracy_score(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
importance = pd.Series(model.feature_importances_, index=x.columns)
importance.sort_values(ascending=False).head(10)
