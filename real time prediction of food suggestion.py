import joblib
import sys
import pandas as pd

model=joblib.load("food_rand.pkl")
label_encoders=joblib.load("label_encoders.pkl")

print("Food diet Preference\n 1. Vegetarian \n 2. Vegan \n 3. Non-Vegetarian")
a = input("Enter your Choice: ")

if a == "1":
    a_ = "vegetarian"
elif a == "2":
    a_ = "vegan"
elif a == "3":
    a_ = "non-vegetarian"
else:
    print("Invalid Choice")
    sys.exit()
print("Food health preference \n 1. Low carb \n 2. High protein \n 3. Balanced \n 4. Low fat")
b = input("Enter your choice: ")

if b == "1":
    b_ = "low carb"
elif b == "2":
    b_ = "high protein"
elif b == "3":
    b_ = "balanced"
elif b == "4":
    b_ = "low fat"
else:
    print("Invalid Choice")
    sys.exit()

print("Craving type \n 1. Salty \n 2. Spicy \n 3. Savory \n 4. Sweet \n 5. umami")
c = input("Enter your choice: ")

if c == "1":
    c_ = "salty"
elif c == "2":
    c_ = "spicy"
elif c == "3":
    c_ = "savory"
elif c == "4":
    c_ = "sweet"
elif c == "5":
    c_ = "umami"
else:
    print("Invalid Choice")
    sys.exit()

print("Do you have any allergies? \n 1. Dairy \n 2. Gluten \n 3. Nuts \n 4. Soy \n 5. None")
d = input("Enter your Option: ")

if d == "1":
    d_ = "dairy"
elif d == "2":
    d_ = "gluten" 
elif d == "3":
    d_ = "nuts"
elif d == "4":
    d_ = "soy"
elif d == "5":
    d_ = "none"
else:
    print("Invalid Choice")
    sys.exit()

print("what kinda cuisine you want to eat \n 1. Indian \n 2. Thai \n 3. Mexican \n 4. Italian \n 5. Chinese")
e = input("Enter your Option: ")

if e == "1":
    e_ = "Indian"
elif e == "2":
    e_ = "Thai" 
elif e == "3":
    e_ = "Mexican"
elif e == "4":
    e_ = "Italian"
elif e == "5":
    e_ = "Chinese"
else:
    print("Invalid Choice")
    sys.exit()
print("Digestion preferences: \n 1. Easy \n 2. Moderate \n 3. Heavy")
f = input("Enter your preferences:")

if f == "1":
    f_="easy"
elif f == "2":
    f_="moderate"
elif f == "3":
    f_="heavy"
else:
    print("Invalid Choice")
    sys.exit()
    
print("current weather: \n 1. Humid \n 2. Cold \n 3. Rainy \n 4. Sunny \n 5. Hot")
g = input("Enter the weather:")

if g == "1":
    g_="humid"
elif g == "2":
    g_="cold"
elif g == "3":
    g_="rainy"
elif g == "4":
    g_="sunny"
elif g =="5":
    g_ ="hot"
else:
    print("Invalid Choice")
    sys.exit()
    
print("meal time: \n 1. Breakfast \n 2. Lunch \n 3. Dinner")
h = input("Enter your preferences:")

if h == "1":
    h_="breakfast"
elif h == "2":
    h_="lunch"
elif h == "3":
    h_="dinner"
else:
    print("Invalid Choice")
    sys.exit()

# Example: returning these from a function or module
print("\n--- Your Selections ---")
print("Food diet Preference:", a_)
print("Food health preference", b_)
print("Craving:", c_)
print("Allergy:", d_)
print("Cuisine:", e_)
print("Digestion:",f_)
print("Weather:",g_)
print("Meal time:",h_)
new = {
    'diet_type': a_,
    'food_health_preference': b_,
    'taste_preference': c_,
    'allergies': d_,
    'preferred_cuisine': e_,
    'digestion_preference': f_,
    'current_weather':g_,
    'meal_time':h_
}
encoded_input = []
for col in ['diet_type','food_health_preference','taste_preference','allergies','preferred_cuisine','digestion_preference','current_weather','meal_time']:
    try:
        val = label_encoders[col].transform([new[col]])[0]
        encoded_input.append(val)
    except ValueError:
        print(f"Invalid value for {col}: {new[col]}")
        exit()
input_df = pd.DataFrame([encoded_input], columns=['diet_type','food_health_preference','taste_preference','allergies','preferred_cuisine','digestion_preference','current_weather','meal_time'])
prediction = model.predict(input_df)
food = label_encoders['suggested_dish'].inverse_transform(prediction)
print("Recommended Food according to your preferences:", food[0])
print("This model is Predict the suggestion according to the trained dataset")
