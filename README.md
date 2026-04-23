# Food Genie 2.0

An intelligent **Machine Learning-based food recommendation system** that suggests personalized dishes based on your preferences, health goals, and real-world conditions.

---

## Live Demo

**Link:** https://food-genie-20-focdl8vwyvmhbwsqdkmsax.streamlit.app/

---

## Overview

Ever struggled with the question:
**“What should I eat today?”**

Food Genie 2.0 solves this problem by acting as your **smart food assistant**, analyzing your inputs and recommending the most suitable dish.

This is an improved version of the original Food Genie, designed to provide **more accurate and personalized suggestions**.

---

## What’s New in Version 2.0

✔ Added real-world factors like **weather conditions** 
✔ Included **health preferences** (low carb, high protein, etc.)
✔ Supports **allergy awareness**
✔ Considers **digestion comfort levels** 
✔ Improved dataset and model performance
✔ Better and more user-friendly UI

 Food Genie 2.0 is not just a recommender — it’s a **personalized food decision assistant**.

---

## How It Works

The model takes multiple inputs from the user:

* Diet Type (Vegetarian / Vegan / Non-Vegetarian)
* Health Preference (Low Carb / High Protein / etc.)
* Craving Type (Sweet / Spicy / etc.)
* Allergies
* Preferred Cuisine
* Digestion Preference
* Current Weather
* Meal Time

These inputs are processed and encoded using **Label Encoding**, then passed into a trained **Machine Learning model** to predict the most suitable dish.

---

## Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **Scikit-learn** (ML Model)
* **Pandas** (Data Handling)
* **Joblib** (Model Serialization)

---

## Project Structure

```id="wdb4jc"
Food-Genie-2.0/
│
├── app.py
├── food_rand.pkl
├── label_encoders.pkl
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1️. Clone the repository

git clone https://github.com/your-username/food-genie-2.0.git
cd food-genie-2.0
```

### 2️. Install dependencies

pip install -r requirements.txt
```

### 3️. Run the app

streamlit run app.py
```

---

## Features

Personalized food recommendations
Multi-factor decision making
Clean and user-friendly UI
Fast predictions
Real-life applicability

---

## Disclaimer

The recommendations are based on trained data and may not always be 100% accurate.

---

## Author

**Pooja Rajaram**
MCA Student
Aspiring Machine Learning Engineer

---

## Future Improvements

* Add food images
* Show model confidence score
* Enhance deployment scalability
* Improve mobile responsiveness

---


