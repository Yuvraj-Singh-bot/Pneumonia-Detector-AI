import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load the trained model
model = tf.keras.models.load_model("pneumonia_detector_model.h5")

# Set Streamlit page config
st.set_page_config(page_title="Pneumonia Detector", layout="centered")

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Pneumonia Detection from Chest X-ray</h1>", unsafe_allow_html=True)

# Session state to hold image and prediction
if 'image_data' not in st.session_state:
    st.session_state.image_data = None
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'confidence' not in st.session_state:
    st.session_state.confidence = None

# Step 1: Upload Image
uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Store image bytes for next page
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    st.session_state.image_data = img_bytes.getvalue()

    # Predict Button
    if st.button("Predict"):
        resized_image = image.resize((150, 150))
        img_array = np.array(resized_image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0][0]
        label = "Pneumonia Detected 😷" if prediction > 0.5 else "Normal Lungs 🫁"
        confidence = prediction if prediction > 0.5 else 1 - prediction

        st.session_state.prediction = label
        st.session_state.confidence = confidence

        st.switch_page("pages/result.py")  # Navigate to result page
