import streamlit as st
from PIL import Image
import io

# Set config
st.set_page_config(page_title="Result", layout="centered")

# Custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Prediction Result</h1>", unsafe_allow_html=True)

# Show uploaded image
if 'image_data' in st.session_state and st.session_state.image_data:
    image = Image.open(io.BytesIO(st.session_state.image_data))
    st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    st.error("No image found. Please upload an image first.")
    st.stop()

# Show prediction
st.markdown(f"<div class='result'><strong>{st.session_state.prediction}</strong><br>Confidence: {st.session_state.confidence:.2%}</div>", unsafe_allow_html=True)

# Back button
if st.button("Back"):
    st.switch_page("app.py")
