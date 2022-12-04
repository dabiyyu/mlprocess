import streamlit as st
import requests
import joblib
from PIL import Image

# Load and set images in the first place
header_images = Image.open('assets/banner.png')
st.image(header_images)

# Add some information about the service
st.title("Full Load Electrical Power Output Prediction")
st.subheader("Enter variabel below")

# Create form of input
with st.form(key = "power_plant_data_form"):
    # Create box for number input
    at = st.number_input(
        label = "Enter ambient temperature value:",
        min_value = 0,
        max_value = 40,
        help = "Value range from 0 to 40"
    )

    v = st.number_input(
        label = "Enter exhaust steam pressure value:",
        min_value = 25,
        max_value = 85,
        help = "Value range from 25 to 85"
    )
    
    ap = st.number_input(
        label = "Enter atmospheric pressure value:",
        min_value = 950,
        max_value = 1050,
        help = "Value range from 950 to 1050"
    )

    rh = st.number_input(
        label = "Enter relative humidity value:",
        min_value = 25,
        max_value = 125,
        help = "Value range from 25 to 125"
    )
    
    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form
        raw_data = {
            "AT": at,
            "V": v,
            "AP": ap,
            "RH": rh
        }

        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            res = requests.post("http://localhost:8080/predict", json = raw_data).json()
            
        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            st.success(res["res"])