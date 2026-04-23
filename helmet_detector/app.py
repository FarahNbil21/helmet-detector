import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
st.set_page_config(page_title="Helmet Detector", page_icon="⛑️")
st.title("Helmet & Safety Vest Detector")
st.write("Upload a photo or use the camera to verify your safety equipment")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'best.pt')

model = YOLO('best.pt')

option = st.radio("Choose input method:", ["Upload Image", "Camera"])

if option == "Upload Image":
    uploaded = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Original Image")
        with st.spinner("Analyzing..."):
            results = model.predict(np.array(image), conf=0.5)
            st.image(results[0].plot(), caption="Result ")

elif option == "Camera":
    img = st.camera_input("Capture Image")
    if img:
        image = Image.open(img)
        with st.spinner("Analyzing..."):
            results = model.predict(np.array(image), conf=0.5)
            st.image(results[0].plot(), caption="Result")
