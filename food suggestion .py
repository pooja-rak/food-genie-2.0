import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.ensemble import RandomForestClassifier 
import joblib
df=pd.read_csv('generated_food_dataset_6000.csv')
print("The Original Dataset:")
print(df)
print("\nThe columns in the Dataset:")
print(df.columns)
print("\nThe diet_type columns unique value")
print(df['diet_type'].unique())
print("\nThe food_health_preference columns unique value")
print(df['food_health_preference'].unique())
print("\nThe taste_preference columns unique value")
print(df['taste_preference'].unique())
print("\nThe preferred_cuisine columns unique value")
print(df['preferred_cuisine'].unique())
print("\nThe allergies columns unique value")
print(df['allergies'].unique())
print("\nThe budget_range columns unique value")
print(df['budget_range'].unique())
print("\nThe location columns unique value")
print(df['location'].unique())
print("\nThe digestion_preference columns unique value")
print(df['digestion_preference'].unique())
print("\nThe user_age columns unique value")
print(df['user_age'].unique())
print("\nThe current_weather columns unique value")
print(df['current_weather'].unique())
print("\nThe meal_time columns unique value")
print(df['meal_time'].unique())
print("\nThe calorie_preference columns unique value")
print(df['calorie_preference'].unique())
print("\nThe suggested_dish columns unique value")
print(df['suggested_dish'].unique())
df.fillna('None', inplace=True)
label_encoders={}
for column in ['diet_type','food_health_preference','taste_preference','preferred_cuisine','allergies','location','digestion_preference','current_weather','meal_time','suggested_dish']:
   le=LabelEncoder()
   df[column]=le.fit_transform(df[column])
   label_encoders[column] = le
x=df[['diet_type','food_health_preference','taste_preference','allergies','preferred_cuisine','digestion_preference','current_weather','meal_time']]
y=df['suggested_dish']
model=RandomForestClassifier(n_estimators=200)
model.fit(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
y_pred=model.predict(x_test)
print("\nPrected values")
print(y_pred)
ar=accuracy_score(y_test, y_pred)
print(f"\nThe Accuracy of Model {ar*100:.2f}")
con=confusion_matrix(y_test, y_pred)
print("\n the confusion Matrix of the Dataset\n",con)
cr=classification_report(y_test, y_pred,zero_division=0)
print("\n The classification report:\n",cr)
sns.heatmap(con,fmt='d',annot=True,cmap='Blues')
plt.show()

joblib.dump(model,'food_rand.pkl', compress=3)
joblib.dump(label_encoders,'label_encoders.pkl')

