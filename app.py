import streamlit as st
from PIL import Image, ImageEnhance

with st.expander("Open Camera") :
    #start the camera
    cam_img=st.camera_input("Camera")

if cam_img:
    img=Image.open(cam_img)     #create Pillow image instance

    option = st.selectbox("options",("grayscale", "brightness", "sharpness"))
    st.write(option)

    match option:
        case "grayscale":
            gray_img = img.convert("L")  # convert Pillow image to grayscale
            st.image(gray_img)          #display the grayscale image to webpage
        case "sharpness":
            imge = ImageEnhance.Sharpness(img)
            st.image(imge.enhance(5.0))
        case "brightness":
            imgb=ImageEnhance.Brightness(img)
            st.image(imgb.enhance(2.0))

