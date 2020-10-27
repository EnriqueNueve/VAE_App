import streamlit as st

from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import backend as K
from tensorflow.keras import Model

##########

codings_size = 1000

interpreter = tf.lite.Interpreter(model_path="decoder_lite.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

##########


# Present title
st.title('Variational Autoencoder')
st.text('This app presents an interactive Variational Autoencoder, where  \nyou can explore how changing the mean and variance value of the normal random  \nvariable used to generate values from the latent vector affects generated  \nsamples.')


# Explain data
st.header('Training Data')
st.text('For the training of the  Variational Autoencoder (VAE), the CFD dataset \n(https://chicagofaces.org/default/) was used. This dataset consists of \nhigh-quality pictures of faces from an array of people. By training the \nVAE on this face dataset, the VAE becomes capable of generating new face \nimages. Below are two examples of the images from the CFD dataset.')


img1 = Image.open('36.jpg')
img2 = Image.open('57.jpg')

st.image(img1,use_column_width=True)
st.image(img2,use_column_width=True)


# Explain how to make images
st.header('Generate Images')
st.text('To generate images from the VAE trained on the CFD dataset, first adjust the \nsliders for the desired mean and variance value, then click Make Image, and Walla!')
st.text('The quality of the generated imgaes ... well uhmm hmm maybe I\'ll try a GAN next time.')

mean = st.slider('mean',min_value=-10.0,max_value=10.0,value=0.0,step=.05)
std = st.slider('standard deviation',min_value=0.01,max_value=10.0,value=1.0,step=.05)

st.write("Mean: ",mean)
st.write("Std: ", std)

if st.button("Make Image"):
    input_data = tf.random.normal([1, codings_size],mean=-.5,stddev=1)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    g_img = interpreter.get_tensor(output_details[0]['index'])
    g_img = g_img[0,:,:,:]*255
    g_img = g_img.astype(int)

    st.image(g_img,use_column_width=True)
