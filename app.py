import joblib
import streamlit as st
import pandas as pd

# Load model
model = joblib.load("food_rand.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Page config
st.set_page_config(page_title="Food Genie 🍽️", page_icon="🍽️", layout="wide")

# Sidebar Navigation
page = st.sidebar.radio("📌 Navigate", ["🏠 Home", "🔮 Prediction", "🍽️ Result", "👩‍💻 About"])

# -------------------- HOME PAGE --------------------
# -------------------- HOME PAGE --------------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center;'>🍽️ Food Genie 2.0</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='max-width:800px; margin:auto; font-size:18px; line-height:1.8;'>

    <h3>🌱 The Beginning...</h3>
    Ever felt confused about <b>what to eat</b>?  
    You open the fridge, scroll through food apps, and still end up unsure...  

    That’s where <b>Food Genie</b> was born 💡  
    A simple idea — <i>"What if a system could suggest food based on how you feel?"</i>

    <br><br>

    <h3>⚙️ Version 1.0</h3>
    The first version focused on basic inputs like:
    <ul>
    <li>Diet type</li>
    <li>Cravings</li>
    <li>Meal time</li>
    </ul>
    It worked... but something was missing 🤔  
    It didn’t fully understand <b>you</b>.

    <br><br>

    <h3>🚀 Introducing Food Genie 2.0</h3>
    This version is smarter, more aware, and more personalized.

    Now it considers:
    <ul>
    <li>🌦️ Weather conditions</li>
    <li>💪 Health preferences</li>
    <li>⚠️ Allergies</li>
    <li>🧠 Digestion comfort</li>
    </ul>

    It’s no longer just a suggestion system —  
    it’s a <b>personalized food decision assistant</b> 🧠✨

    <br><br>

    <h3>🎯 Why Version 2.0 is Better?</h3>
    ✔ More features = Better accuracy  
    ✔ Real-life factors included  
    ✔ Improved dataset & model learning  
    ✔ More user-friendly experience  

    <br><br>

    <h3>💬 Your Turn</h3>
    Instead of guessing what to eat…  
    let <b>Food Genie 2.0</b> decide for you 🍜✨  

    👉 Head to the <b>Prediction Page</b> and try it now!

    </div>
    """, unsafe_allow_html=True)

# -------------------- PREDICTION PAGE --------------------
elif page == "🔮 Prediction":
    st.title("🔮 Get Your Food Suggestion")

    col1, col2 = st.columns(2)

    with col1:
        a = st.selectbox("🥗 Diet Preference", ["vegetarian","vegan","non-vegetarian"])
        c = st.selectbox("😋 Craving Type", ["salty","spicy","savory","sweet","umami"])
        e = st.selectbox("🌍 Cuisine", ["Indian","Thai","Mexican","Italian","Chinese"])
        g = st.selectbox("🌦️ Weather", ["humid","cold","rainy","sunny","hot"])

    with col2:
        b = st.selectbox("💪 Health Preference", ["low carb","high protein","balanced","low fat"])
        d = st.selectbox("⚠️ Allergies",["dairy","gluten","nuts","soy","none"])
        f = st.selectbox("🧠 Digestion",["easy","moderate","heavy"])
        h = st.selectbox("⏰ Meal Time",["breakfast","lunch","dinner"])

    if st.button("✨ Suggest Food"):
        user_input = {
            'diet_type': a,
            'food_health_preference': b,
            'taste_preference': c,
            'allergies': d,
            'preferred_cuisine': e,
            'digestion_preference': f,
            'current_weather': g,
            'meal_time': h
        }

        # Store in session
        st.session_state["user_input"] = user_input
        st.session_state["predict"] = True

        st.success("✅ Preferences saved! Go to Result page 🍽️")

# -------------------- RESULT PAGE --------------------
elif page == "🍽️ Result":
    st.title("🍽️ Your Food Recommendation")

    if "predict" not in st.session_state:
        st.warning("⚠️ Please fill the Prediction page first!")
    else:
        user_input = st.session_state["user_input"]

        try:
            encoded_input = []
            for col in ['diet_type','food_health_preference','taste_preference','allergies','preferred_cuisine','digestion_preference','current_weather','meal_time']:
                val = label_encoders[col].transform([user_input[col]])[0]
                encoded_input.append(val)

            input_df = pd.DataFrame([encoded_input], columns=[
                'diet_type','food_health_preference','taste_preference','allergies',
                'preferred_cuisine','digestion_preference','current_weather','meal_time'
            ])

            prediction = model.predict(input_df)
            food = label_encoders['suggested_dish'].inverse_transform(prediction)

            st.markdown(f"""
            <div style='text-align:center; padding:20px; border-radius:15px; background-color:#000000;'>
            <h2>🥗 Recommended for You</h2>
            <h1 style='color:green;'>{food[0]}</h1>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

# -------------------- ABOUT PAGE --------------------
elif page == "👩‍💻 About":
    st.title("👩‍💻 About Food Genie")

    st.markdown("""
    ### 💡 Project Overview
    Food Genie is a Machine Learning-based food recommendation system that suggests dishes based on user preferences.

    ### ⚙️ Features
    - Personalized recommendations
    - Multiple input factors (diet, weather, cravings)
    - User-friendly interface
    - Fast predictions

    ### 🧠 Tech Stack
    - Python
    - Scikit-learn
    - Streamlit
    - Pandas

    ### 👩‍💻 Developer
    **Pooja Rajaram**  
    MCA Student | Future ML Engineer 🚀

    ### ⚠️ Disclaimer
    This model provides suggestions based on trained data and may not always be 100% accurate.
    """)

# Footer
st.markdown("---")
st.caption("✨ Created by Pooja Rajaram using Machine Learning")