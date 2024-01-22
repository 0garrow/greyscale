import streamlit as st
from PIL import Image


def convert(image):
    # Create a pillow image instance.
    img = Image.open(image)

    # Convert the pillow image to greyscale
    grey_img = img.convert("L")

    # Render the greyscale image on the webpage
    st.image(grey_img)
    return


st.subheader("Color to Grayscale Converter")
st.text("Upload Image")
uploaded_image = st.file_uploader("Upload Image", key="upload")



with st.expander("Start Camera"):
    # Start the camera.
    camera_image = st.camera_input("Camera")


if camera_image:
    convert(camera_image)

if uploaded_image:
    convert(uploaded_image)